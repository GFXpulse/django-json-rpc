#!/usr/bin/env python

import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

HERE = os.path.dirname(os.path.abspath(__file__))

setup(
    name="django-json-rpc",
    version="0.7.3",
    description="A simple JSON-RPC implementation for Django",
    author="Samuel Sutch",
    author_email="sam@sutch.net",
    license="MIT",
    url="http://github.com/samuraisam/django-json-rpc/tree/master",
    download_url="http://github.com/samuraisam/django-json-rpc/tree/master",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment', 'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent', 'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Framework :: Django', 'Framework :: Django :: 3.2',
    ],
    packages=['jsonrpc'],
    zip_safe=False,  # we include templates and tests
    install_requires=['Django>=3.2', 'six'],
    package_data={'jsonrpc': ['templates/*']})
