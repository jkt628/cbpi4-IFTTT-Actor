"""cbpi4-IFTTT-Actor is a plugin for CraftBeerPi 4 using IFTTT Maker Webhooks"""
from setuptools import setup

setup(name='cbpi4-IFTTT-Actor',
      version='0.0.2',
      description='CraftBeerPi Plugin',
      author='',
      author_email='',
      url='',
      install_requires=['requests'],
      include_package_data=True,
      package_data={
        # If any package contains *.txt or *.rst files, include them:
      '': ['*.txt', '*.rst', '*.yaml'],
      'cbpi4-IFTTT-Actor': ['*','*.txt', '*.rst', '*.yaml']},
      packages=['cbpi4-IFTTT-Actor'],
     )
