#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('COPYING.LESSER') as f:
    license = f.read()

setup(
    name='glstring',
    version='0.1.0',
    description='GL String handling functions, including sanity checks',
    long_description=readme,
    author='Bob Milius',
    author_email='bmilius@nmdp.org',
    url='https://github.com/nmdp-bioinformatics/pyglstring',
    license=license,
    packages=find_packages(exclude=('tests', 'docs', 'bin'))
)

