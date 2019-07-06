from setuptools import find_packages
from setuptools import setup

REQUIRED_PACKAGES = ["Flask>=0.8"]

setup(
  name='flask_queryparser',
  version='0.1',
  author = 'Matias Aravena',
  author_email = 'matias@spikelab.xyz',
  install_requires=REQUIRED_PACKAGES,
  packages=find_packages(),
  include_package_data=True,
  description='Simple query string parser decorator for Flask')