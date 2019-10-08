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

class bcolors:
    INFO = '\033[92m'
    WARN = '\033[93m'
    ERROR = '\033[91m'
    ENDC = '\033[0m'

def verbose(*args, level=0, label='INFO', **kwargs):
    pid, time_measure, dt, source, module, method = '','','','','',''
    try:
        if settings.verbose_level >= level:
            dt = f'[{datetime.now():%Y-%m-%d %H:%M:%S}]'

            try:
                time_measure = f'[{round(timer()-settings.starttimer,4)}ms]'
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
