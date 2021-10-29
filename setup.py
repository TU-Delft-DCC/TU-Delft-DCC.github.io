from setuptools import setup, find_packages

setup(
    name="example",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'jupyter-book',
        'ghp-import'
    ]
)