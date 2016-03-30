# -*- Coding utf-8 -*-
import sys

from setuptools import setup

setup(
name = 'cream',
version = '0.1.0dev',
license = 'MIT',
author = 'Akshay B N',
description = 'Scaffolding and templating engine experiment',
zip_safe = False,
include_package_data = True,
url = 'https://github.com/akshbn/creamware',
packages = ['cream'],
entry_points = {"console_scripts":["cream=cream.cream:main"]}
)
