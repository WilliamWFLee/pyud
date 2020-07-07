.. currentmodule:: pyud

Changelog
=========

This page shows a complete summary of changes and fixes made in each version.

v1.0.1
------

Enhancements
~~~~~~~~~~~~

- Support for Python >= 3.5.3 added.
- :meth:`Definition` raises more helpful :exc:`ValueError` for incorrect date format.
- Fix :paramref:`Client.random.limit` and :paramref:`AsyncClient.random.limit` parameters so that values greater than 10 are properly considered. Previously, for values higher than 10, only 10 definitions were returned.
- Add :data:`version_info`, adding it alongside :data:`__version__` (previously undocumented).

Bug Fixes
~~~~~~~~~

- Fix bug that prevented multiple-word terms from being defined.
