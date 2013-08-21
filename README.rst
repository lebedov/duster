.. -*- rst -*-

Duster
======

Package Description
-------------------
Duster is an IPython extension that clears one's IPython session namespace and 
automatically reloads specified packages.

Installation
------------
The package may be installed as follows: ::

    pip install duster

Configuration
-------------
To specify modules that duster should reload when invoked, update 
IPython's configuration file. Each module should be listed as a tuple
containing the module name and the name to which it should be imported (or '' if
it should be imported as-is). For example: ::

    c.Duster.modules = [('numpy', 'np'), ('scipy', 'sp'), ('sys', '')]

Notes
-----
Duster will automatically reload pylab if IPython was started in pylab mode.

Development
-----------
The latest release of the package may be obtained from
`Github <https://github.com/lebedov/duster>`_.

Author
------
This software was written and packaged by Lev Givon.

License
-------
This software is licensed under the
`BSD License <http://www.opensource.org/licenses/bsd-license.php>`_.
See the included LICENSE file for more information.


