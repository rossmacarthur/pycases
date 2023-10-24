# pycases

[![PyPI version](https://badgers.space/pypi/version/pycases)](https://pypi.org/project/pycases)
[![License](https://badgers.space/github/license/rossmacarthur/pycases)](https://github.com/rossmacarthur/pycases#license)
[![Build Status](https://badgers.space/github/checks/rossmacarthur/pycases/trunk?label=build)](https://github.com/rossmacarthur/pycases/actions/workflows/build.yaml)

A case conversion library for Python with Unicode support.

The currently supported cases are:

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

## Details

Each of the provided functions using the same underlying implementation which
does the following:
- Divide the input string into words
- Convert each word as required
- Join the words back together optionally with a separator

Word boundaries are defined as follows:

- A set of consecutive Unicode non-letter and non-number characters.

  For example: 'foo _bar' is two words (foo and bar)

- A transition from a lowercase letter to an uppercase letter.

  For example: fooBar is two words (foo and Bar)

- A transition from multiple uppercase letters to a single uppercase letter
  followed by lowercase letters.

  For example: FOOBar is two words (FOO and Bar)

Functions where the transform is "title" accept an optional `acronyms` argument,
which is a mapping of lowercase words to their output. For example:

```python
>>> cases.to_pascal("xml_http_request", acronyms={"xml": "XML"})
'XMLHttpRequest'
>>> cases.to_pascal("xml_http_request", acronyms={"xml": "XML", "http": "HTTP"})
'XMLHTTPRequest'
```

## License

This project is licensed under the terms of the MIT license. See
[LICENSE](LICENSE) for more details.
