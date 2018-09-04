# -*- coding: utf8 -*-
import pytz
from datetime import datetime

__all__ = []


class TZDate(object):
    @staticmethod
    def get(time, f=None, tz=None):
        format_ = f or '%a, %d %b %Y %H:%M:%S'
        timezone = tz or 'Europe/Moscow'
        if not isinstance(format_, str):
            raise TypeError()
        if not isinstance(time, (float, int)):
            raise TypeError()
        if not isinstance(timezone, str):
            raise TypeError()
        d = datetime.fromtimestamp(time)
        d = d.astimezone(pytz.timezone(tz))
        return d.strftime(format_)
