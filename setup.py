#!/usr/bin/python
# -*- coding: utf-8 -*-

# SPAMU Simple Process and Automata Marshaller and Unmarshaller
# Copyright © 2016 Erwan Queffélec

import os
from setuptools import setup, find_packages

import spamu

setup(
    name='spamu',
    version=spamu.__version__,
    description='Spamu Process Automation Marshaller and Unmarshaller',
    long_description='',
    author='Erwan Queffélec',
    author_email='erwan.queffelec@gmail.com',
    packages=find_packages(exclude=('tests', 'tests.*')),
    scripts=['bin/spamu'],
    test_suite='tests',
    data_files=[],
    classifiers=[
        'Operating System :: Unix',
        'Programming Language :: Python :: 2',
    ],
)
