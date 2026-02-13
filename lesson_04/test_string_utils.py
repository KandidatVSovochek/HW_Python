import pytest
from string_utilits import StringUtils


@pytest.mark.parametrize('input, expected', [('hello', 'Hello'),
                                             ('hello world', 'Hello world'),
                                             ('12345', '12345'),
                                             ('Hello', 'Hello')])
def test_capitalize(input, expected):
    text = StringUtils()
    res = text.capitalize(input)
    assert res == expected


@pytest.mark.parametrize('input, expected', [('     hello', 'hello'),
                                             ('    ', ''),
                                             ('Hello', 'Hello')])
def test_trim(input, expected):
    text = StringUtils()
    res = text.trim(input)
    assert res == expected


@pytest.mark.parametrize('input, symbol, expected',
                         [('Less', 'L', True),
                          ('Less', 'D', False)])
def test_contains(input, symbol, expected):
    text = StringUtils()
    res = text.contains(input, symbol)
    assert res == expected


@pytest.mark.parametrize('input, symbol, expected',
                         [('Less', 'L', 'ess'),
                          ('HopeLess', 'Less', 'Hope'),
                          ('I love you', 'bad', 'I love you'),
                          ('coco nut', ' ', 'coconut')])
def test_delete_symbol(input, symbol, expected):
    text = StringUtils()
    res = text.delete_symbol(input, symbol)
    assert res == expected
