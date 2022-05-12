import os, sys
import frontmatter
import pandas as pd
import logging
from typing import List

# Set up logger
FORMATTER = logging.Formatter("%(levelname)s : %(message)s")
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(FORMATTER)
log.addHandler(handler)


def create_page_maintainers(path: str = './docs'):
    """Create a .md file with all maintainers

    Parameters
    ----------
    path : str, optional
        directory of the jupyter book, by default "./docs"
    
    """

    files = get_filenames_in_toc(path)
    df = get_metadata(files)
    write_authors_page(df, path)


def get_filenames_in_toc(path: str) -> List:
    """Get list of filenames from _toc.yml

    Parameters
    ----------
    path : str
        directory of the jupyter book

    Returns
    -------
    list
        filepaths of files in _toc.yml
    """
    toc_file = os.path.join(path, '_toc.yml')
    files = []
    with open(toc_file, 'r') as f:
        for line in f:
            if '- file:' in line:
                files.append(line.strip().split()[-1])

    filepaths = [os.path.join(path, f"{file}.md") for file in files]
    return filepaths


def get_metadata(files: List) -> pd.DataFrame:
    """Return DataFrame with metadata stored as yaml frontmatter in the .md files

    Parameters
    ----------
    files : List
        list of filepaths

    Returns
    -------
    pandas.DataFrame
        dataframe with the metadata from the articles
    
    """ 
    entries = []
    for file in files:
        try:
            post = frontmatter.load(file)
            details = [post["section"], post["title"], post["author_1"], post["author_2"]]
            entries.append(details)
            log.info(f"Added metadata found in {file}")
        except:
            log.debug(f"No metadata found in {file}")        
    
    return pd.DataFrame(entries, columns = ["Section", "Title", "Lead maintainer", "Backup maintainer"])    


def write_authors_page(df: pd.DataFrame, path):
    """Write markdown page in book_path/community/maintainers.md

    Parameters
    ----------
    df : pd.DataFrame
        dataframe with the metadata from the articles
    path : str
        directory of the jupyter book
    """
    file = os.path.join(path, 'community', 'maintainers.md')
    with open(file, 'w') as f:
        f.write("# Guide maintainers \n\n")
        f.write("_This content is automatically generated, all changes made will be lost._ \n\n")
        f.write(df.sort_values(by=["Section"]).to_markdown(index=False))        


if __name__ == '__main__':
    if len(sys.argv) == 2:
        create_page_maintainers(sys.argv[1])
    else:
        create_page_maintainers()