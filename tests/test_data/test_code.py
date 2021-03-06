# -*- coding: utf-8 -*-
import re

import pytest

from mimesis.data import LOCALE_CODES

from . import _patterns as p


def test_str(code):
    assert re.match(p.STR_REGEX, str(code))


def test_custom_code(code):
    result = code.custom_code(
        mask='@###', char='@', digit='#')

    assert len(result) == 4


def test_custom_code_args(code):
    result = code.custom_code(
        mask='@@@-###-@@@').split('-')

    a, b, c = result
    assert a.isalpha()
    assert b.isdigit()
    assert c.isalpha()


@pytest.mark.parametrize(
    'fmt, length', [
        ('ean-8', 8),
        ('ean-13', 13),
    ],
)
def test_ean(code, fmt, length):
    result = code.ean(fmt=fmt)
    assert len(result) == length


def test_imei(code):
    result = code.imei()
    assert len(result) <= 15


def test_pin(code):
    result = code.pin()
    assert len(result) == 4


def test_issn(code):
    result = code.issn()
    assert len(result) == 9


def test_locale_code(code):
    result = code.locale_code()
    assert result in LOCALE_CODES


@pytest.mark.parametrize(
    'fmt, length', [
        ('isbn-10', 10),
        ('isbn-13', 13),
    ],
)
def test_isbn(generic, fmt, length):
    result = generic.code.isbn(fmt=fmt)
    assert result is not None
    assert len(result) >= length
