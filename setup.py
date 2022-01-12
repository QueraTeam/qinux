import os

from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='qinux',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    description='Qinux',
    long_description=README,
    url='https://github.com/QueraTeam/qinux',
    author='Quera',
    author_email='info@quera.ir',
    install_requires=[
    ],
    classifiers=[
    ],
)
