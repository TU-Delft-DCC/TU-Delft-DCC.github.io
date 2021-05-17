!/bin/bash
# Build jupyter-books faster with chained toc, build and launching in bash
# A simple bash script to automate the building of table of contents,
# The static website and also to launch the local static website 

REPO=$(pwd)
cd ..
echo "Changed directory to: $(pwd)"

# Build table of contents
jupyter-book toc "${REPO}"
echo "Table of contents built succesfully"
cat  "${REPO}/_toc.yml"

# Build static website
jupyter-book build ${REPO}

# Launch static website
cd ${REPO}/_build/html
# start index.html
# echo "Opened static website in browser"