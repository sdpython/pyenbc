
.. image:: https://travis-ci.com/sdpython/pyenbc.svg?branch=master
    :target: https://travis-ci.com/sdpython/pyenbc
    :alt: Build status

.. image:: https://ci.appveyor.com/api/projects/status/scv9gmggw7qc462i?svg=true
    :target: https://ci.appveyor.com/project/sdpython/pyenbc
    :alt: Build Status Windows

.. image:: https://circleci.com/gh/sdpython/pyenbc/tree/master.svg?style=svg
    :target: https://circleci.com/gh/sdpython/pyenbc/tree/master

.. image:: https://badge.fury.io/py/pyenbc.svg
    :target: http://badge.fury.io/py/pyenbc

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :alt: MIT License
    :target: http://opensource.org/licenses/MIT

.. image:: https://requires.io/github/sdpython/pyenbc/requirements.svg?branch=master
     :target: https://requires.io/github/sdpython/pyenbc/requirements/?branch=master
     :alt: Requirements Status

.. image:: https://codecov.io/github/sdpython/pyenbc/coverage.svg?branch=master
    :target: https://codecov.io/github/sdpython/pyenbc?branch=master

.. image:: http://img.shields.io/github/issues/sdpython/pyenbc.png
    :alt: GitHub Issues
    :target: https://github.com/sdpython/pyenbc/issues

.. image:: http://www.xavierdupre.fr/app/pyenbc/helpsphinx/_images/nbcov.png
    :target: http://www.xavierdupre.fr/app/pyenbc/helpsphinx/all_notebooks_coverage.html
    :alt: Notebook Coverage

.. _l-README:

pyenbc: helper to submit jobs from a notebeook
==============================================

This project contains helpers used at the `ENSAE <http://www.ensae.fr/>`_
for teachings available at
`ENSAE - Programmation - Xavier Dupré <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/index.html>`_.
It is not used anymore and probably not wworking anymore.
It implements a pythonic way to access a remote Linux machine
with a python *putty* and also:

* magic commands to access a Cloudera Cluster and run PIG jobs
* magic commands to access Azure Blob Storage and HDInsight
* magic commands to display content of a folder in DataFrame

Class *ASSHClient* requires:

* `paramiko <http://www.paramiko.org/>`_
* `pycrypto <https://pypi.python.org/pypi/pycrypto/>`_
* `ecdsa <https://pypi.python.org/pypi/ecdsa>`_

Class *AzureClient* requires:

* `azure <http://www.xavierdupre.fr/app/azure-sdk-for-python/helpsphinx/index.html>`_

The function *register_magics* defines magic commands
to send commands to a remote commands through a SSH connection:

* ``%remote_open``, ``%remote_close``
* ``%remote_cmd``, ``%remote_up``, ``%remote_down``

The magic commands will be automatically enabled if the module is imported from a notebook.

**Links:**

* `GitHub/pyenbc <https://github.com/sdpython/pyenbc/>`_
* `documentation <http://www.xavierdupre.fr/app/pyenbc/helpsphinx/index.html>`_
* `Blog <http://www.xavierdupre.fr/app/pyenbc/helpsphinx/blog/main_0000.html#ap-main-0>`_
