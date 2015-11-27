.. -*- rst -*-

Duster
======

Package Description
-------------------
Duster is an IPython extension that clears one's IPython session namespace and 
automatically reloads specified packages.

.. image:: https://img.shields.io/pypi/v/duster.svg
    :target: https://pypi.python.org/pypi/duster
    :alt: Latest Version
.. image:: https://img.shields.io/pypi/dm/duster.svg
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
To specify modules that duster should reload when invoked, update 
IPython's configuration file. Each module should be listed as a tuple
containing the module name and the name to which it should be imported (or '' if
it should be imported as-is). For example: ::

    c.DusterMagic.modules = [('numpy', 'np'), ('scipy', 'sp'), ('sys', '')]

The modules can be viewed or modified within an IPython session using ::

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
See the included `AUTHORS.rst`_ file for more information.

.. _AUTHORS.rst: AUTHORS.rst

License
-------
This software is licensed under the
`BSD License <http://www.opensource.org/licenses/bsd-license>`_.
See the included `LICENSE.rst`_ file for more information.

.. _LICENSE.rst: LICENSE.rst
