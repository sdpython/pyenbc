# -*- coding: utf-8 -*-
import sys
import os
import alabaster
from pyquickhelper.helpgen.default_conf import set_sphinx_variables, get_default_stylesheet

sys.path.insert(0, os.path.abspath(os.path.join(os.path.split(__file__)[0])))

set_sphinx_variables(__file__, "pyenbc", "Xavier Dupré", 2020,
                     "alabaster", alabaster.get_path(),
                     locals(), add_extensions=None,
                     extlinks=dict(issue=('https://github.com/sdpython/pyenbc/issues/%s', 'issue')))

blog_root = "http://www.xavierdupre.fr/app/pyenbc/helpsphinx/"
blog_background = False
exclude_patterns += ["pyenbc/filehelper/pigjar/*",
                     "pyenbc/filehelper/hadoopjar/*"]

nblinks = {"code-r2python": blog_root + "pyensae/languages/rconverter.html"}

html_context = {
    'css_files': get_default_stylesheet() + ['_static/my-styles.css'],
}

epkg_dictionary["blockdiag"] = 'http://blockdiag.com/'
epkg_dictionary["pyensae"] = 'http://www.xavierdupre.fr/app/pyensae/helpsphinx/index.html'
