from setuptools import setup
import setuptools

with open("README.md","r") as fh:
    long_description = fh.read()

setup(
    name = "My_Sort_1",
    version='0.0.1',
    description='Sorting a Number',
    author="Muthu Raman",
    url = "https://github.com/Muthuram05/Algorithms-in-python",
    long_description= long_description,
    packages=setuptools.find_packages(),
    keywords=["sorting","sort"],
    py_modules=["Sort"],
    package_dir={'':'src'},
)