from setuptools import setup, find_packages

setup(
    name="example",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "jupyter-book>=0.12.3",
        "sphinx-book-theme>=0.3.2",
        "sphinx_inline_tabs",
        "sphinx-tabs",
    ],
)
