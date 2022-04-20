# !/bin/bash

# Clean cache
jupyter-book clean docs/

# Build html
jupyter-book build docs/

# Copy slides inside _build/html
cp -R docs/slides docs/_build/html