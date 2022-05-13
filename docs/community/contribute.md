# Contributing guidelines

## 👋 Welcome!

- Do you have issues, tips, ideas, events, or questions related to Research Computing, Research Data, and Research Software at TU Delft?
- Are you a researcher interested in these topics?
- Do you work and collaborate with researchers on these topics?

We’re using [**GitHub Discussions**](https://github.com/TU-Delft-DCC/TU-Delft-DCC.github.io/discussions) as a place to connect with other members of our community. We hope that you:
* Ask questions about challenges you encounter
* Share ideas and solutions
* Engage with other community members
* Be welcoming and open-minded. Remember that this is a community we
build together. See our [Code of Conduct](code_of_conduct.md) for more information 💪.

## How to participate
Do you have questions, ideas or ongoing developments on FAIR related aspects, Open Science, training, etc? Would you like to point to specific resources and potential solutions or ideas?

-  Use the [**Q&A**](https://github.com/TU-Delft-DCC/TU-Delft-DCC.github.io/discussions/categories/q-a) to ask a question on a specific topic, such as
    - _How do I generate a reproducible software development environment?_
    - _Where can I find information on creating a Python package?_
    - _How should I archive my software?_
    - _How do I get started with git?_

-  Use [**Ideas**](https://github.com/TU-Delft-DCC/TU-Delft-DCC.github.io/discussions/categories/ideas) to make proposals, for instance 
    - _Using jupyter hub for a workshop_
    - _Using jupyter books to create educational resources_
    - _Running monthly webinars for the community to transfer FAIR practices_

- Use [**Solutions**](https://github.com/TU-Delft-DCC/TU-Delft-DCC.github.io/discussions/categories/solution) to point people to existing solutions or share your own. These solutions might end up on our Guides website to share with our community.

- [**Show and tell**](https://github.com/TU-Delft-DCC/TU-Delft-DCC.github.io/discussions/categories/show-and-tell) things you have done that you are proud of and like other to be aware of.


### For moderators and maintainers
For the maintainers, here are some tips 💡 for getting started with Discussions. 

🔗 If you use issue templates, **link any relevant issue templates** such as questions and community conversations to Discussions. Declutter your issues by driving community content to where they belong in Discussions. If you need help, here's a [link to the documentation](https://docs.github.com/en/github/building-a-strong-community/configuring-issue-templates-for-your-repository#configuring-the-template-chooser).

➡️ You can **convert issues to discussions** either individually or bulk by labels. Looking at you, issues labeled “question” or “discussion”.

## For developers

### Developing and building the guides locally
1. Fork the repository to your own Github profile
1. Clone the repository
1. Create a conda environment in the terminal with 

    ```bash
    conda env create -f environment.yml
    ```
1. Run `bash build.sh` to generate the documentation
1. Go to the `./_build/html/` folder and open the `index.html` file. This should open the website in your browser.

### Deploying the website in your forked version
1. Fork the repository to your own Github profile
1. In your forked repository, under **Settings -> Pages** set Source to `gh-pages` and `/(root)` and press **Save**
1. Either commit a new change to the repository to trigger the build action or manually trigger the action. To manually trigger the action, go to **Actions -> Deploy guides** and press `Run workflow` and `Run workflow`.

### You want to make some kind of change
1. (**important**) announce your plan to the rest of the community *before you start working*. This announcement should be in the form of a (new) issue;
1. (**important**) wait until some kind of consensus is reached about your idea being a good idea;
1. if needed, fork the repository to your own Github profile and create your own feature branch off of the latest master commit. While working on your feature branch, make sure to stay up to date with the master branch by pulling in changes, possibly from the 'upstream' repository (follow the instructions [here](https://help.github.com/articles/configuring-a-remote-for-a-fork/) and [here](https://help.github.com/articles/syncing-a-fork/));
1. [push](http://rogerdudler.github.io/git-guide/) your feature branch to (your fork of) the DCC guides repository on GitHub;
1. create the pull request, e.g. following the instructions [here](https://help.github.com/articles/creating-a-pull-request/). If needed, provide a link to the gh-pages in your forked repository: `https://<your-username>.github.io/TU-Delft-DCC.github.io/`.
