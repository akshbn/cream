# -*- Coding utf-8 -*-
import sys

from setuptools import setup,find_packages

setup(
name = 'cream',
version = '0.1.0dev',
license = 'MIT',
author = 'Akshay B N',
description = 'Scaffolding and templating engine experiment',
zip_safe = False,
url = 'https://github.com/akshbn/creamware',
packages = find_packages(),
package_data = {'assets.html':['*.html'],'assets.css':['*.css'],'js':['*.js']},
entry_points = {"console_scripts":["cream=cream.cream:main"]}
)
