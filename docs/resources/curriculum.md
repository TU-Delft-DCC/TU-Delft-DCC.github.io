---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use MM/DD/YYYY]
#date:

# We use this key to indicate the last modified date [automatic entry]
date-modified: last-modified

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
title: Research Software Curriculum

# Authors of the document, will not be parsed [manual entry]
author_1: Ashley Cryan
author_2: aurits Kok

# Maintainers of the document, will not be parsed [manual entry]
maintainer_1:
maintainer_2:

# To whom reach out regarding the document, will not be parsed [manual entry]
corresponding:

# Meaningful keywords, newline separated [manual entry]
categories: 
 - 
 - 

---

# Research Software Curriculum
These materials represent a curated curriculum designed to help you develop and maintain your repository and code base. All of the resources listed below are free to access and use, and supplementary material like video lessons has been added where possible and relevant.

## Bash
* [What is Bash?](https://opensource.com/resources/what-bash) - of all the shells available, Bash is one of the most popular, the most powerful, and the most friendly
* [Bash Essentials](https://www.guru99.com/linux-commands-cheat-sheet.html) – Bash commands commonly used to navigate file directories in your Terminal/GitBash
* [The Unix Shell lesson from Software Carpentries](http://swcarpentry.github.io/shell-novice/) - use of the shell is fundamental to using a wide range of other powerful tools and computing resources. These lessons will start you on a path towards using these resources effectively
* [Installation Instructions](https://carpentries.github.io/workshop-template/#shell) - particularly important for Windows users, as Bash comes pre-installed on Mac. Windows users will need to install GitBash following the instructions at this link
* [Using the Terminal in Mac](https://macpaw.com/how-to/use-terminal-on-mac) - The Terminal app allows you to control your Mac using a command prompt

## Git
* [What is Git?](https://www.youtube.com/watch?v=2ReR1YJrNOM)- 2-minute video overview of the technology and how it works
* [Install Git from GitHub Guides](https://github.com/git-guides/install-git) - Check if Git is already installed on your machine; if not, follow these instructions to get started. Notes: If you've already installed GitBash on Windows OS, you will have Git already. Installing GitHub Desktop will also install the latest version of Git if you don't already have it.
* [Installing Git from Software Carpentries](https://carpentries.github.io/workshop-template/#git) - Alternative installation instructions from Software Carpentries, including videos and details per OS. 
* [Intro to version control with Git from Code Refinery](https://coderefinery.github.io/git-intro/) – self-paced introductory lesson to version control using Git
* [Git Intro video lesson from Code Refinery - Day 1](https://www.youtube.com/watch?v=QcwQ8jeaHmc) - Recorded lesson from a May 2021 Code Refinery workshop on material in Intro to version control with Git, part 1/2
* [Git Intro video lesson from Code Refinery - Day 2](https://www.youtube.com/watch?v=MeHB_Fjssjw) - Recorded lesson from a May 2021 Code Refinery workshop on material in Intro to version control with Git, part 2/2
* [Branching and merging](https://coderefinery.github.io/git-intro/branches/) – lesson from Code Refinery on concept of branching in Git (featuring octopus diagram)
* [What is .gitignore?](https://www.freecodecamp.org/news/gitignore-what-is-it-and-how-to-add-to-repo/) – introduction to how and why to use the .gitignore file to not track some files in a project folder (e.g., because of their size or sensitivity)
* [Git command cheat sheet](https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet) – commonly used Git commands in one page that can also be downloaded

## GitHub/GitLab (remote repositories)
* [Understanding the GitHub flow](https://guides.github.com/introduction/flow/) – guide from GitHub on how and why to work with branches
* [Collaborative distributed version control](https://coderefinery.github.io/git-collaborative/) - We have learned how to make a git repository for a single person. What about sharing?
* [SSH connection to GitHub](https://coderefinery.github.io/installation/ssh/) – instructions to set up SSH connection to GitHub so that you do not need to input your login credentials with every push/pull
* [Gitlab and SSH keys](https://docs.gitlab.com/ee/user/ssh.html) - instructions to add an SSH key to your (TU Delft) GitLab account for the same reason as above
* [GitHub without the Command Line from Code Refinery](https://coderefinery.github.io/github-without-command-line/) - practice collaborating and sharing using either the GitHub website or GitHub desktop application
* [GitHub Guides: Mastering Markdown](https://guides.github.com/features/mastering-markdown/) - Markdown is a lightweight and easy-to-use syntax for styling all forms of writing on the GitHub platform.

## Jupyter Notebooks and JupyterLab
* [Introduction to Jupyter and JupyterLab](https://coderefinery.github.io/jupyter/) - lesson material on the user interface of JupyterLab, how Jupyter notebooks work, and what some common and powerful usecases are

## Anaconda Navigator and managing conda environments
* [Anaconda Installation Guide from Software Carpentries](https://carpentries.github.io/workshop-template/#python) - Although one can install a plain-vanilla Python and all required libraries by hand, we recommend installing Anaconda, a Python distribution that comes with the latest version of Python and Jupyter Notebooks by default
* [Intro to Anaconda Navigator](https://docs.anaconda.com/free/navigator/getting-started/) - Anaconda Navigator is a graphical user interface to the conda package and environment manager. This 10-minute guide to Navigator will have you navigating the powerful conda program in a web-like interface without having to learn command line commands
* [Introduction to Conda for (Data) Scientists](https://carpentries-incubator.github.io/introduction-to-conda-for-data-scientists/) -  Conda is an open source package and environment management system that easily creates, saves, loads, and switches between environments on your local computer
* [Managing Conda environments](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) - documentation on performing a range of common tasks with Conda using the command line

## Python
* [Scientific Computing with Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/) - a free video course series that teaches the basics of using Python 3
* [Applied Data Science with Python Specialization](https://www.coursera.org/specializations/data-science-python?utm_source=gg&utm_medium=sem&utm_campaign=29-AppliedDataSciencePython-ROW&utm_content=29-AppliedDataSciencePython-ROW&campaignid=13259947800&adgroupid=117959621210&device=c&keyword=introduction%20to%20python&matchtype=b&network=g&devicemodel=&adpostion=&creativeid=524072187253&hide_mobile_promo&gclid=CjwKCAjwjdOIBhA_EiwAHz8xmzgKFVlySbCes2TmwDAB08gMJM3xW3QfOXp3NjVhym45aLS3nbCaFBoC3LEQAvD_BwE) - Coursera course in which you can enroll for free 
* [LearnPython.org](https://www.learnpython.org/) - Whether you are an experienced programmer or not, this website is intended for everyone who wishes to learn the Python programming language
* [Programming with Python from Software Carpentries](https://swcarpentry.github.io/python-novice-inflammation/) - this introduction to Python is built around a common scientific task: data analysis
* [Plotting and Programming with Python from Software Carpentries](http://swcarpentry.github.io/python-novice-gapminder/) - an introduction to programming in Python for people with little or no previous programming experience using plotting as its motivating example
* [Data Analysis and Visualization with Python for Social Scientists](https://datacarpentry.org/python-socialsci/) - basic information about Python syntax, the Jupyter notebook interface, how to import CSV files, using the pandas package to work with data frames, how to calculate summary information from a data frame, and a brief introduction to plotting. The last lesson demonstrates how to work with databases directly from Python
* [Can You Speak Python?](https://github.com/wmvanvliet/gizmo) - test your knowledge of some important features of the Python programming language and the NumPy and Pandas libraries

## Pandas
* [Getting started with Pandas](https://pandas.pydata.org/getting_started.html) - documentation and quick start guide for Pandas, an essential Python library used for working with data sets. It has functions for analyzing, cleaning, exploring, and manipulating data
* [Pandas Tutorial](https://www.w3schools.com/python/pandas/default.asp) - 14-part tutorial series featuring live code examples and tests of your knowledge
* [Pandas Data Wrangling Cheat Sheet](https://towardsdatascience.com/pandas-data-wrangling-cheat-sheet-2021-cf70f577bcdd) - to excel data analysis/data science/machine learning in Python, Pandas is a library you need to master. Here is a cheat sheet of some of the most used syntax that you probably don’t want to miss
* [Pandas Cheat Sheet - Visual](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf) - visual, printable 2-page reference guide on commonly performed operations using Pandas
* [Ultimate Pandas Guide — Inspecting Data Like a Pro](https://medium.com/towards-data-science/ultimate-pandas-guide-inspecting-data-like-a-pro-9b4f13c39c94) - Whether you’re working on a simple analysis or a complex machine learning model, there’s a lot of value in being able to answer quick, exploratory questions about the nature of your data. This is a walk through of several DataFrame attributes and methods that make data inspection painless and productive
* [10 Efficient Ways for Inspecting a Pandas DataFrame Object](https://medium.com/codex/10-efficient-ways-for-inspecting-a-pandas-dataframe-object-3f66563e2f2) - A guide to using pandas effectively and efficiently

## Plotly
* [Getting Started with Plotly](https://plotly.com/python/getting-started/) - The plotly Python library is an interactive, open-source plotting library that supports over 40 unique chart types covering a wide range of statistical, financial, geographic, scientific, and 3-dimensional use-cases
* [Plotly Python Open Source Graphing Library](https://plotly.com/python/) - Examples of how to make line plots, scatter plots, area charts, bar charts, error bars, box plots, histograms, heatmaps, subplots, multiple-axes, polar charts, and bubble charts
* [Heatmaps with Plotly](https://plotly.com/python/heatmaps/) - How to make Heatmaps in Python with Plotly

## Ipywidgets
* [Ipywidgets documentation](https://ipywidgets.readthedocs.io/en/latest/) - ipywidgets, also known as jupyter-widgets or simply widgets, are interactive HTML widgets for Jupyter notebooks and the IPython kernel.
* [Introduction to ipywidgets](https://www.youtube.com/watch?v=wb6k_T4rKBQ) - in this tutorial video, learn about ipywidgets, a Python library for building interactive HTML widgets for your Jupyter browser.
* [Ipywidgets Interact Function | ipywidgets Examples of Slider, Dropdown, Checkbox, Text Box](https://www.youtube.com/watch?v=vtC5laIgMJc) - Video demo on how to make an ipywidgets slider, ipywidgets dropdown, ipywidgets checkbox, or an ipywidgets text box using Python code.

## R
* [Install R guide from Software Carpentries](https://carpentries.github.io/workshop-template/#r) - R is a programming language that is especially powerful for data exploration, visualization, and statistical analysis. To interact with R, we use RStudio, which must also be installed separately from [here](https://www.rstudio.com/)
* [Programming with R from Software Carpentries](http://swcarpentry.github.io/r-novice-inflammation/) - this introduction to R is built around a common scientific task: data analysis
* [R for Reproducible Data Analysis from Software Carpentries](http://swcarpentry.github.io/r-novice-gapminder/) - write modular code and best practices for using R for data analysis
* [R for Social Scientists](https://datacarpentry.org/r-socialsci/) - basic information about R syntax, the RStudio interface, how to import CSV files, the structure of data frames, how to deal with factors, how to add/remove rows and columns, how to calculate summary statistics from a data frame, and a brief introduction to plotting

## MATLAB
* [Using git with MATLAB](https://admin.kuleuven.be/icts/onderzoek/wetsoft/software/matlab/pdf/versioning-git-matlab.pdf) - Introduction into using MATLAB and version control with git 
* [Programming with MATLAB](http://swcarpentry.github.io/matlab-novice-inflammation/) - Lesson from the Software Carpentries on the basics of programming with MATLAB

## Modular Code and testing
* [Writing tests](https://coderefinery.github.io/testing/) - lesson from CodeRefinery on automated testing
* [Video testing lesson](https://www.youtube.com/watch?v=s72AqTTi_Y8) - recording from software testing workshop by Code Refinery
* [Modular coding](http://cicero.xyz/v3/remark/0.14.0/github.com/coderefinery/modular-code-development/master/talk.md) - slides on modular code from Code Refinery

## Docker
* [Installing Docker](https://docs.docker.com/get-docker/) - installation instructions for Windows, macOS, and Linux
* [Install WSL2 update](https://docs.microsoft.com/en-us/windows/wsl/install-manual) - manual WSL2 update for Windows
* [Dockerfile reference](https://docs.docker.com/engine/reference/builder/) - information on how to write a Dockerfile

## VSCode 
* [Setting up VSCode for Linux](https://docs.microsoft.com/en-us/windows/wsl/tutorials/wsl-vscode) - guide to getting started using VSCode with Windows Subsystem for Linux

## Continuous Integration
* [GitHub Actions introduction course](https://github.com/skills/hello-github-actions) - an introductory course from GitHub on how to use GitHub Actions

## Reproducible Research
* [Reproducible Research material from Code Refinery](https://coderefinery.github.io/reproducible-research/) - demonstrates how version control, workflows, containers, and package managers can be used to record reproducible environments and computational steps
* [Reproducible Research video lesson from Code Refinery](https://www.youtube.com/watch?v=MxZF1gEJoWw) - Recorded video lesson from Code Refinery workshop in May 2021 on Reproducible Research material
* [Data + Code + Software = PDF](https://zenodo.org/record/5508797) - Slides to an overview on how to integrate data and software into a PDF.
