# Zammad user documentation

If you want to contribute to the Zammad documentation you can edit the rst files and create pull requests.

We take care about the translation part, so please don't change anything else whithin the repository. These changes would be discarded anyway ;)

Note:
At the moment we only have a german version. We are working on an english version and will change the default later.

## Documentation

Zammad hosts a searchable version of this documentation at https://docs.zammad.org

## ReStructuredText markup

If you like to edit the docs use the ReStructuredText markup language. Info about this markup language can be found at:

- http://www.sphinx-doc.org/en/stable/rest.html
- http://docs.readthedocs.io/en/latest/_themes/sphinx_rtd_theme/demo_docs/source/demo.html

Thanks! ❤ ❤ ❤

  Zammad Team


[![Documentation Status](https://readthedocs.org/projects/zammad-user-documentation/badge/?version=latest)](https://docs.zammad.org)

## Local tests (mostly internal stuff)

If you want to test the docs for yourself you need a local installation of sphinx and gettext.

```
pip install sphinx sphinx-autobuild sphinx-intl sphinx_rtd_theme

```

### Example for a local HTML build

```
make html
```

### Example workflow for localization using transifex

If you have to work on the translations you need gettext.

For OS X use HomeBrew or build from source. For Linux use your package manager.

```
brew install gettext
```

The workflow itself
```
# create .tx config
tx init
# or if you just want to update a ressource
tx set --source -r <project_slug.resource_slug> -l <lang> <file>

make clean

# this will generate the strings from the *.rst files
make gettext

# this will generate the locales (DE|EN)
sphinx-intl update -p _build/locale/ -l de -l en

# this will update the resource files from the pot dir
sphinx-intl update-txconfig-resources --pot-dir _build/locale --transifex-project-name zammad-user-documentation

# push to transifex (if configured)
tx push -s

# after translation pull needed languages from transifex
tx pull -l en

# manual language-based build (_build/html/)
make -e SPHINXOPTS="-D language='de'" html
make -e SPHINXOPTS="-D language='en'" html

```
