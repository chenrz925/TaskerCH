# -*- coding: utf-8 -*-
# Copyright 2019-2020 Chen Runze. All Rights Reserved.
#
# This Source Code Form is subject to the terms of the
# Apache License Version 2.0. If a copy of the Apache
# License was not distributed with this file, You can
# obtain one at http://www.apache.org/licenses/LICENSE-2.0.

import taskerch as module
import setuptools

with open("README.md", "r") as fp:
    long_description = fp.read()
setuptools.setup(
    name="TaskerCH",
    version=module.__version__,
    author="Chen Runze",
    author_email="chenrz925@icloud.com",
    description="A scalable and extendable experiment task scheduler framework.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chenrz925/TaskerCH",
    packages=setuptools.find_packages(exclude=('tests',)),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Scientific/Engineering",
    ],
    python_requires=">=3.7",
    install_requires=[
        "toml>=0.10.0",
        "python-box>=4.0.4",
        "colorama>=0.4.3",
    ],
)
