#!/usr/bin/env python
"""
Generic Catalog Reader (GCR)
A common reader interface for accessing generic catalogs
https://github.com/yymao/generic-catalog-reader
The MIT License (MIT)
Copyright (c) 2017 Yao-Yuan Mao (yymao)
http://opensource.org/licenses/MIT
"""

from setuptools import setup

setup(
    name='GCR',
    version='0.2.0',
    description='Generic Catalog Reader: A common reader interface for accessing generic catalogs',
    url='https://github.com/yymao/generic-catalog-reader',
    author='Yao-Yuan Mao',
    author_email='yymao.astro@gmail.com',
    maintainer='Yao-Yuan Mao',
    maintainer_email='yymao.astro@gmail.com',
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='GCR catalog reader',
    py_modules=['GCR'],
    install_requires=['numpy'],
)
