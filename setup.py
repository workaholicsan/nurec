from setuptools import setup, find_packages

setup(
  name='nurec',
  version='0.1',
  license='MIT',
  summary='Сhecking data recognition',
  packages=find_packages(),
  install_requires=[line.strip() for line in open("requirements.txt").readlines()],
)
