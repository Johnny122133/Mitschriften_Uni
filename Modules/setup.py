from setuptools import setup, find_packages, find_namespace_packages

setup(
    name='Modules',
    version='0.1.1',
    packages=find_packages(include=['Modules']),
    namespace_packages = find_namespace_packages(include=['Modules'])
)