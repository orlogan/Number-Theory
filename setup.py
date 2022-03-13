# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Number Theory',
    version='0.1.0.dev',
    description='Simple Package for Number Theory Algorithms',
    long_description=readme,
    author='Logan Reed',
    author_email='me@loganreed.org',
    url='https://github.com/orlogan/Number-Theory',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

