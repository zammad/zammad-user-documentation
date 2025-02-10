[![Documentation Status][badge_pre-release]][docs_pre-release] [![Translation Status][tbadge_pre-release]][wbetranslate_pre-release] (pre-release)

[![Documentation Status][badge_latest]][docs_latest] [![Translation Status][tbadge_latest]][wbetranslate_latest] (latest)

# Zammad User Documentation

Source files for Zammad’s user documentation ([latest][docs_latest] / [pre-release][docs_pre-release]).

## Contributing

Please see [the Contributing section in this manual](https://docs.zammad.org/en/latest/contributing/start.html).

## Compilation

### Dependencies

* sphinx

  ```
  $ pip install sphinx sphinx-autobuild sphinx-intl sphinx_rtd_theme sphinx-tabs sphinx-version-warning
  ```

* gettext

  ```
  $ brew install gettext              # macOS
  $ sudo apt install gettext          # Debian / Ubuntu
  $ sudo dnf install gettext          # Fedora
  ```

### Example for a local HTML build

```
make html
```
Building for a specific language:

```
$ make -e SPHINXOPTS="-D language='en'" html
```

### Localization progress

[![Translation progress][tprogress]][wbetranslate_pre-release]

[badge_latest]: https://readthedocs.org/projects/zammad-user-documentation/badge/?version=latest
[docs_latest]: https://user-docs.zammad.org/en/latest/

[badge_pre-release]: https://readthedocs.org/projects/zammad-user-documentation/badge/?version=pre-release
[docs_pre-release]: https://user-docs.zammad.org/en/pre-release/

[tbadge_latest]: https://translations.zammad.org/widget/documentations/user-documentation-latest/svg-badge.svg
[wbetranslate_latest]: https://translations.zammad.org/projects/documentations/user-documentation-latest/

[tbadge_pre-release]: https://translations.zammad.org/widget/documentations/user-documentation-pre-release/svg-badge.svg
[wbetranslate_pre-release]: https://translations.zammad.org/projects/documentations/user-documentation-pre-release/

[tprogress]: https://translations.zammad.org/widget/documentations/user-documentation-pre-release/multi-auto.svg
