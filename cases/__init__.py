import warnings

from anycase import (
    to_camel,
    to_pascal,
    to_snake,
    to_screaming_snake,
    to_kebab,
    to_screaming_kebab,
    to_train,
    to_lower,
    to_title,
    to_upper,
)

__all__ = [
    "to_camel",
    "to_pascal",
    "to_snake",
    "to_screaming_snake",
    "to_kebab",
    "to_screaming_kebab",
    "to_train",
    "to_lower",
    "to_title",
    "to_upper",
]

warnings.warn(
    """This package has been renamed and it is now published as py-anycase,

Please see https://github.com/rossmacarthur/anycase/tree/trunk/python.

You can install it with:
```sh
pip install py-anycase
```

The new usage is:

>>> import anycase
>>> anycase.to_snake('Hello World')
'hello_world'
""",
    DeprecationWarning,
)
