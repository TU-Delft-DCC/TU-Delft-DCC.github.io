---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
# Uncomment and populate the next line accordingly
date: 2025-02-12

# We use this key to indicate the last modified date [automatic entry]
date-modified: last-modified

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
#categories: 
# - project management
# - github
# - issues
# - project board

---

Git is a distributed version control system that allows developers to track changes in their code over time. Platforms like GitHub, GitLab and Bitbucket enhance the capabilities of git by providing a centralized location for storing repositories, collaborating, and providing powerful tools to plan, organize, and track your work efficiently.

## Version control platforms

The choice between GitHub, GitLab and Bitbucket depends on your feature, privacy and other preferences, but they all are Git-based platforms for version control. While numerous detailed comparisons exist online, here we will focus on GitHub.

::: {.callout-important appearance="simple" icon="false"}
## {{< fa info-circle >}} TU Delft GitLab

TU Delft has its own [GitLab instance](https://gitlab.tudelft.nl/) hosted on campus. For more information, please visit the [documentation](https://gitlab.tudelft.nl/help) and our TU Delft GitLab guides in the [Computing Infrastracture](../../infrastructure/getting_started.md) section.
:::

Similarly, whether you are using a version control system through your terminal or IDE, or using a GUI like GitHub Desktop, the core functionality remains the same.

::: {.callout-tip appearance="simple" icon="false"}
## {{< fa lightbulb >}} Tip

GitHub Desktop is a great choice if you are just starting out with version control. It provides a user-friendly graphical interface that simplifies Git operations. It makes it easy to visualize changes, create branches, and manage pull requests without needing to use command-line Git commands.
:::

## Managing projects on GitHub

When approaching to manage your project on GitHub, you have two main options:

- a simplified approach using only issues, or
- a more structured approach using milestones and project boards. 

Both methods have their merits, and the choice depends on the size of the project, complexity, and your preferences.

You can use a simplified approach and just track your progress in the form of issues and work without defining milestones and using a project board. This can be particularly useful for smaller projects or when you are just starting out with GitHub. 

In this approach, you can:

1. Create issues for each task or feature you need to work on.
1. Optionally, use labels to categorize and prioritize your issues.
1. Assign issues to yourself or team members/collaborators.
1. Use comments to update progress and discuss any challenges.
1. Close issues as you complete them.

This method allows for a more flexible workflow while still maintaining organization and transparency in your project. As your project grows or becomes more complex, you can always transition to using milestones and project boards for more structured management.

If you plan a large piece of work in your project, it is a good idea to produce an outline of the work. Your roadmap should cover your goal and vision, and include a timeline for tasks that need to be completed. This helps yourself and your collaborators to get an understanding of what is currently happening on the project and what is coming next.

To create a roadmap, it is important to map out the key milestones, tasks needed to accomplish the milestones and related challenges.

Getting started this way would be similar to this:

1. Define a milestone.
1. Add issues to your milestone.
1. Create a project board.
1. Add issues to your project board.
1. Use task lists in your issues to break down the work.
1. When collaborating, assign people to issues.
1. Consider linking milestones, issues and pull requests to track progress.

## Issues

Issues are a fundamental component of project management on GitHub, serving as a versatile tool for tracking tasks, bugs, feature requests, and more.

::: {.callout-tip appearance="simple" icon="false"}
{{< fa lightbulb >}} Integrating issues with project boards streamlines the tracking of tasks from beginning to end, ensuring each task is closely monitored and helping you achieve your set milestones.

:::

Using GitHub issues effectively:

1. **Use descriptive titles:** Write clear, concise titles that summarize the issue. This helps others quickly understand the purpose of each issue.
1. **Provide detailed descriptions:** Include all relevant information, steps to reproduce (if you are bringing up something that is not working), and expected outcomes in the issue description. This ensures that anyone working on the issue has all the necessary context.
1. **Use labels:** Labels can help filter and sort issues; helps you categorize and prioritize issues.
1. **Assign people:** By assigning someone (or yourself) you let others know that you are picking up and working on this issue.
1. **Link related issues:** Connect related work by linking issues to provide context (add `#issue_number` to reference an issue).

You can effectively use GitHub Issues to manage your project, improve collaboration, and maintain a clear overview of your work progress. As your project(/-s) grows, you can easily transition to more structured management using milestones and project boards while still benefitting from well-organized issues.

:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn more

- [Mastering GitHub Issues](https://gitprotect.io/blog/mastering-github-issues-best-practices-and-pro-tips/)
:::


## Project boards

Project boards on GitHub are designed for planning, organizing, and tracking work within a project. They serve as visual management interfaces that integrate directly with GitHub issues and pull requests. Project boards can be configured as kanban boards, tables, or roadmaps, offering various layouts to suit different project management needs.

::: {.callout-tip appearance="simple" icon="false"}
{{< fa lightbulb >}} Project boards can be particularly useful for visualizing the overall progress of your project and identifying bottlenecks in your workflow. They provide a high-level view that complements the detailed tracking offered by issues.
:::


:::{.callout-note appearance="simple" icon="false"}
## {{< fa signs-post >}} Learn more

- **Example** - [xarray projects](https://github.com/pydata/xarray/projects?query=is%3Aopen)
- Define a [milestone](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/creating-and-editing-milestones-for-issues-and-pull-requests)
- [GitHub Guides for Issues and Projects](https://docs.github.com/en/issues/guides)
:::


## GitHub benefits for researchers and organisations

Researchers at TU Delft are eligible to receive [GitHub Educational benefits](https://github.com/education).

To qualify for the benefits, you must:

- Have a GitHub account
- Be an educator, faculty member, or researcher at a recognized educational institution
- Be able to provide documentation from your school which demonstrates your current employment status

::: {.callout-important appearance="simple" icon="false"}
## {{< fa info-circle >}}  [Application page](https://education.github.com/discount_requests/application)


:::

Moreover, *Organizations* can access a tier above the free plan. The GitHub Team plan is available at no cost for accredited educational institutions. You can view the benefits included with the Team plan [here](https://github.com/pricing).
