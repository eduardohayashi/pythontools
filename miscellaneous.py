import os
import fnmatch
from glob import glob
from random import randint
from typing import List, AnyStr
from datetime import datetime, timedelta


def pool_filter(pool, func, candidates):
    '''

    :param pool:
    :param func:
    :param candidates:
    :return:
    '''

    return [c for c, keep in zip(candidates, pool.map(func, candidates)) if keep]


def set_tags(text, **kwargs):
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


def __recursive_file_search(directory):
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


def find_files(localpath, recursive=False, **kwargs):
    '''

    :param localpath:
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