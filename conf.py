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

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ['_static']

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if not on_rtd:  # only import and set the theme if we're building docs locally
    # Override default css to solve issues (e.g. width, overflows)
    def setup(app):
        app.add_css_file('theme/theme_overrides.css')
else:
    # Override default css to solve issues (e.g. width, overflows)
    html_context = {
        'css_files': [
            'https://media.readthedocs.org/css/sphinx_rtd_theme.css',
            'https://media.readthedocs.org/css/readthedocs-doc-embed.css',
            '_static/theme/theme_overrides.css'
        ],
    }
