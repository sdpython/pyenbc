# -*- coding: utf-8 -*-
import sys
import os
import sphinxjp.themes.basicstrap
from pyquickhelper.helpgen.default_conf import set_sphinx_variables

sys.path.insert(0, os.path.abspath(os.path.join(os.path.split(__file__)[0])))

set_sphinx_variables(__file__, "pyenbc", "Xavier Dupré", 2018,
                     "basicstrap", None, locals(), add_extensions=None,
                     extlinks=dict(issue=('https://github.com/sdpython/pyenbc/issues/%s', 'issue')))

blog_root = "http://www.xavierdupre.fr/app/pyenbc/helpsphinx/"
blog_background = False
exclude_patterns += ["pyensae/file_helper/pigjar/*",
                     "pyensae/file_helper/hadoopjar/*"]

nblinks = {"code-r2python": blog_root + "pyensae/languages/rconverter.html"}

epkg_dictionary["blockdiag"] = 'http://blockdiag.com/'
epkg_dictionary["pyensae"] = 'http://www.xavierdupre.fr/app/pyensae/helpsphinx/index.html'
