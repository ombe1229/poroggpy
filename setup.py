import setuptools
from setuptools import setup
import poroggpy


setup(
    name="poroggpy",
    version=poroggpy.__version__,
    author="ombe1229",
    author_email="h3236516@gmail.com",
    description="poroggpy python library",
    license="Apache 2.0",
    packages=setuptools.find_packages(),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ombe1229/poroggpy",
)
