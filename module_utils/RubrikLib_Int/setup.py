# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# coding: utf-8

from setuptools import setup, find_packages

NAME = "rubriklibint"
VERSION = "0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["msrest>=0.2.0"]

setup(
    name=NAME,
    version=VERSION,
    description="RubrikLib_Int",
    author_email="",
    url="",
    keywords=["Swagger", "RubrikLib_Int"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    This is the INTERNAL REST API for Rubrik. We don't guarantee support
    or backward compatibility. Use at your own risk.
    """
)
