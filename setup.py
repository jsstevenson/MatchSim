"""Defines how metakb is packaged and distributed."""
from setuptools import setup

exec(open('match/version.py').read())
setup(version=__version__)
