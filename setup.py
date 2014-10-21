#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='python-googlegeocoder',
    version='0.3.0',
    description='A simple Python wrapper for version three of Google\'s geocoder API',
    author='Ben Welsh',
    author_email='ben.welsh@latimes.com',
    url='http://datadesk.github.com/python-googlegeocoder/',
    packages=(
        "googlegeocoder",
    ),
    install_requires=("six>=1.4.1",)
)
