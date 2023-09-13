mod transform;

use std::fmt;

use pyo3::prelude::*;

use crate::transform::{fmt_lower, fmt_title, fmt_upper, transform};

/// Convert a string to 'camelCase'.
#[pyfunction]
fn to_camel(s: &str) -> String {
    let mut buf = String::with_capacity(s.len());

    let mut first = true;
    let word_fn = |buf: &mut String, s: &str| -> fmt::Result {
        if first {
            first = false;
            fmt_lower(buf, s)
        } else {
            fmt_title(buf, s)
        }
    };

    transform(s, &mut buf, word_fn, "").unwrap();
    buf
}

/// Convert a string to 'PascalCase'.
#[pyfunction]
fn to_pascal(s: &str) -> String {
    let mut buf = String::with_capacity(s.len());
    transform(s, &mut buf, fmt_title, "").unwrap();
    buf
}

/// Convert a string to 'snake_case'.
#[pyfunction]
fn to_snake(s: &str) -> String {
    let mut buf = String::with_capacity(s.len());
    transform(s, &mut buf, fmt_lower, "_").unwrap();
    buf
}

/// Convert a string to 'SCREAMING_SNAKE_CASE'.
#[pyfunction]
fn to_screaming_snake(s: &str) -> String {
    let mut buf = String::with_capacity(s.len());
    transform(s, &mut buf, fmt_upper, "_").unwrap();
    buf
}

/// Convert a string to 'kebab-case'.
#[pyfunction]
fn to_kebab(s: &str) -> String {
    let mut buf = String::with_capacity(s.len());
    transform(s, &mut buf, fmt_lower, "-").unwrap();
    buf
}

/// Convert a string to 'SCREAMING-KEBAB-CASE'.
#[pyfunction]
fn to_screaming_kebab(s: &str) -> String {
    let mut buf = String::with_capacity(s.len());
    transform(s, &mut buf, fmt_upper, "-").unwrap();
    buf
}

/// Convert a string to 'Train-Case'.
#[pyfunction]
fn to_train(s: &str) -> String {
    let mut buf = String::with_capacity(s.len());
    transform(s, &mut buf, fmt_title, "-").unwrap();
    buf
}

/// Convert a string to 'lower case'.
#[pyfunction]
fn to_lower(s: &str) -> String {
    let mut buf = String::with_capacity(s.len());
    transform(s, &mut buf, fmt_lower, " ").unwrap();
    buf
}

/// Convert a string to 'Title Case'.
#[pyfunction]
fn to_title(s: &str) -> String {
    let mut buf = String::with_capacity(s.len());
    transform(s, &mut buf, fmt_title, " ").unwrap();
    buf
}

/// Convert a string to 'UPPER CASE'.
#[pyfunction]
fn to_upper(s: &str) -> String {
    let mut buf = String::with_capacity(s.len());
    transform(s, &mut buf, fmt_upper, " ").unwrap();
    buf
}

/// A case conversion library with Unicode support, implemented in Rust.
#[pymodule]
fn cases(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(to_camel, m)?)?;
    m.add_function(wrap_pyfunction!(to_pascal, m)?)?;
    m.add_function(wrap_pyfunction!(to_snake, m)?)?;
    m.add_function(wrap_pyfunction!(to_screaming_snake, m)?)?;
    m.add_function(wrap_pyfunction!(to_kebab, m)?)?;
    m.add_function(wrap_pyfunction!(to_screaming_kebab, m)?)?;
    m.add_function(wrap_pyfunction!(to_train, m)?)?;
    m.add_function(wrap_pyfunction!(to_lower, m)?)?;
    m.add_function(wrap_pyfunction!(to_title, m)?)?;
    m.add_function(wrap_pyfunction!(to_upper, m)?)?;
    Ok(())
}
