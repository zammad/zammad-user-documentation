import sys
import os
import time

import sphinx_rtd_theme
import time

html_logo = "images/zammad_logo_70x61.png"
html_favicon = "images/favicon.ico"
project = u'Zammad'
copyright = u'%s, Zammad' % time.strftime("%Y")
author = u'Zammad'

source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = ['_build', 'html', 'doctrees']

locale_dirs = ['locale/']
gettext_compact = False
language = "en"

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
