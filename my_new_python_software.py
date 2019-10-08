# -*- coding: utf-8 -*-
import time
import concurrent.futures
from pythontools import *

def bla(v=1):
    verbose('running bla method','Process:', v, label='INFO')

def blabla():
    if 1==2:
        pass
    else:
        verbose('Something strange here, but its ok', label='WARN')

def blablabla():
    try:
        unexistent()
    except:
        verbose('Unexistent  function called', label='ERROR')

def runsleep():
    verbose('So tired. I\'ll get some sleep', label='INFO')
    time.sleep(1)
    verbose('Wake up. What\'s time is it?', label='WARN')

bla()
blabla()
verbose('I\'m a -vv INFO text', level=2, label='INFO')
verbose('I\'m a -vvv WARN text', level=3, label='WARN')
blablabla()
runsleep()

jobs = [1,2,3]

with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
    future_mbl = {executor.submit(bla, job): job for job in jobs}
