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
package_data = {'html':'*.html','css':'*.css','js':'*.js'},
url = 'https://github.com/akshbn/creamware',
packages = ['cream','assets'],
entry_points = {"console_scripts":["cream=cream.cream:main"]}
)
