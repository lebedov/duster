#!/usr/bin/env python 

"""
IPython extension to reset namespace and reload several modules automatically
"""

# Copyright (c) 2013-2014, Lev Givon
# All rights reserved.
# Distributed under the terms of the BSD license:
# http://www.opensource.org/licenses/bsd-license

import importlib
import IPython
from IPython.core.magic import Magics, magics_class, line_magic, \
                                cell_magic, line_cell_magic

if IPython.release.version < '1.0.0':
    ip = IPython.core.ipapi.get()
else:
    ip = IPython.core.getipython.get_ipython()

# Modules to be reloaded; each element contains the module and the name to which
# it should be imported (or '' if it should be imported as-is):
if IPython.release.version < '4.0.0':
    cfg = ip.config
else:
    import traitlets.config as cfg
try:
    modules = cfg.Duster.modules
except AttributeError:
    modules = []

@magics_class
class DusterMagic(Magics):
    @line_magic
    def duster(self, line=''):
        opts, args = self.parse_options(line, 'f')
        if 'f' in opts:
            ip.run_line_magic('reset', '-f')
        else:
            ip.run_line_magic('reset', '')
        for m in modules:
            if len(m) == 1:
                ip.ns_table['user_global'][m[0]] = importlib.import_module(m[0])
            else:
                ip.ns_table['user_global'][m[1]] = importlib.import_module(m[0])

        # If IPython was started in pylab mode, reload symbols in pylab module directly
        # into namespace:
        if (cfg.has_key('IPKernelApp') and cfg['IPKernelApp'].has_key('pylab')) or \
           (cfg.has_key('TerminalIPythonApp') and cfg['TerminalIPythonApp'].has_key('pylab')):
            ip.ns_table['user_global']['pylab'] = importlib.import_module('pylab')
            for name in ip.ns_table['user_global']['pylab'].__dict__.keys():
                ip.ns_table['user_global'][name] = \
                    ip.ns_table['user_global']['pylab'].__dict__[name]

DusterMagic.duster.__func__.__doc__ = \
"""
Reset namespace and (re)load modules automatically.

Parameters
----------
-f : force reset without asking for confirmation

Reloaded Modules
----------------
"""
if modules:
    for m in modules:
        if len(m) == 1:
            DusterMagic.duster.__func__.__doc__ += "%s as %s\n" % (m[0], m[0])
        else:
            DusterMagic.duster.__func__.__doc__ += "%s as %s\n" % (m[0], m[1])
else:
    DusterMagic.duster.__func__.__doc__ += "None"

def load_ipython_extension(ip):
    ip.register_magics(DusterMagic)
