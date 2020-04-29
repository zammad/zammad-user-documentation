[![Documentation Status][badge]][docs]

# Zammad User Documentation

Source files for [Zammad’s user documentation][docs].

## Contributing

If you would like to improve the docs, simply:

1. fork the repo,
2. edit the appropriate `.rst` files (see [Markup Format](#markup-format) below), and
3. submit a pull request.

> **🌍 Note on localization:** Translations are prepared and stored on
> [Transifex][tfx], a third-party cloud platform. Do **NOT** manually edit the
> `.po` and `.mo` localization files, as any such changes will be overwritten
> in the compilation process.
> 
> If you want to help on translation, you can find the [find the Transifex project here][tfxtranslate]. 
> You can also request to translate new languages. 💪

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

# or if you just want to update a resource
$ tx set --source -r <project_slug.resource_slug> -l <lang> <file>
$ make clean

# generate the strings from the *.rst files
$ make gettext

# generate the locales (DE|EN)
$ sphinx-intl update -p _build/locale/ -l de -l en

# update the resource files from the pot dir
$ sphinx-intl update-txconfig-resources --pot-dir _build/locale --transifex-project-name zammad-user-documentation

# push to transifex (if configured)
$ tx push -s

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
[tfx]: https://www.transifex.com/
[tfxtranslate]: https://www.transifex.com/zammad/zammad-user-documentation/
