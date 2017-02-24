.. -*- rst -*-

Duster
======

Package Description
-------------------
Duster is an IPython extension that selectively clears one's IPython session 
namespace while automatically ignoring specified variables to preserve and 
reloading specified packages.

.. image:: https://img.shields.io/pypi/v/duster.svg
    :target: https://pypi.python.org/pypi/duster
    :alt: Latest Version
.. Uncomment after pypi is migrated to warehouse and stats are re-enabled:
.. https://github.com/badges/shields/issues/716
.. .. image:: https://img.shields.io/pypi/dm/duster.svg
    :target: https://pypi.python.org/pypi/duster
    :alt: Downloads

Installation
------------
The package may be installed as follows: ::

    pip install duster

After installation, the extension may be loaded within an IPython 
session with ::

    %load_ext duster

Configuration
-------------
Modules to be reloaded when duster is invoked should each be listed as a tuple 
containing the module name and the name to which it should be imported (or '' if 
it should be imported as-is). For example: ::

    c.DusterMagic.modules = [('numpy', 'np'), ('scipy', 'sp'), ('sys', '')]

Variables to be ignored when resetting the IPython namespace should be listed
by name as follows: ::

    c.DusterMagic.ignore = ['varname0', 'varname1']

The above settings may be viewed and/or modified within an IPython session using 
::

    %config DusterMagic

Notes
-----
Duster will automatically reload `pylab 
<http://matplotlib.org/users/shell.html>`_ if pylab mode is active.

Development
-----------
The latest release of the package may be obtained from
`GitHub <https://github.com/lebedov/duster>`_.

Author
------
See the included `AUTHORS.rst 
<https://github.com/lebedov/duster/blob/master/AUTHORS.rst>`_ file for more 
information.

License
-------
This software is licensed under the
`BSD License <http://www.opensource.org/licenses/bsd-license>`_.
See the included `LICENSE.rst 
<https://github.com/lebedov/duster/blob/master/LICENSE.rst>`_ file for more 
information.
