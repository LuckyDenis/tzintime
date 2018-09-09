# -*- coding: utf8 -*-

import io
from setuptools import setup, find_packages

from intimezone import __about__ as about


with io.open('README.rst', 'r', encoding='utf-8') as f:
    readme = f.read()


setup(
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Posix :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    name=about.__title__,
    version=about.__version__,
    description=about.__description__,
    author=about.__author__,
    url=about.__url__,
    author_email=about.__email__,
    license=about.__license__,
    install_requires=['pytz>=2018.5'],
    long_description=readme,
    long_description_content_type='text/x-rst',
    platforms=about.__platforms__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False
)
