---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-02-24

# We use this key to indicate the last modified date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date-modified: 2025-09-19

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
# Uncomment and populate the next line accordingly
title: Project management

# Brief overview of the document (will be used in listings) [manual entry]
# Uncomment and populate the next line and uncomment "hide-description: true".
#description: Short description of the document
#hide-description: true

# Authors of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
author_1: Elviss Dvinskis
author_2: Maurits Kok

# Maintainers of the document, will not be parsed [manual entry]
# Uncomment and populate the next lines accordingly
maintainer_1: Elviss Dvinskis
#maintainer_2:

# To whom reach out regarding the document, will not be parsed [manual entry]
# Uncomment and populate the next line accordingly
corresponding: Elviss Dvinskis

# Meaningful keywords, newline separated [manual entry]
# Uncomment and populate the next line and list accordingly
categories:
 - Software
 - Version Control
 - Collaboration
 - Project Management
 - GitHub
 - Issues
 - Project Board
---

[Git](https://git-scm.com/) is a distributed version control system that enables you to track changes in your code over time. Platforms like GitHub, GitLab and Bitbucket extend the features of git by providing a centralized location for storing repositories, collaborating, and providing powerful tools to plan, organize, and track your work efficiently.

::: {.callout-tip appearance="simple" icon="false"}
## {{< fa brands square-git >}} New to git?
If you are new to Git, we recommend starting with the [Software Carpentry lesson on version control with Git](https://swcarpentry.github.io/git-novice/).
:::

## Version control platforms

The choice between GitHub, GitLab and Bitbucket depends on your required features, privacy and other preferences, but all are Git-based platforms for version control. While numerous detailed comparisons exist online, here we will focus on GitHub.

::: {.callout-warning appearance="simple" icon="false"}
## {{< fa brands gitlab >}} TU Delft GitLab

TU Delft has its own [GitLab instance](https://gitlab.tudelft.nl/) hosted on campus. For more information, please visit the [help page](https://gitlab.tudelft.nl/help) documentation.

{{< fa share-from-square >}} [Choosing a Repository Manager - for TU Delft Researchers](https://zenodo.org/records/4725444)
:::

Similarly, whether you are using a version control system through your terminal or Integrated Development Environment (IDE), or using a GUI like [GitHub Desktop](https://github.com/apps/desktop), the core functionality remains the same.

::: {.callout-tip appearance="simple" icon="false" collapse="true"}
## {{< fa lightbulb >}} Learn more about GitHub Desktop

GitHub Desktop is a great choice if you are just starting out with version control, providing a user-friendly graphical interface that simplifies Git operations. It makes it easy to visualize changes, create branches, and manage pull requests without needing to use command-line Git commands.

{{< fa share-from-square >}} [Getting started with GitHub Desktop](https://docs.github.com/en/desktop/overview/getting-started-with-github-desktop)
:::

## GitHub issues

GitHub issues help you keep track of tasks, bugs, feature ideas in your project. They are like a to-do list items that everyone on your team can see and update.

How to use issues effectively:

1. **Use descriptive titles:** Write short, specific titles that make it easy to understand what the issue is about.
2. **Provide detailed descriptions:** Include all relevant information, steps to reproduce (if reporting a bug), and expected outcomes in the issue description. This ensures that anyone working on the issue has all the necessary context.
3. **Use labels:** Labels act like tags to help you organize and prioritize tasks.
4. **Assign people:** By assigning someone (or yourself) you let others know that you are picking up and working on this issue.
5. **Link related issues:** Connect related work by linking issues to provide context (add `#issue_number` to reference an issue).

GitHub Issues make it easier to manage your project, collaborate with others, and keep track of progress. As your project grows, you can use additional tools like milestones and project boards while still benefiting from well-organized issues.

:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn more

- [Quickstart for GitHub Issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/configuring-issues/quickstart)
- [Mastering GitHub Issues](https://gitprotect.io/blog/mastering-github-issues-best-practices-and-pro-tips/)
:::


## Project boards

Project boards on GitHub are designed for planning, organizing, and tracking work within a project. They serve as visual management interfaces that integrate directly with GitHub issues and pull requests. Project boards can be configured as Kanban boards, tables, or roadmaps, offering various layouts to suit different project management needs. Project boards can be particularly useful for visualizing the overall progress of your project and identifying bottlenecks in your workflow. They provide a high-level view that complements the detailed tracking offered by issues.

### Milestones

Using milestones you can break down large projects into smaller, more manageable parts. While project boards offer a visual, dynamic interface to manage and track your tasks, milestones serve as structured markers that help you monitor progress toward key project phases/goals.

:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn more

- [Example project board - TU Delft Astrodynamics Toolkit (Tudat)](https://github.com/orgs/tudat-team/projects/18)
- [Define a milestone](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/creating-and-editing-milestones-for-issues-and-pull-requests)
- [GitHub Guides for Issues and Projects](https://docs.github.com/en/issues/guides)
:::

## Managing projects on GitHub

When managing your project on GitHub, we recommend two approaches:

1. a **simplified approach** using only issues, or
2. a more **structured approach** using milestones and project boards. 

Both methods have advantages, and the choice depends on the size of the project, its complexity, and your preferences.

::: {.panel-tabset}
## Simplified approach
You can use a simplified approach and just track your progress in the form of issues and work without defining milestones or using a project board. This can be particularly useful for smaller projects or when you are just starting out with GitHub. 

In this approach, you would:

1. Create issues for each task or feature you need to work on.
1. Optionally, use labels to categorize and prioritize your issues.
1. Assign issues to yourself or team members/collaborators.
1. Use comments to update progress and discuss any challenges.
1. Close issues as you complete them.

This method allows for a flexible workflow while still maintaining a good level of organization and transparency in your project. If your project grows or becomes more complex, you can always adopt milestones and project boards for more structured project management.


## Structured approach
When working on a big project, it's helpful to create **a roadmap** - a simple plan that outlines what needs to be done and when. A roadmap gives you and your team a clear view of what’s happening now and what’s coming next.

To create a roadmap, it is useful to map out the key milestones and the tasks needed to accomplish the milestones. You can then use GitHub milestones and project boards to track progress and manage your project:

1. Define key milestones.
2. Create a milestone in GitHub
3. Add related issues to your milestone.
4. Set up a project board.
5. Add issues to your project board.
6. Use task lists in your issues to break down the work.
7. Assign tasks to team members.
8. Linking milestones, issues and pull requests to track progress.

:::

## GitHub benefits for researchers and organisations

Researchers at TU Delft are eligible to receive [GitHub Educational benefits](https://github.com/education), which includes

- GitHub Team plan at no cost (check out [the benefits](https://github.com/pricing))
- GitHub Codespaces
- GitHub Pages for private repositories
- And more!

To qualify for the benefits, you must:

- Have a GitHub account
- Be an educator, faculty member, or researcher at a recognized educational institution
- Be able to provide documentation from your institute demonstrating your employment

:::{.callout-tip appearance="simple" icon="false"}
{{< fa share-from-square >}}  [Apply for Educational benefits](https://education.github.com/discount_requests/application)
:::