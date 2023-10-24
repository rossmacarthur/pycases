import re
import cases
import inflection
import case_conversion
import stringcase
from pytest_benchmark.fixture import BenchmarkFixture


LEN = 100
INPUT = "thisIsACamelCaseString" * LEN
EXPECT = "this_is_a_camel_case_string" * LEN


def test_bench_to_snake_pure_python(benchmark: BenchmarkFixture):
    def camel_to_snake(s):
        return "".join(["_" + c.lower() if c.isupper() else c for c in s]).lstrip("_")

    assert benchmark(camel_to_snake, INPUT) == EXPECT


def test_bench_to_snake_regex(benchmark: BenchmarkFixture):
    pattern = re.compile(r"(?<!^)(?=[A-Z])")

    def camel_to_snake(s):
        return pattern.sub("_", s).lower()

    assert benchmark(camel_to_snake, INPUT) == EXPECT

def test_bench_to_snake_cases(benchmark: BenchmarkFixture):
    assert benchmark(cases.to_snake, INPUT) == EXPECT


def test_bench_to_snake_caseconversion(benchmark: BenchmarkFixture):
    assert benchmark(case_conversion.snakecase, INPUT) == EXPECT


def test_bench_to_snake_inflection(benchmark: BenchmarkFixture):
    assert benchmark(inflection.underscore, INPUT) == EXPECT


def test_bench_to_snake_stringcase(benchmark: BenchmarkFixture):
    assert benchmark(stringcase.snakecase, INPUT) == EXPECT
