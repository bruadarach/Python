##### Techniques for Importing Modules #####
# => import modules, packages, names


### 1. To import an individual function or class from a module : 
from collections import defaultdict
# from module_name import object_name
# => importing an individual objects from a module


### 2. To import multiple individual objects from a module :
from collections import defaultdict, namedtuple
# you can import multiple individual objects from a module by separating them with commas.

"""
### no need to write . to access the object! 
collections.defaultdict()
# NameError: name 'collections' is not defined
"""

defaultdict()


### 3. To rename a module :
##### use 'as' to rename the module
import multiprocessing as mp

print(mp.cpu_count()) 
# 4
 

### 4. To import an object from a module and rename it :
##### input an intem from a module and change its name
from csv import reader as csvreader 
# it means, open from 'csv.py', and choose 'def reader', and rename def reader' to 'cscreader'


### 5. To import every object individually from a module (DO NOT DO THIS):
from os import *


### 6. If you really want to use all of the objects from a module, use the standard import module_name statement instead and access each of the objects with the dot notation.
import os



##### Package 
# a package is simply a module that contains sub-modules. 
# A sub-module is specified with the usual dot notation.
# e.g.) os / os.path

import os.path
# import package_name.submodule_name

os.path.isdir('my_path')