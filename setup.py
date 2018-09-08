# -*- coding: utf8 -*-

import codecs
from setuptools import setup, find_packages

from intimezone import __about__ as about


with codecs.open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()
with codecs.open('HISTORY.rst', 'r', 'utf-8') as f:
    history = f.read()


setup(
    name=about.__title__,
    version=about.__version__,
    description=about.__description__,
    author=about.__author__,
    url=about.__url__,
    author_email=about.__email__,
    platforms=about.__platforms__,
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/x-rst',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=['pytz>=2018.5'],
    keywords='datetime, utc, timezone',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)
