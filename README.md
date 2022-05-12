# Welcome
Welcome to the DCC guides! Here we try to address common issues related to Research Software, Data and Infrastructure at TU Delft. It is an ongoing and continuosly developing set of contents that we try to adapt as we go and in response to the community needs.

This repository also has a discussions "backend" where we try to address not only answers to problems, but also share ideas, questions, comments, or simply get an overview of hot topics we are discussing.

## Who is it for?
TU Delft Research community (researchers, and support staff working closeley with researcher, data stewards, data manager, RSEs, etc.)
> Originally we started this website to capture learnings to make our lives easier at the DCC. But the content is meant for any researcher at TU Delft that wants to get a quick orientation on fundamental topics of Open Science, FAIR software and FAIR data, research software infrastructure and tools, among other related topics.

## How to participate
- **Do you have a common problem, tip or suggestion related to Software, Data, Computational Environments or Research infrastructure?** Then find out if the topic has been already opened in our [discussions](https://github.com/TU-Delft-DCC/TU-Delft-DCC.github.io/discussions).

- **Do you want to improve or add content to the website?** You can fork the content and make a pull request. 
```{node} 
    Please include in the pull request your deployed version in github pages, i.e, the link to your deployed version. Make sure to enable github pages and deploy from the gh-pages branch in your forked repositroy.
```

### Reproducing the repository in a forked version
The most straightforward way to make a replica of this website is to fork this repository.
- Fork the repo.
- Setup github pages in the settings of your repository.
- Change the branch of github pages to `gh-pages`. 
- Clone it in your computer.
- Commit your markdown changes locally and push them to your fork.
- Inspect the continuous integration process. Go to gitub actions. There you will see a job running and making all the building and publishing steps in the cloud enabled by github services. 
- Once this actions is done you can go to environment and click on view deployment. Alternatively you can go to `https://<your-username>.github.io/TU-Delft-DCC.github.io/`



### Reproducing the repository in your pc
```{note}
In order to reproduce this code you need to have [jupyter book](https://jupyterbook.org/intro.html) installed. You can use jupyter cli to make changes, but we also provide some bash scripts make this step less tedious, in order to be able to use this scripts you need a unix shell as is written in bash.
```
- Fork first so that you can work on your own version and experiment there.
- Navigate to the `./docs` folder
- Simply run `bash build.sh`, this will automatically build a new table of contents and open the static website on your browser.
- Go to the `./_build/html/` folder and open the index.html file. This should launch the website with the latest version in your browser
```{warning}
You might need to open your browser in an incognito window, as the browser will cache some of the html files and will render old versions of the website.
```

## Common issues and trouble shooting
- When running the jupyter-book locally you might have installed different
