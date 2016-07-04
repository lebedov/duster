#!/usr/bin/env python 

"""
Configurable IPython namespace reset.
"""

# Copyright (c) 2013-2016, Lev Givon
# All rights reserved.
# Distributed under the terms of the BSD license:
# http://www.opensource.org/licenses/bsd-license

import importlib
import warnings

import IPython
from IPython.core.magic import Magics, magics_class, line_magic, \
                                cell_magic, line_cell_magic

# Version specific imports:
if IPython.release.version < '1.0.0':
    get_ipython = IPython.core.ipapi.get
else:
    get_ipython = IPython.core.getipython.get_ipython
ip = get_ipython()

if IPython.release.version < '4.0.0':
    from IPython.utils.traitlets import List
    cfg = ip.config
else:
    from traitlets import List
    import traitlets.config
    cfg = traitlets.config.get_config()

@magics_class
class DusterMagic(Magics):
    modules = List([], config=True,
                   help="List of (module, module import name) tuples to reload.")
    ignore = List([], config=True,
                  help="List of variables to ignore when resetting the namespace.")
    
    @line_magic
    def duster(self, line=''):
        """
        Configurable namespace reset.
    
        Selectively reset IPython namespace while reloading specified modules and 
        ignoring certain variables.
        
        To configure, run 

        %config DusterMagic

        Parameters
        ----------
        -f : force reset without asking for confirmation

        Examples
        --------
        ::
          In [1]: config DusterMagic.modules = [('numpy', 'np')]

          In [2]: import numpy as np
          
          In [3]: duster -f
         
          In [4]: who_ls module
          Out[4]: ['p']

          In [5]: config DusterMagic.ignore = ['xyz']
         
          In [6]: xyz = 1; abc = 2
    
          In [7]: duster -f
 
          In [8]: who_ls int
          Out[8]: ['xyz']
        """

        opts, args = self.parse_options(line, 'f')
        ip = get_ipython()

        ignore_list = [i for i in self.ignore if i]
        if ignore_list:
            ignore_regex = '^(?!%s)' % '|'.join(ignore_list)
            if 'f' in opts:
                ip.run_line_magic('reset_selective', '-f %s' % ignore_regex)
            else:
                ip.run_line_magic('reset_selective', ignore_regex)
        else:
            if 'f' in opts:
                ip.run_line_magic('reset', '-f')
            else:
                ip.run_line_magic('reset', '')
            
        for m in self.modules:
            try:
                if len(m) == 1:
                    ip.ns_table['user_global'][m[0]] = importlib.import_module(m[0])
                else:
                    ip.ns_table['user_global'][m[1]] = importlib.import_module(m[0])
            except ImportError:
                warnings.warn('cannot reimport %s - module not found' % m[0])

        # If IPython was started in pylab mode, reload symbols in pylab module directly
        # into namespace:
        if (cfg.has_key('IPKernelApp') and cfg['IPKernelApp'].has_key('pylab')) or \
           (cfg.has_key('TerminalIPythonApp') and cfg['TerminalIPythonApp'].has_key('pylab')):
            ip.ns_table['user_global']['pylab'] = importlib.import_module('pylab')
            for name in ip.ns_table['user_global']['pylab'].__dict__.keys():
                ip.ns_table['user_global'][name] = \
                    ip.ns_table['user_global']['pylab'].__dict__[name]

def load_ipython_extension(ip):
    ip.register_magics(DusterMagic)
