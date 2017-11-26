#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ 'requests>=2.9.1' ]
setup_requirements = [ ]
test_requirements = [ ]

setup(
    name='ziggo_mediabox_xl',
    version='1.0.0',
    description="Python interface to Ziggo's Mediabox XL",
    long_description=readme + '\n\n' + history,
    author="Menno Blom",
    author_email='menno@b10m.net',
    url='https://github.com/b10m/ziggo_mediabox_xl',
    py_modules=['ziggo_mediabox_xl'],
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='ziggo_mediabox_xl',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
