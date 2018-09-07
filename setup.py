# -*- coding: utf8 -*-

import codecs
from setuptools import setup, find_packages

from intimezone import __about__ as about


def read(filename):
    with codecs.open(filename, 'r', 'utf8') as f:
        return f.read()


setup(
    name=about.__title__,
    version=about.__version__,
    description=about.__description__,
    author=about.__author__,
    url=about.__url__,
    author_email=about.__email__,
    platforms=about.__platforms__,
    license=about.__license__,
    long_description=read('README.rst'),
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=['pytz>=2018.5'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: MIT',
        'Programming Language :: Python 3',
    ],
)
