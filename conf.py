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
extensions = ['versionwarning.extension', 'sphinx_tabs.tabs']

locale_dirs = ['locale/']
gettext_compact = "user-docs"
language = "en"

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ['_static']

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if not on_rtd:  # only import and set the theme if we're building docs locally
   # Override default css to solve issues (e.g. width, overflows)
   import sphinx_rtd_theme
   html_theme = 'sphinx_rtd_theme'
   html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
   def setup(app):
      app.add_css_file('theme/theme_overrides.css')

   # We're running outside of readthedocs and expect the compiled version to 
   # be a pre release
   branch = 'pre-release'

else:
   # Override default css to solve issues (e.g. width, overflows)
   # html context breaks sphinx tabs ~
   # html_context = {
   #    'css_files': [
   #       'https://media.readthedocs.org/css/sphinx_rtd_theme.css',
   #       'https://media.readthedocs.org/css/readthedocs-doc-embed.css',
   #       '_static/theme/theme_overrides.css',
   #       '_static/theme/tabs.css'
   #    ],
   # }

   html_css_files = [
     'https://media.readthedocs.org/css/sphinx_rtd_theme.css',
     'https://media.readthedocs.org/css/readthedocs-doc-embed.css',
     'theme/theme_overrides.css'
   ]

   # Get current version we're on for possible version warning
   version = os.environ.get('READTHEDOCS_VERSION')

   # If we're **not on latest**, we'll display a deprecation warning.
   if version == 'latest':
      branch = version
   elif version == 'pre-release':
      branch = "pre-release"
   else:
      branch = "old-version"

# Default definitions for this documentations version warnings if applicable
# https://sphinx-version-warning.readthedocs.io/en/latest/configuration.html
versionwarning_project_slug = "zammad-admin-documentation"
versionwarning_admonition_type = "warning"
versionwarning_project_version = branch
versionwarning_body_selector = "div.document"

versionwarning_messages = {
   "pre-release": (
      "You're viewing a <strong>pre-release</strong> version of this "
      "documentation! If you want to see the stable, current version of "
      "this documentation, please see "
      '<a href="https://user-docs.zammad.org/en/latest/" '
      'title="current documentation version">here</a>.'
   ),
   "old-version": (
      "You're viewing a <strong>deprecated</strong> version of Zammad's "
      "documentation. If you're still running that version, please consider "
      '<a href="https://docs.zammad.org/en/latest/install/update.html" '
      'title="Updating Zammad">Updating Zammad</a> asap.'
      "If you're a hosted user, please contact support."
   ),
}
