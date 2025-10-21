# Contributing guidelines

## 👋 Welcome!

- Do you have tips, ideas, or questions related to Research Computing, Research Data, and Research Software at TU Delft?
- Are you a researcher interested in these topics?
- Do you work and collaborate with researchers on these topics?

We use [**GitHub Discussions**](https://github.com/TU-Delft-DCC/TU-Delft-DCC.github.io/discussions) as a place to connect with other members of our community. We hope that you:

- Ask questions you’re wondering about.
- Share ideas (and solutions).
- Engage with other community members.

## Code of Conduct

Please be welcoming and open‑minded. This is a community we build together. See our [Code of Conduct](CODE_OF_CONDUCT.md) for more information.

## How to participate

Do you have questions you'd like to ask? Would you like to point to specific resources and potential solutions or ideas? Would you like to contribute to the development of these guides? Select the *Discussions* category that best matches your situation:

- Use the [*Q&A*](https://github.com/TU-Delft-DCC/TU-Delft-DCC.github.io/discussions/categories/q-a) to ask a question on a specific topic.

- Use [*Ideas*](https://github.com/TU-Delft-DCC/TU-Delft-DCC.github.io/discussions/categories/ideas) to propose new features, topics, or improvements.

- Use [*Solutions*](https://github.com/TU-Delft-DCC/TU-Delft-DCC.github.io/discussions/categories/solutions) to share worked examples, guidelines, or solutions. Strong posts in this category may be integrated into the DCC guides by maintainers.

- You can also use [*Polls*](https://github.com/TU-Delft-DCC/TU-Delft-DCC.github.io/discussions/categories/polls) to gather opinions or vote on a change or idea.

- Lastly, you can use the section [*Docs draft box*](https://github.com/TU-Delft-DCC/TU-Delft-DCC.github.io/discussions/categories/docs-draft-box) to simply share plain‑text drafts or outlines for new or updated guides. Maintainers can review, edit, and integrate these into the DCC guides. Any contribution is appreciated.

Consider watching or subscribing to categories of interest in *Discussions* to follow updates and replies.

### You want to make some kind of change

If you want to propose a change to the content of the guides, you can do so by either:

1. Opening a new issue describing the change you would like to see. 
    - This is the preferred way for small changes, typos, or if you are unsure about how to proceed.
    - Maintainers will either implement the change themselves or help you to integrate your proposed changes. Maintainers may convert an issue to a *Discussion* if that’s a better fit.
1. Opening a discussion in a relevant category (see [above](#how-to-participate)). 
    - Maintainers can help you to integrate your proposed changes.
1. Creating a pull request with the proposed changes. 
    - This would be the ideal way to propose changes (and if you are familiar with the steps described [below](#for-developers)).
    - Include a short summary and links to any related discussion/issue, and keep the pull request focused on a single topic.
    - Open it as a draft if you want early feedback.

## For developers

If you wish to contribute to the development of these guides directly, please follow the instructions below.

### Developing and building the guides locally

1. Fork the repository to your own GitHub profile.
1. Clone the repository.
1. Navigate to the root of this repository in your terminal.
1. Install Quarto if you don't already have it installed on your machine. You can find the installation instructions [here](https://quarto.org/docs/get-started/).
    - Alternatively, install Quarto within a virtual environment using the `environment.yml` file by:
        - Running `conda env create -f environment.yml` in the terminal to create a conda environment with Quarto pre-installed.
        - Activating the environment by running `conda activate dcc_guides`.  
1. Run `quarto preview` in your terminal.
1. You will see the rendered version in a browser window.

### Deploying the website in your forked version

1. In your forked repository, either commit a new change to the repository to trigger the build action or manually trigger the action. 
    - To manually trigger the action, go to **Actions → Quarto Publish Guides** and press `Run workflow` and again `Run workflow`.
1. In your forked repository, under **Settings → Pages** set Source to `gh-pages` and `/(root)` and press **Save**.

### Creating a pull request

1. Make sure your changes are committed and pushed to your forked repository.
    - Note: While working on your feature branch, make sure to stay up to date with the main branch by pulling in changes regularly.
1. Go to the original repository where you want to propose the changes.
1. Click on the "Pull requests" tab.
1. Click on the "New pull request" button.
1. Select the branch from your forked repository that contains your changes.
1. Review the changes and add a descriptive title and comment for your pull request.
1. Click on the "Create pull request".
1. Wait for maintainers to review your pull request. They may provide feedback or request changes before merging it.

### YAML front matter template (optional)

- For new guide pages, please copy the [Quarto front matter template](https://github.com/TU-Delft-DCC/TU-Delft-DCC.github.io/blob/main/_templates/quarto-front-matter.yml) into the top of your `.md` file. 
- Maintainers will add it if omitted.

## Notes on review and integration

- Maintainers will review contributions for scope and fit with the site’s content
- Content may be edited for style, structure, and metadata to ensure consistency across the guides.

