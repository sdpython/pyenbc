pyenbc documentation
=====================

.. image:: https://travis-ci.org/sdpython/pyenbc.svg?branch=master
    :target: https://travis-ci.org/sdpython/pyenbc
    :alt: Build status

.. image:: https://ci.appveyor.com/api/projects/status/scv9gmggw7qc462i?svg=true
    :target: https://ci.appveyor.com/project/sdpython/pyenbc
    :alt: Build Status Windows

.. image:: https://circleci.com/gh/sdpython/pyenbc/tree/master.svg?style=svg
    :target: https://circleci.com/gh/sdpython/pyenbc/tree/master

.. image:: https://badge.fury.io/py/pyenbc.svg
    :target: http://badge.fury.io/py/pyenbc

.. image:: http://img.shields.io/github/issues/sdpython/pyenbc.png
    :alt: GitHub Issues
    :target: https://github.com/sdpython/pyenbc/issues

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :alt: MIT License
    :target: http://opensource.org/licenses/MIT

.. image:: https://requires.io/github/sdpython/pyenbc/requirements.svg?branch=master
     :target: https://requires.io/github/sdpython/pyenbc/requirements/?branch=master
     :alt: Requirements Status

.. image:: https://codecov.io/github/sdpython/pyenbc/coverage.svg?branch=master
    :target: https://codecov.io/github/sdpython/pyenbc?branch=master

.. image:: https://badge.waffle.io/sdpython/pyenbc.png?label=to%20do&title=to%20do
    :alt: Waffle
    :target: https://waffle.io/sdpython/pyenbc

.. image:: nbcov.png
    :target: http://www.xavierdupre.fr/app/pyenbc/helpsphinx/all_notebooks_coverage.html
    :alt: Notebook Coverage

**Links:** `pypi <https://pypi.python.org/pypi/pyenbc/>`_,
`github <https://github.com/sdpython/pyenbc/>`_,
`documentation <http://www.xavierdupre.fr/app/pyenbc/helpsphinx/index.html>`_,
:ref:`l-README`,
:ref:`blog <ap-main-0>`,
:ref:`l-issues-todolist`

What is it?
-----------

This project contains helpers used at the `ENSAE <http://www.ensae.fr/>`_
for teaching purposes but not only.
It requires `github/pyquickhelper <https://github.com/sdpython/pyquickhelper/>`_,
and `github/pyensae <https://github.com/sdpython/pyensae/>`_.

Galleries and examples
----------------------

.. toctree::
    :maxdepth: 1

    api/index
    i_ex
    i_nb
    i_cmd
    i_faq
    gyexamples/index
    all_notebooks
    blog/blogindex
    HISTORY

Functionalities
---------------

* retrieve data for practical lessons (see :func:`download_data <pyenbc.datasource.http_retrieve.download_data>`)
* magic commands to access a Cloudera Cluster and run PIG jobs (see :class:`MagicRemoteSSH <pyenbc.remote.magic_remote_ssh.MagicRemoteSSH>`)
* magic commands to access Azure Blob Storage and HDInsight (see :class:`MagicAzure <pyenbc.remote.magic_azure.MagicAzure>`)
* magic commands to display content of a folder in DataFrame (see :class:`MagicFile <pyenbc.file_helper.magic_file.MagicFile>`)

Dependencies
------------

The :class:`ASSHClient <pyenbc.remote.ssh_remote_connection.ASSClient>` requires:

* `paramiko <http://www.paramiko.org/>`_
* `pycrypto <https://pypi.python.org/pypi/pycrypto/>`_
* `ecdsa <https://pypi.python.org/pypi/ecdsa>`_

The :class:`AzureClient <pyenbc.remote.azure_connection.AzureClient>` requires:

* `azure <http://www.xavierdupre.fr/app/azure-sdk-for-python/helpsphinx/index.html>`_

The function :func:`register_magics_ssh <pyenbc.remote.magic_remote_ssh.register_magics_ssh>` defines magic commands
to send commands to a remote commands through a SSH connection:

* ``%remote_open``, ``%remote_close``
* ``%remote_cmd``, ``%remote_up``, ``%remote_down``

Navigation
----------

.. toctree::
    :maxdepth: 1

    indexmenu

+------------------------+---------------------+---------------------+--------------------+------------------------+------------------------------------------------+
| :ref:`l-modules`       |  :ref:`l-functions` | :ref:`l-classes`    | :ref:`l-methods`   | :ref:`l-staticmethods` | :ref:`l-properties`                            |
+------------------------+---------------------+---------------------+--------------------+------------------------+------------------------------------------------+
| :ref:`modindex`        |  :ref:`l-EX2`       | :ref:`search`       | :ref:`l-license`   | :ref:`l-changes`       | :ref:`l-README`                                |
+------------------------+---------------------+---------------------+--------------------+------------------------+------------------------------------------------+
| :ref:`API <genindex>`  |  :ref:`l-FAQ2`      | :ref:`l-notebooks`  | :ref:`l-NB2`       | :ref:`l-statcode`      | `Unit Test Coverage <coverage/index.html>`_    |
+------------------------+---------------------+---------------------+--------------------+------------------------+------------------------------------------------+
