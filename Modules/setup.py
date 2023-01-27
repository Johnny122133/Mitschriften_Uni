from setuptools import setup, find_packages, find_namespace_packages

setup(
    name='modules',
    version='0.1.1',
    packages=find_packages(include=['modules']),
    namespace_packages = find_namespace_packages(include=['modules'])
)