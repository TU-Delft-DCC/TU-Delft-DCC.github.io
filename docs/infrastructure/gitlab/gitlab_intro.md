---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use MM/DD/YYYY]
# Uncomment and populate the next line accordingly
#date: MM/DD/YYYY

# We use this key to indicate the last modified date [automatic entry]
date-modified: last-modified

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: TU Delft GitLab

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
#description: Short description of the document
#hide-description: true

# Authors of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
#author_1: Name Surname
#author_2:

# Maintainers of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
#maintainer_1: Name Surname
#maintainer_2:

# To whom reach out regarding the document, will not be parsed [manual entry]
# Uncomment and populate the next line accordingly
#corresponding: Name Surname

# Meaningful keywords, newline separated [manual entry]
# Uncomment and populate the next line and list accordingly
#categories: 
# - 
# - 

---

Imagine the following: you are working with a group on a research software code base. At this point your codebase might be quite large, dozens of scripts, and it has a good amount of dependencies. Furthermore, other researchers depend on your code to work properly for their own research. When your code becomes more relevant to yourself and your community, you will feel the urge to have more control on the quality of contributions. You would like to be able to easily upgrade and maintain the code, but also automate the process of packaging and publishing your code, instead of doing it manually everytime. 

The TU Delft offers a local instance of GitLab at gitlab.tudelft.nl. GitLab is an online Git repository management tool with a wiki, issue tracker, Continuous Integration and Continuous Deployment built-in. The service is intended for researchers. Similar services are, for example, GitHub.com or GitLab.com. In contrast to these services, GitLab TU Delft is hosted by the TU Delft itself, on campus. For more information, please consult the [documentation](https://gitlab.tudelft.nl/help).


## GitHub or TU Delft GitLab?
The current instance of the TU Delft GitLab has a few limitations:

- Hosting a website through pages is currently deactivated
- Continuous integration is not available by default. See our [guide](./gitlab_docker.md) on setting this up.
- Container registry has been disabled
- ...

The free edition of GitLab has the following limitations:

- Wiki is not available in a private repository
- ...
