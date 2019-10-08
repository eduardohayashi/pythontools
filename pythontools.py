# -*- coding: utf-8 -*-

'''
    File name: pythontools.py
    Python Version: 3.7
'''

__author__ = "Eduardo Hayashi"
__version__ = "0.1"

import os
import sys
import random
import argparse
import settings
from datetime import datetime
from timeit import default_timer as timer

try:
    description = settings.__description
except:
    description = ""

epilog = '    '+random.choice(list(open('.quotes')))

parser = argparse.ArgumentParser(description=description,
    formatter_class=argparse.RawTextHelpFormatter, epilog=epilog)
parser.add_argument("-v", "--verbose", action='count', dest='verbose',
    help='Make the operation more talkative', default=False)
parser.add_argument("-d", "--debug", action='store_true', dest='debug',
    help='Debug mode', default=False)
parser.add_argument("-t", "--timer", action='store_true', dest='time_measure',
    help='Measure time execution in microsseconds', default=False)
parser.add_argument("--settings", action='store_true', dest='show_settings',
    help='Show the settings and exit', default=False)

for var in settings.__dir__():
    if not var.startswith("_"):
        try:
            help = getattr(settings, f'__{var}')
        except:
            help = ''
        parser.add_argument(f"--{var}", dest=var, help=help,
            default=getattr(settings, var))

args = parser.parse_args()
for v in dir(args):
    if not v.startswith("_") and getattr(args, v):
        setattr(settings, v, getattr(args, v))

try:
    if args.time_measure:
        starttimer = timer()
except:
    pass

try:
    if settings.show_settings:
        for v in dir(settings):
            if not v.startswith("_"):
                print(v, getattr(settings, v))
        exit()
except:
    pass

class bcolors:
    INFO = '\033[92m'
    WARN = '\033[93m'
    ERROR = '\033[91m'
    ENDC = '\033[0m'

def verbose(*args, level=1, label='INFO', **kwargs):
    pid, time_measure, dt, source, module, method = '','','','','',''
    try:
        if settings.verbose >= level:
            dt = f'[{datetime.now():%Y-%m-%d %H:%M:%S}]'

            try:
                time_measure = f'[{round(timer()-starttimer,4)}ms]'
            except:
                pass

            try:
                label = getattr(bcolors, label)+f'[{label}]'+bcolors.ENDC

            except:
                label = f'[{label}]'

            try:
                if settings.debug:
                    pid = f'[{os.getpid()}]'
                    module_name = sys._getframe(1).f_globals['__name__']
                    module = f'[{module_name}]'
                    method_name = sys._getframe(1).f_code.co_name
                    method = f'[{method_name}]'
                    if method == '<module>':
                        method = f'[{sys.argv[0]}]'
            except:
                pass

            print(f'{label}{dt}{pid}{module}{method}{time_measure}', *args)

    except:
        pass
