# -*- coding: utf8 -*-
from setuptools import setup, find_packages

setup(
    name='intimezone',
    version='1.0',
    description='Converts the UTC time, the date and time of the region.',
    long_description='Library for converting time from UTC to date,'
                     'depending on the specified "region/city". '
                     'You can use standard date and time templates.',
    author='Denis Belavin',
    packages=find_packages(),
    platforms='any',
    zip_safe=False,
    url='https://github.com/LuckyDenis/tzintime',
    include_package_data=True,
    install_requires=['pytz==2018.5'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: MIT',
        'Programming Language :: Python 3',
    ],
)
