# -*- coding: utf-8 -*-
import time
import concurrent.futures
from pythontools import *

def bla(v=1):
    verbose('running bla method','Process:', v, type='INFO')

def blabla():
    if 1==2:
        pass
    else:
        verbose('Something strange here, but its ok', type='WARN')

def blablabla():
    try:
        unexistent()
    except:
        verbose('Unexistent  function called', type='ERROR')

def runsleep():
    verbose('So tired. I\'ll get some sleep', type='INFO')
    time.sleep(1)
    verbose('Wake up. What\'s time is it?', type='WARN')

bla()
blabla()
verbose('I\'m a -vv INFO text', level=2, type='INFO')
verbose('I\'m a -vvv WARN text', level=3, type='WARN')
blablabla()
runsleep()

jobs = [1,2,3]

with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
    future_mbl = {executor.submit(bla, job): job for job in jobs}
