import re
import cases
import inflection
import stringcase
from pytest_benchmark.fixture import BenchmarkFixture


LEN = 100


def test_bench_to_snake_pure_python(benchmark: BenchmarkFixture):
    def camel_to_snake(s):
        return "".join(["_" + c.lower() if c.isupper() else c for c in s]).lstrip("_")

    s = "thisIsACamelCaseString" * LEN
    result = benchmark(camel_to_snake, s)
    assert result == "this_is_a_camel_case_string" * LEN


def test_bench_to_snake_regex(benchmark: BenchmarkFixture):
    s = "thisIsACamelCaseString" * LEN
    pattern = re.compile(r"(?<!^)(?=[A-Z])")
    result = benchmark(pattern.sub, "_", s).lower()
    assert result == "this_is_a_camel_case_string" * LEN


def test_bench_to_snake_cases(benchmark: BenchmarkFixture):
    s = "thisIsACamelCaseString" * LEN
    result = benchmark(cases.to_snake, s)
    assert result == "this_is_a_camel_case_string" * LEN


def test_bench_to_snake_inflection(benchmark: BenchmarkFixture):
    s = "thisIsACamelCaseString" * LEN
    result = benchmark(inflection.underscore, s)
    assert result == "this_is_a_camel_case_string" * LEN


def test_bench_to_snake_stringcase(benchmark: BenchmarkFixture):
    s = "thisIsACamelCaseString" * LEN
    result = benchmark(stringcase.snakecase, s)
    assert result == "this_is_a_camel_case_string" * LEN
