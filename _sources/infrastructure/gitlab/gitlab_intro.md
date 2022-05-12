# TU Delft GitLab
Imagine the following: you are working with a group on a research software code base. At this point your codebase might be quite large, dozens of scripts, and it has a good amount of dependencies. Furthermore, other researchers depend on your code to work properly for their own research. When your code becomes more relevant to yourself and your community, you will feel the urge to have more control on the quality of contributions. You would like to be able to easily upgrade and maintain the code, but also automate the process of packaging and publishing your code, instead of doing it manually everytime. 

The TU Delft offers a local instance of Gitlab at gitlab.tudelft.nl. Gitlab is an online Git repository management tool with a wiki, issue tracker, Continuous Integration and Continuous Deployment built-in. The service is intended for researchers. Similar services are, for example, GitHub.com or GitLab.com. In contrast to these services, GitLab TU Delft is hosted by the TU Delft itself, on campus. For more information, please consult the [documentation](https://gitlab.tudelft.nl/help).


## GitHub or TU Delft Gitlab?
The current instance of the TU Delft Gitlab has a few limitations:
- Hosting a website through pages is currently deactivated
- Continuous integration is not available by default. See our [guide](./gitlab_docker.md) on setting this up.
- Container registry has been disabled
- ...

The free edition of Gitlab has the following limitations:
- Wiki is not available in a private repository
- ...

## Table of Contents
```{tableofcontents}
```