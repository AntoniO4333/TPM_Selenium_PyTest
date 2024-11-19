import pytest
from math_string_functions import *


# Фикстура для работы с текстовым файлом
@pytest.fixture
def sample_text():
    with open("text_sample.txt", "r", encoding="utf-8") as file:
        return file.read().strip()


# Класс тестов для математических функций
class TestMathFunctions:
    @pytest.mark.parametrize("a, b, result", [
        (3, 5, 15),
        (7, -2, -14),
        (0, 5, 0),
        (-3, -3, 9),
        (4, 0, 0),
    ])
    def test_multiply(self, a, b, result):
        assert multiply(a, b) == result

    @pytest.mark.parametrize("a, b, result", [
        (10, 2, 5),
        (-9, 3, -3),
        (7, -7, -1),
        (0, 5, 0),
        (100, 25, 4),
    ])
    def test_divide(self, a, b, result):
        if b == 0:
            with pytest.raises(ValueError):
                divide(a, b)
        else:
            assert divide(a, b) == result

    @pytest.mark.parametrize("x1, y1, x2, y2, result", [
        (0, 0, 3, 4, 5),
        (1, 1, 4, 5, 5),
        (0, 0, 0, 0, 0),
        (-1, -1, 2, 2, 4.2426406871),
        (3, 3, 3, 3, 0),
    ])
    def test_distance(self, x1, y1, x2, y2, result):
        assert distance(x1, y1, x2, y2) == pytest.approx(result)

    @pytest.mark.parametrize("a, b, c, result", [
        (1, -3, 2, (2, 1)),
        (1, 2, 1, (-1,)),
        (1, 0, -4, (2, -2)),
        (1, 0, 4, None),
        (2, 5, -3, (0.5, -3)),
    ])
    def test_quadratic_roots(self, a, b, c, result):
        assert quadratic_roots(a, b, c) == result

    @pytest.mark.parametrize("a, r, n, result", [
        (1, 2, 3, 7),
        (2, 1, 5, 10),
        (3, 0.5, 4, 5.625),
        (5, 2, 0, 0),
        (1, -1, 3, 1),
    ])
    def test_geometric_sum(self, a, r, n, result):
        assert geometric_sum(a, r, n) == pytest.approx(result)


# Класс тестов для работы со строками
class TestStringFunctions:
    @pytest.mark.parametrize("expected", [
        6  # Слова учитывая тире
    ])
    def test_count_words(self, sample_text, expected):
        assert count_words(sample_text) == expected

    @pytest.mark.parametrize("substring, expected", [
        ("пельмени", True),
        ("очень", True),
        ("вкусно", True),
        ("еда", False),
        ("Настоящие", True),
    ])
    def test_find_substring(self, sample_text, substring, expected):
        assert find_substring(sample_text, substring) == expected

    @pytest.mark.parametrize("expected", [
        "НАСТОЯЩИЕ ПЕЛЬМЕНИ - ЭТО ОЧЕНЬ ВКУСНО"
    ])
    def test_to_uppercase(self, sample_text, expected):
        assert to_uppercase(sample_text) == expected

