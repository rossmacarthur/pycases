# Deprecated

- This repository was merged into [anycase](https://github.com/rossmacarthur/anycase), and is now published as [`py-anycase`] on PyPI
- This package now simply re-exports the [`py-anycase`] package.

[`py-anycase`]: https://github.com/rossmacarthur/anycase/tree/trunk/python

# pycases

[![PyPI version](https://badgers.space/pypi/version/pycases)](https://pypi.org/project/pycases)
[![License](https://badgers.space/github/license/rossmacarthur/pycases)](https://github.com/rossmacarthur/pycases#license)
[![Build Status](https://badgers.space/github/checks/rossmacarthur/pycases/trunk?label=build)](https://github.com/rossmacarthur/pycases/actions/workflows/build.yaml)

A case conversion library for Python.

## Features

- Automatic case detection, no need to specify the input case
- Extremely fast, written in Rust ✨
- Support for Unicode characters
- Support for providing acronyms in title case

**Supported cases**

| Function                      | Output                 |
| :---------------------------- | :--------------------- |
| `cases.to_camel(s)`           | `camelCase`            |
| `cases.to_pascal(s)`          | `PascalCase`           |
| `cases.to_snake(s)`           | `snake_case`           |
| `cases.to_screaming_snake(s)` | `SCREAMING_SNAKE_CASE` |
| `cases.to_kebab(s)`           | `kebab-case`           |
| `cases.to_screaming_kebab(s)` | `SCREAMING-KEBAB-CASE` |
| `cases.to_train(s)`           | `Train-Case`           |
| `cases.to_lower(s)`           | `lower case`           |
| `cases.to_title(s)`           | `Title Case`           |
| `cases.to_upper(s)`           | `UPPER CASE`           |

## Getting started

Install using

```sh
pip install pycases
```

Now convert a string using the relevant function.

```python
import cases

cases.to_snake("XMLHttpRequest") # returns "xml_http_request"
```

## License

This project is licensed under the terms of the MIT license. See
[LICENSE](LICENSE) for more details.
