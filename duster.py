#!/usr/bin/env python                                                                                             
"""                                                                                                               
IPython extension to reset namespace and reload several modules automatically                                     
"""

import importlib
import IPython

# Modules to reload; if no name is specified as the                                                               
modules = [('numpy', 'np'),
           ('scipy', 'sp')]

ip = IPython.core.ipapi.get()
def duster(self, arg=''):
    ip.magic('reset')
    for m in modules:
        if len(m) == 1:
            ip.ns_table['user_global'][m[0]] = importlib.import_module(m[0])
        else:
            ip.ns_table['user_global'][m[1]] = importlib.import_module(m[0])

duster.__doc__ = \
"""                                                                                                               
Reset namespace and (re)load several modules automatically.                                                       
Modules currently reloaded:                                                                                       
                                                                                                                  
"""
for m in modules:
    if len(m) == 1:
        duster.__doc__ += "%s as %s\n" % (m[0], m[0])
    else:
        duster.__doc__ += "%s as %s\n" % (m[0], m[1])

def load_ipython_extension(ip):
     ip.define_magic('duster', duster)