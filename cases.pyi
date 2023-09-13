"""
A case conversion library with Unicode support, implemented in Rust.

Word boundaries are defined as follows:

- A set of consecutive Unicode non-letter/number
  e.g. 'foo _bar' is two words (foo and bar)

- A transition from a lowercase letter to an uppercase letter
  e.g. fooBar is two words (foo and Bar)

  - The second last uppercase letter in a word with multiple uppercase letters
  e.g. FOOBar is two words (FOO and Bar)

Some functions accept an optional `acronyms` argument, which is a mapping of
lowercase words to their output. For example:

    >>> cases.to_pascal("xml_http_request", acronyms={"xml": "XML"})
    'XMLHttpRequest'
    >>> cases.to_pascal("xml_http_request", acronyms={"xml": "XML", "http": "HTTP"})
    'XMLHTTPRequest'

"""

from typing import Optional

def to_camel(s: str, acronyms: Optional[dict[str, str]] = None) -> str:
    """
    Convert a string to 'camelCase'.
    """
    ...

def to_pascal(s: str, acronyms: Optional[dict[str, str]] = None) -> str:
    """
    Convert a string to 'PascalCase'.
    """
    ...

def to_snake(s: str) -> str:
    """
    Convert a string to 'camelCase'.
    """
    ...

def to_screaming_snake(s: str) -> str:
    """
    Convert a string to 'SCREAMING_SNAKE_CASE'.
    """
    ...

def to_kebab(s: str) -> str:
    """
    Convert a string to 'kebab-case'.
    """
    ...

def to_screaming_kebab(s: str) -> str:
    """
    Convert a string to 'SCREAMING-KEBAB-CASE'.
    """
    ...

def to_train(s: str, acronyms: Optional[dict[str, str]] = None) -> str:
    """
    Convert a string to 'Train-Case'.
    """
    ...

def to_lower(s: str) -> str:
    """
    Convert a string to 'lower case'.
    """
    ...

def to_title(s: str, acronyms: Optional[dict[str, str]] = None) -> str:
    """
    Convert a string to 'Title Case'.
    """
    ...

def to_upper(s: str) -> str:
    """
    Convert a string to 'UPPER CASE'.
    """
    ...
