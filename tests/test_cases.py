import cases

TESTS = [
    ("", "", ""),
    ("Test", "test", "test"),
    ("test case", "test_case", "testCase"),
    (" test case", "test_case", "testCase"),
    ("test case ", "test_case", "testCase"),
    ("Test Case", "test_case", "testCase"),
    (" Test Case", "test_case", "testCase"),
    ("Test Case ", "test_case", "testCase"),
    ("camelCase", "camel_case", "camelCase"),
    ("PascalCase", "pascal_case", "pascalCase"),
    ("snake_case", "snake_case", "snakeCase"),
    (" Test Case", "test_case", "testCase"),
    ("SCREAMING_SNAKE_CASE", "screaming_snake_case", "screamingSnakeCase"),
    ("kebab-case", "kebab_case", "kebabCase"),
    ("SCREAMING-KEBAB-CASE", "screaming_kebab_case", "screamingKebabCase"),
    ("Title Case ", "title_case", "titleCase"),
    ("Train-Case ", "train_case", "trainCase"),
    ("This is a Test case.", "this_is_a_test_case", "thisIsATestCase"),
    (
        "MixedUP CamelCase, with some Spaces",
        "mixed_up_camel_case_with_some_spaces",
        "mixedUpCamelCaseWithSomeSpaces",
    ),
    (
        "mixed_up_ snake_case with some _spaces",
        "mixed_up_snake_case_with_some_spaces",
        "mixedUpSnakeCaseWithSomeSpaces",
    ),
    (
        "this-contains_ ALLKinds OfWord_Boundaries",
        "this_contains_all_kinds_of_word_boundaries",
        "thisContainsAllKindsOfWordBoundaries",
    ),
    ("XΣXΣ baﬄe", "xσxσ_baﬄe", "xσxσBaﬄe"),
    ("XMLHttpRequest", "xml_http_request", "xmlHttpRequest"),
    ("FIELD_NAME11", "field_name11", "fieldName11"),
    ("99BOTTLES", "99bottles", "99bottles"),
    ("FieldNamE11", "field_nam_e11", "fieldNamE11"),
    ("abc123def456", "abc123def456", "abc123def456"),
    ("abc123DEF456", "abc123_def456", "abc123Def456"),
    ("abc123Def456", "abc123_def456", "abc123Def456"),
    ("abc123DEf456", "abc123_d_ef456", "abc123DEf456"),
    ("ABC123def456", "abc123def456", "abc123def456"),
    ("ABC123DEF456", "abc123def456", "abc123def456"),
    ("ABC123Def456", "abc123_def456", "abc123Def456"),
    ("ABC123DEf456", "abc123d_ef456", "abc123dEf456"),
    ("ABC123dEEf456FOO", "abc123d_e_ef456_foo", "abc123dEEf456Foo"),
    ("abcDEF", "abc_def", "abcDef"),
    ("ABcDE", "a_bc_de", "aBcDe"),
]


def test_to_camel():
    for s, _, camel in TESTS:
        assert cases.to_camel(s) == camel


def test_to_camel_with_acronyms():
    assert (
        cases.to_camel("xml_http_request", acronyms={"xml": "XML"}) == "xmlHttpRequest"
    )
    assert (
        cases.to_camel("xml_http_request", acronyms={"http": "HTTP"})
        == "xmlHTTPRequest"
    )


def test_to_pascal():
    assert cases.to_pascal("test case") == "TestCase"


def test_to_pascal_with_acronyms():
    assert (
        cases.to_pascal("xml_http_request", acronyms={"xml": "XML"}) == "XMLHttpRequest"
    )
    assert (
        cases.to_pascal("xml_http_request", acronyms={"xml": "XML", "http": "HTTP"})
        == "XMLHTTPRequest"
    )
    assert (
        cases.to_pascal("xml_http_request", acronyms={"xml": "XML", "http": "Http"})
        == "XMLHttpRequest"
    )


def test_to_snake():
    for s, snake, _ in TESTS:
        assert cases.to_snake(s) == snake


def test_to_screaming_snake():
    assert cases.to_screaming_snake("test case") == "TEST_CASE"


def test_to_kebab():
    assert cases.to_kebab("test case") == "test-case"


def test_to_screaming_kebab():
    assert cases.to_screaming_kebab("test case") == "TEST-CASE"


def test_to_train():
    assert cases.to_train("test case") == "Test-Case"


def test_to_train_with_acronyms():
    assert (
        cases.to_train("xml_http_request", acronyms={"xml": "XML"})
        == "XML-Http-Request"
    )
    assert (
        cases.to_train("xml_http_request", acronyms={"xml": "XML", "http": "HTTP"})
        == "XML-HTTP-Request"
    )
    assert (
        cases.to_train("xml_http_request", acronyms={"xml": "XML", "http": "Http"})
        == "XML-Http-Request"
    )


def test_to_lower():
    assert cases.to_lower("Test-case") == "test case"


def test_to_title():
    assert cases.to_title("Test-case") == "Test Case"


def test_to_title_with_acronyms():
    assert (
        cases.to_title("xml_http_request", acronyms={"xml": "XML"})
        == "XML Http Request"
    )
    assert (
        cases.to_title("xml_http_request", acronyms={"xml": "XML", "http": "HTTP"})
        == "XML HTTP Request"
    )
    assert (
        cases.to_title("xml_http_request", acronyms={"xml": "XML", "http": "Http"})
        == "XML Http Request"
    )


def test_to_upper():
    assert cases.to_upper("test case") == "TEST CASE"
