# -*- coding: utf-8 -*-

'''
    File name: argparse.py
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

settings_file = 'settings.py'
if os.path.isfile(settings_file):
    import settings

stop = False

try:
    description = settings.__description
except:
    description = ""

quotes_file = 'pythontools/.quotes'
if os.path.isfile('.quotes'):
    quotes_file = '.quotes'

epilog = '   '+random.choice(list(open(quotes_file)))

parser = argparse.ArgumentParser(description=description,
    formatter_class=argparse.RawTextHelpFormatter, epilog=epilog)
parser.add_argument("-v", "--verbose", action='count', dest='verbose_level',
    help='Make the operation more talkative', default=False)
parser.add_argument("-d", "--debug", action='store_true', dest='debug',
    help='Debug mode', default=False)
parser.add_argument("-t", "--timer", action='store_true', dest='time_measure',
    help='Measure time execution in microsseconds', default=False)

try:
    if os.path.isfile(settings_file):
        parser.add_argument("--settings", action='store_true', dest='show_settings',
            help='Show the settings and exit', default=False)
except:
    pass

try:
    if os.path.isfile(settings_file):
        for var in settings.__dir__():
            if not var.startswith("_"):
                try:
                    help = getattr(settings, f'__{var}')
                except:
                    help = ''
                parser.add_argument(f"--{var}", dest=var, help=help,
                    default=getattr(settings, var))
except:
    pass

args = parser.parse_args()

for v in dir(args):
    if not v.startswith("_") and getattr(args, v):
        setattr(settings, v, getattr(args, v))

try:
    if args.time_measure:
        settings.starttimer = timer()
except:
    pass

try:
    if args.verbose_level:
        settings.verbose_level = args.verbose_level
except:
    pass

try:
    if settings.show_settings:
        for v in dir(settings):
            if not v.startswith("_"):
                print(v, getattr(settings, v))
        stop = True
except:
    pass

if stop == True:
    sys.exit()
