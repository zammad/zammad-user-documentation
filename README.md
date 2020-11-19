[![Documentation Status][badge]][docs]

# Zammad User Documentation

Source files for [Zammad’s user documentation][docs].

## Contributing

If you would like to improve the docs, simply:

1. fork the repo,
2. edit the appropriate `.rst` files (see [Markup Format](#markup-format) below), and
3. submit a pull request.

> 🌍 **Wanna help translate?** Submit your contributions
> (or request additional languages) [here][tfxtranslate].
> Do **NOT** submit a PR with changes to the contents of the `locale/` directory.

Thanks! ❤ ❤ ❤  
The Zammad Team

### Markup Format

These docs are written using the ReStructuredText markup format. Info about
this markup language can be found at:

- <http://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>
- <https://sphinx-rtd-theme.readthedocs.io/en/latest/demo/structure.html>

## Compilation

### Dependencies

* sphinx

  ```
  $ pip install sphinx sphinx-autobuild sphinx-intl sphinx_rtd_theme
  ```

* gettext

  ```
  $ brew install gettext              # macOS
  $ sudo apt install gettext          # Debian / Ubuntu
  $ sudo dnf install gettext          # Fedora
  ...
  ```

* transifex-client (optional)

  ```
  $ pip install transifex-client
  ```

### Local HTML build

```
$ make html
```

### Localization using transifex

```
# create .tx config
$ tx init

# ensure clean enviroment
$ make clean

# generate the strings from the *.rst files
$ make gettext

# OPTIONAL: if you have to adapt a new locale, run
sphinx-intl update -p _build/locale/ -l de

# update the resource files from the pot dir
$ sphinx-intl update-txconfig-resources --pot-dir _build/locale --transifex-project-name zammad-user-documentation

# push to transifex (if configured)
$ tx push -s

# Below pull options by default ignore unreviewed (see https://docs.transifex.com/client/pull#getting-different-file-variants )
# after translation pull needed languages from transifex
$ tx pull -l en

# build the .MO files for use with readthedocs
# (After a successful build, push to this repo and readthedocs will update itself.)
$ sh build_mo.sh

# manual language-based build (`_build/html/`) (for testing)
$ make -e SPHINXOPTS="-D language='de'" html
$ make -e SPHINXOPTS="-D language='en'" html
```

[badge]: https://readthedocs.org/projects/zammad-user-documentation/badge/?version=latest
[docs]: https://zammad-user-documentation.readthedocs.io/en/latest/
[tfxtranslate]: https://www.transifex.com/zammad/zammad-user-documentation/
