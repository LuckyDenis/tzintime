# -*- coding: utf8 -*-

import pytest

from time import time

from intimezone import convert, Error
from tests.timezone_list import all_timezones


def test_convert_flag_none():
    for tz in all_timezones:
        assert isinstance(convert(time(), tz=tz), str)


def test_convert_flag_convert():
    for tz in all_timezones:
        assert isinstance(convert(time(), tz=tz, flag="convert"), str)


def test_convert_flag_localize():
    for tz in all_timezones:
        assert isinstance(convert(time(), tz=tz, flag="localize"), str)


def test_convert_template_flag_none():
    for tz in all_timezones:
        assert isinstance(convert(time(), tz=tz, f='%H:%M:%S'), str)


def test_convert_template_flag_convert():
    for tz in all_timezones:
        assert isinstance(convert(time(), tz=tz, f='%H:%M:%S', flag="convert"), str)


def test_convert_template_flag_localize():
    for tz in all_timezones:
        assert isinstance(convert(time(), tz=tz, f='%H:%M:%S', flag="localize"), str)


def test_answer_not_template():
    dt = convert(946684800, tz='Europe/London')
    assert dt == 'Sat, 01 Jan 2000 00:00:00'
    dt = convert(946684800, tz='Europe/Madrid', flag="convert")
    assert dt == 'Sat, 01 Jan 2000 01:00:00'
    dt = convert(946684800, tz='Europe/Moscow', flag="localize")
    assert dt == 'Sat, 01 Jan 2000 00:00:00 +0300(MSK)'


def test_answer_yes_template():
    dt = convert(946684800, tz='Europe/London', f="%H:%M:%S")
    assert dt == '00:00:00'
    dt = convert(946684800, tz='Europe/Madrid', flag="convert", f="%H:%M:%S")
    assert dt == '01:00:00'
    dt = convert(946684800, tz='Europe/Moscow', flag="localize", f="%H:%M:%S")
    assert dt == '00:00:00'


def test_error_moment_time():
    with pytest.raises(Error.ErrorFormatTime):
        convert('qwer', tz='Europe/London', f="%H:%M:%S")
    with pytest.raises(Error.ErrorFormatTime):
        convert('qwer', tz='Europe/Madrid', flag="convert", f="%H:%M:%S")
    with pytest.raises(Error.ErrorFormatTime):
        convert('qwer', tz='Europe/Moscow', flag="localize", f="%H:%M:%S")


def test_error_timezone():
    with pytest.raises(Error.ErrorFormatTimeZone):
        convert(946684800, tz=123, f="%H:%M:%S")
    with pytest.raises(Error.ErrorFormatTimeZone):
        convert(946684800, tz=123, flag="convert", f="%H:%M:%S")
    with pytest.raises(Error.ErrorFormatTimeZone):
        convert(946684800, tz=123, flag="localize", f="%H:%M:%S")


def test_error_template():
    with pytest.raises(Error.ErrorFormatTemplate):
        convert(946684800, tz='Europe/London', f=123)
    with pytest.raises(Error.ErrorFormatTemplate):
        convert(946684800, tz='Europe/Madrid', flag="convert", f=123)
    with pytest.raises(Error.ErrorFormatTemplate):
        convert(946684800, tz='Europe/Moscow', flag="localize", f=123)


def test_error_flag():
    with pytest.raises(Error.ErrorFlag):
        convert(946684800, tz='Europe/London', flag="123")
    with pytest.raises(Error.ErrorFlag):
        convert(946684800, tz='Europe/Madrid', flag=123)
    with pytest.raises(Error.ErrorFlag):
        convert(946684800, tz='Europe/Moscow', flag=str)
