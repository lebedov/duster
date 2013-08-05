#!/usr/bin/env python 
"""
IPython extension to reset namespace and reload several modules automatically
"""

import importlib
import IPython

# Modules to reload; each element contains the module and the name to which
# it should be imported (or '' if it should be imported as-is):
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

    # If IPython was started in pylab mode, reload symbols in pylab module directly
    # into namespace:
    cfg = ip.config
    if (cfg.has_key('IPKernelApp') and cfg['IPKernelApp'].has_key('pylab')) or \
       (cfg.has_key('TerminalIPythonApp') and cfg['TerminalIPythonApp'].has_key('pylab')):
        ip.ns_table['user_global']['pylab'] = importlib.import_module('pylab')
        for name in ip.ns_table['user_global']['pylab'].__dict__.keys():
            ip.ns_table['user_global'][name] = \
                ip.ns_table['user_global']['pylab'].__dict__[name]

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
