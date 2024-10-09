<!-- ---
section: software
title: Branch management
author_1: Maurits Kok
author_2: 
--- -->

# Branch management

Branch management is an important consideration when working collaboratively with Git and GitHub. In Git, branches are a part of your everyday development process. Git branches are effectively a pointer to a snapshot of your changes. When you want to add a new feature or fix a bug — no matter how big or how small — you spawn a new branch to encapsulate your changes.

Branches are primarily used as a means for teams to develop featurest and give them a separate workspace for their code. Branching allows you to diverge from the main (stable) version of development and continue to do work without affecting that main line[^1]. 

A branching strategy, therefore, is the strategy that teams adopt when writing, merging and releasing code when using a version control system. It is essentially a set of rules that developers can follow to stipulate how they interact with a shared codebase.

For open source projects, the branching strategy is often described in the [Contributing guide](../../../CONTRIBUTING.md) of the repository.

:::{.callout-note title="A branching strategy aims to"}

- Enhance productivity by ensuring proper coordination among developers
- Enable parallel development
- Help organize a series of planned, structured releases
- Map a clear path when making changes to software through to production
- Maintain a bug-free code where developers can quickly fix issues and get these changes back to production without disrupting the development workflow
:::

Various branch management workflows have been developed for different teams and software types[^2]. When developing research software, we recommend using either GitHub Flow or Gitflow[^3].

## GitHub flow
GitHub Flow is a simpler alternative to GitFlow ideal for smaller teams. This strategy relies on three different branches:

- Main: `main`
- Develop: `develop`
- Feature: `feature/[name-of-feature]`

You start off with the master branch then developers create feature branches that stem directly from the master to isolate their work. When ready, these are then merged back into main and the feature branch is deleted.

### Example workflow
**Aim:** create a new feature  

1. Create new descriptively-named branches off the master branch for new work, such as `feature/add-new-payment-types`.
2. Commit new work to your local branches and regularly push work to the remote.
3. To request feedback or help, or when you think your work is ready to merge into the `master` branch, open a pull request.
4. After your work or feature has been reviewed and approved, it can be merged into the `master` branch.
5. Once your work has been merged into the `master` branch, it is available for use.

![](../../img/github-flow-branching-model.jpeg)

### Benefits of GitHub Flow
1. Simple design
2. Works well for small teams, especially without (anonymous) external contributors
3. Suitable for teams that continuously deploy production code

### Challenges of GitHub Flow
1. Unable to support multiple versions of code in production at the same time
2. The lack of dedicated development branches makes GitHub Flow more susceptible to bugs in production.


## Gitflow

Gitflow is more complicated and advances, but allows for more control over the development cycle. The main idea behind the [Git flow branching strategy](https://www.gitkraken.com/learn/git/git-flow) is to isolate your work into different **types of branches**. There are six different branch types in total:

- Main: `main`
- Develop: `develop`
- Feature: `feature/[name-of-feature]`
- Bug fix: `fix/[issue-number]` 
- Hot fix: `hotfix/[issue-number]` (for a bug in `origin/master`)
- Release: `release/[version]`

The two primary branches in Gitflow are `main` and `develop` and have an infinite timeline. The other branches are temporary supporting branches with different intended purposes: feature, release, bugfix, and hotfix.

<img src="https://user-images.githubusercontent.com/15414938/110449882-f0639180-80c2-11eb-93a1-2688824c22cc.png" alt="git-model" width="500"/>

In general, the `origin/master`branch is considered to be the main branch where the source code always reflects a _production-ready_ state, i.e. a stable source code that you would like to share with the community. The `origin/develop` branch is the main development branch where the source code always reflects a state with the latest delivered development changes for the next release. When the source code in the `origin/develop` branch reaches a stable point, it needs to be merged into `origin/master` and tagged with a release number.

We would like develop new code in isolation to keep `origin/develop` clean. To do this, we use feature branches to develop new features for upcoming releases. When starting work on a new feature, branch off from `origin/develop` and develop the feature in isolation. When the feature is ready, create a pull request to merge the feature back into `origin/develop`. Once the feature branch is merged, it should be deleted.

### Benefits of GitFlow

1. The various types of branches make it easy and intuitive to organize your work.
1. The systematic development process allows for efficient testing.
1. The use of release branches allows you to easily and continuously support multiple versions of production code.
1. Structured and more secure approach better suited for open source project with contributions from external (anonymous) developers.

### Challenges of GitFlow

1. Depending on the complexity of the product, the Git flow model could overcomplicate and slow the development process and release cycle.
1. Because of the long development cycle, Git flow is historically not able to support Continuous Delivery or Continuous Integration.

### Workflow examples
**Aim:** implement new features into the code.

1. General development of the code takes place on `origin/develop`. When you want to fix a bug or work on a new feature, first create an issue where you announce what you will be working on.
1. When you want to work on a new feature or fix a bug, create a new feature branch from the development branch. 
1. Work on the code in the feature branch.
1. Create a merge request on GitLab to merge the feature branch into the development branch when ready. A good practice is to invite another developer to review your feature.
1. Repeat previous steps to implement more features. Best practice is to keep the merge requests small; this makes it easy to review and limits the possibilty of generating conflicts.

**Aim:** create a new release on `origin/master`.

1. When ready to make a new release, create a release branch from the development branch.
1. On the release branch: compile and package the software, update documentation, update version, dotting i's, ...
1. Create a merge request to merge the release branch with the main branch and back into the development branch. 
1. Delete release branch after merge.
1. Create a [new release](https://docs.gitlab.com/ee/user/project/releases/) in the master branch.

<!-- 
[^1]: https://www.atlassian.com/git/tutorials/using-branches   
[^2]: https://www.flagship.io/git-branching-strategies/ 
[^3]: https://nvie.com/posts/a-successful-git-branching-model/ -->