intimezone
==========

.. image:: https://img.shields.io/badge/python-2%20%7C%203-ffc30f.svg
    :target: https://github.com/LuckyDenis/tzintime/

.. image:: https://img.shields.io/badge/license-MIT-ffc30f.svg
    :target: https://github.com/LuckyDenis/tzintime/blob/v1.0.0/LICENSE

.. image:: https://img.shields.io/badge/platform-win32/64%20%7C%20linux32/64-ffc30f.svg
    :target: https://github.com/LuckyDenis/tzintime/

.. image:: https://img.shields.io/badge/pypi-v1.0.1-ffc30f.svg
    :target: https://pypi.org/project/intimezone/

.. image:: https://travis-ci.org/LuckyDenis/tzintime.svg?branch=master
    :target: https://travis-ci.org/LuckyDenis/tzintime/

-----

**Introduction**

This package is based on the library ``pytz``. Provides an interface, converting naive and localized time to another time zone. You can choose how the new time zone will be added - it will be added directly on the date itself or displayed separately (examples will be discussed below). You can also specify a date output template. Templates need to be configured according to the `datetime <https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior>`_ library's templates table.

-----

**Installation**

.. code-block:: python

    python -m pip install intimezone

-----

**Example & Usage**

This library supports only two methods of conversion. The first is ``flag='convert'`` (``flag=None``) adds a timezone to the base date. The second ``flag='localize'`` adds the time zone separately.

*Test dataset:*

.. code-block:: python

    >>> from intimezone import convert
    >>> ntime = 1545695999 # naive time
    >>> ltime = 1545695999.5219207 # localized time

*Default settings:*

.. code-block:: python

    >>> convert(ntime) # naive time
    'Mon, 24 Dec 2018 23:59:59'
    >>> convert(ltime) # localized time
    'Mon, 24 Dec 2018 23:59:59'

*The values flag='convert':*

.. code-block:: python

    >>> convert(ntime, tz='Europe/Madrid', flag='convert') # naive time
    'Tue, 25 Dec 2018 00:59:59'
    >>> convert(ltime, tz='Europe/Madrid', flag='convert') # localized time
    'Tue, 25 Dec 2018 00:59:59'

*The values flag='localize':*

.. code-block:: python

    >>> convert(ntime, tz='Europe/Madrid', flag='localize') # naive time
    'Mon, 24 Dec 2018 23:59:59 +0100(CET)'
    >>> convert(ltime, tz='Europe/Madrid', flag='localize') # localized time
    'Mon, 24 Dec 2018 23:59:59 +0100(CET)'

*Custom template for date:*

.. code-block:: python

    >>> convert(ntime, tz='Europe/Madrid', f='%D - %H:%M:%S') # naive time
    '12/25/18 - 00:59:59'
    >>> convert(ltime, tz='Europe/Madrid', f='%D - %H:%M:%S') # localized time
    '12/25/18 - 00:59:59'

-----

**Options**

* The library provides a single interface. In order to select in which mode to get the date, the ``flag`` (``None``/``'convert'`` or ``'localize'``) option is used.

* The parameter ``moment_time`` can take unix time in the format ``int`` or ``float``. Represents moment-time.

* The time zone ``tz`` is specified in the format ``'Region/City'``, ``'Etc/GMT±12'``.

* ``f`` is responsible for generating a line at the output, through this parameter you can set a template in the style of templates of the standard library `datetime <https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior>`_.