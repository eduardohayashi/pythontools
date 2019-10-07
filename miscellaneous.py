import os
import re
import gzip
import types
import tarfile
import zipfile
import fnmatch
from glob import glob
from random import randint
from typing import List, AnyStr
from datetime import datetime, timedelta


def pool_filter(pool, func, candidates):
    '''

    :param pool:
    :param func:
    :type func: types.FunctionType
    :param candidates:
    :return:
    '''

    if not isinstance(func, types.FunctionType):
        raise Exception('Function not defined')

    return [c for c, keep in zip(candidates, pool.map(func, candidates)) if keep]


def set_tags(text: str, **kwargs):
    '''

    :param text:
    :param kwargs:
    :return:
    '''

    tags = dict(
        today=datetime.today(), now=datetime.now(), yesterday=(datetime.today() - timedelta(days=1)),
        tomorrow=(datetime.today() + timedelta(days=1)), random_int=randint(0, 999999), current_time=datetime.now(),
        current_date=datetime.today()
    )
    tags.update(kwargs)

    return str(text).format(**tags)


def __recursive_file_search(directory: str):
    '''

    :param directory:
    :return:
    '''

    directory, pattern = os.path.split(directory)

    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename


def find_files(localpath, recursive: bool = False, **kwargs):
    '''

    :param localpath:
    :type localpath: list or str
    :param recursive:
    :param kwargs:
    :return:
    '''

    __set_tags = lambda i: set_tags(i, **kwargs.get('tags'))

    files: List[AnyStr] = list()
    localpath: List[AnyStr] = list(map(__set_tags, localpath)) if isinstance(localpath, list) else [
        __set_tags(localpath)]

    for item in localpath:
        if not isinstance(item, str):
            continue

        current_path = set_tags(item)
        directory, _ = os.path.split(current_path)

        if recursive:
            new_files: List[AnyStr] = list(__recursive_file_search(current_path))
        else:
            new_files: List[AnyStr] = list(glob(current_path))
            new_files = list(filter(lambda item: os.path.isfile(item), new_files))

        files += new_files

    return list(set(files))


def replace_many(text: str, adict: dict):
    '''

    :param text:
    :param adict:
    :return:
    '''

    regex = re.compile("|".join(map(re.escape, adict.keys())))
    return regex.sub(lambda match: adict[match.group(0)], text)


def decompress(filepath: str, outpath: str = None):
    '''

    :param filepath:
    :param outpath:
    :return:
    '''

    repl_func = lambda text: replace_many(text, {'.tar.gz': '', '.lzma': '', '.gz': '', '.zip': '', '.tar': ''})

    if outpath is None:
        func = lambda item: os.path.join('/'.join(filepath.split('/')[:-1]), repl_func(filepath.split('/')[-1]))
    else:
        func = lambda item: os.path.join(outpath, repl_func(filepath.split('/')[-1])) if outpath.endswith(
            '/') else outpath

    if filepath.endswith("tar.gz") or filepath.endswith("tar") or filepath.endswith("gz") or filepath.endswith("lzma"):
        try:
            with tarfile.open(filepath, "r:*") as tar:
                _path = repl_func(outpath)
                tar.extractall(path=_path)
        except tarfile.ReadError:
            if filepath.endswith("gz"):
                with gzip.open(filepath, 'rb') as gzip_ref:
                    _path = func('.gz')
                    with open(_path, 'wb') as nfile:
                        nfile.write(gzip_ref.read())

    elif filepath.endswith("zip"):
        with zipfile.ZipFile(filepath) as zip_ref:
            _path = func('.zip')
            zip_ref.extractall(path=_path)
    else:
        raise Exception(f'Unrecognized extension: {filepath}')

    return _path
