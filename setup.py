from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='django_hamage_demo',
      version=version,
      description="Scratch django project for testing spam control strategies",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Paul M. Winkler',
      author_email='slinkp@gmail.com',
      url='',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'django>=1.3',
          # 'hamage',
          'twod.wsgi',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
