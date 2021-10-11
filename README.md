[![Documentation Status][badge]][docs] [![Translation Status][tbadge]][wbetranslate]

# Zammad User Documentation

Source files for [Zammad’s user documentation][docs].

## Contributing

If you would like to improve the docs, simply:

1. fork the repo,
2. edit the appropriate `.rst` files (see [Markup Format](#markup-format) below),
   and
3. submit a pull request.

> 🌍 **Wanna help translate?** Submit your contributions
> (or request additional languages) [here][wbetranslate].
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
  $ pip install sphinx sphinx-autobuild sphinx-intl sphinx_rtd_theme sphinx-tabs
  ```

* gettext

  ```
  $ brew install gettext              # macOS
  $ sudo apt install gettext          # Debian / Ubuntu
  $ sudo dnf install gettext          # Fedora
  ...
  ```

### Local HTML build

```
$ make html
```

### Localization using Weblate

This documentation is translated via Weblate.
After changing or adding text in this documentation, updating the POT file
is required. (This is usually done by us after QA *before* merging the PR)

Weblate will automatically provide the translation parts in in its UI for
all available languages. If there's translation progress it will automatically
provide pull requests on this repository. 🎉

```
# ensure clean enviroment
$ make clean

# generate the strings from the *.rst files
$ make gettext

# manual language-based build (`_build/html/`) (for testing)
$ make -e SPHINXOPTS="-D language='de'" html
$ make -e SPHINXOPTS="-D language='en'" html
```

### Localization process

[![Translation progress][tprogress]][wbetranslate]

[badge]: https://readthedocs.org/projects/zammad-user-documentation/badge/?version=latest
[docs]: https://user-docs.zammad.org/en/latest/
[tbadge]: https://translations.zammad.org/widgets/documentations/-/user-documentation/svg-badge.svg
[wbetranslate]: https://translations.zammad.org/projects/documentations/user-documentation/
[tprogress]: https://translations.zammad.org/widgets/documentations/-/user-documentation/multi-auto.svg
