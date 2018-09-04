# -*- coding: utf8 -*-
import pytz
from datetime import datetime

__all__ = ['convert']


def convert(time, f=None, tz=None):
    """
    Converts the UTC time, the date and time of the region.

    Library for converting time from UTC to date,
    depending on the specified "region/city".
    You can use standard date and time templates.

    :param time: the time in UTC format
    :param f: date and time template (standard datetime class),
              example '%a, %d %b %Y %H:%M:%S'
    :param tz: time zone in the format "region/city",
               example "Europe/Moscow"
    :return: str in format '%a, %d %b %Y %H:%M:%S' or your format
    """
    format_ = f or '%a, %d %b %Y %H:%M:%S'
    if not isinstance(format_, str):
        raise TypeError('f must str.')
    if not isinstance(time, (float, int)):
        raise TypeError('time must float or int.')
    if not isinstance(tz, str):
        raise TypeError('tz must str.')
    d = datetime.fromtimestamp(time)
    d = d.astimezone(pytz.timezone(tz))
    return d.strftime(format_)
