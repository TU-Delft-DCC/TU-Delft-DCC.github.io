# Branch management

Branch management is an important consideration for working collaboratively with git and GitHub. Branching allows you to diverge from the main line of development and continue to do work without messing with that main line [1]. A good method for branch management is Gitflow [2]. The referenced [article](https://nvie.com/posts/a-successful-git-branching-model/) contains all information.   

In general, the `origin/master` branch is considered to be the main branch where the source code always reflects a _production-ready_ state, i.e. a stable source code that you would like to share with the community. The `origin/develop` branch is the main development branch where the source code always reflects a state with the latest delivered development changes for the next release. When the source code in the `origin/develop` branch reaches a stable point, it needs to be merged into `origin/master` and tagged with a release number.

When we work on specific features or bugs, we would like to do this in isolation to keep `origin/develop` clean. To do this, we use feature branches to develop new features for upcoming releases. When starting work on a new feature, branch off from `origin/develop` and develop the feature in isolation. When the feature is ready, create a [merge request](https://docs.gitlab.com/ee/user/project/merge_requests/getting_started.html) to merge the feature back into `origin/develop`. Once the feature branch is merged, it can be deleted.

To make it clear for other developers what you are working on, please use the following branch names
- Feature: `<your_name>/[name-of-feature]`
- Bug fix: `<your_name>/fix-[issue-number]` 
- Hot fix: `hotfix/[issue-number]` (for a bug in `origin/master`)
- Release: `release/[version]`

## Workflow examples
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

<img src="https://user-images.githubusercontent.com/15414938/110449882-f0639180-80c2-11eb-93a1-2688824c22cc.png" alt="git-model" width="500"/>

## Protected branches

GitLab will protect the `master` branch, see https://docs.gitlab.com/ee/user/project/protected_branches.html 

### References
[1] https://www.atlassian.com/git/tutorials/using-branches   
[2] https://nvie.com/posts/a-successful-git-branching-model/