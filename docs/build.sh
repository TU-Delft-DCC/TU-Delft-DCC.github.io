!/bin/bash
# Build jupyter-books faster with chained toc, build and launching in bash
# A simple bash script to automate the building of table of contents,

REPO=$(pwd)

# if test -f "_toc.yml"; then
#     rm -f "_toc.yml"
# fi

# Build table of contents website
jupyter-book toc from-project "${REPO}" > _toc.yml

# if test -f "./_build"; then
#     rm -r -f "./_build"
# fi
# Build html
jupyter-book build ${REPO}

# Copy slides inside _build/html
cp -R ../slides ./_build/html