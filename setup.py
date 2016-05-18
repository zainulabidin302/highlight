# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Highligh',
    version='0.0.1',
    description='A Content Searchable Engine',
    long_description=readme,
    author='Zain Ulabidin',
    author_email='zain@zforapple.com',
    url='https://github.com/zainulabidin302/highlight',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

