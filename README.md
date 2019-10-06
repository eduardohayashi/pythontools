pythontools
===========

Python Development tools

### verbose( -v, --verbose )
Print smart, multilevel logs (-vv, -vvv, -vvvv)
```
verbose('running bla method','Process:', v, type='INFO')
verbose('Something strange here, but its ok', type='WARN')
verbose('I\'m a -vv INFO text', level=2, type='INFO')
verbose('I\'m a -vvv WARN text', level=3, type='WARN')
```
![Screenshot from 2019-10-05 23-40-15](https://user-images.githubusercontent.com/3841825/66261712-5e1ed600-e7ca-11e9-9e44-9dbf32eea402.png)

### Debug model (-d, --debug)
Print PID, module and method called

### Time measure ( -t, --timer)
Print time measure

![Screenshot from 2019-10-05 23-46-12](https://user-images.githubusercontent.com/3841825/66261713-5e1ed600-e7ca-11e9-86d4-228c19a5e909.png)
**[TYPE][DATE][PID][MODULE][METHOD][TIMER]** Message log

### CLI options
Automatically add option in argparse() to overwrite your app settings

![Screenshot from 2019-10-05 23-10-47](https://user-images.githubusercontent.com/3841825/66261517-c23f9b00-e7c6-11e9-947c-d5bc395dcb5f.png)

### install
Import code inside your applications:
```
from pythontools import *
```
