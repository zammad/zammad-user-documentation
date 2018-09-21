import sys
import os
import time

import sphinx_rtd_theme

html_logo = "images/zammad_logo_70x61.png"
html_favicon = "images/favicon.ico"
project = u'Zammad (for Agents)'
copyright = u'%s, The Zammad Foundation' % time.strftime("%Y")
author = u'The Zammad Foundation'

source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = ['_build', 'html', 'doctrees']

locale_dirs = ['locale/']
gettext_compact = False
language = "en"

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
