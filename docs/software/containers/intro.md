---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
date: 2025-02-28

# We use this key to indicate the last modified date [automatic entry]
date-modified: last-modified

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
title: Introduction to containers

# Short description of the document, will be used in the listing
description: Containers are a way to package software and its dependencies into a single unit that can run consistently across different environments.
hide-description: true

# Authors of the document, will not be parsed [manual entry]
-author_1: Elviss Dvinskis
-author_2: Maurits Kok
-author_3: Jose Carlos Urra Llanusa

# Maintainers of the document, will not be parsed [manual entry]
#maintainer_1:
#maintainer_2:

# To whom reach out regarding the document, will not be parsed [manual entry]
corresponding: Elviss Dvinskis

# Meaningful keywords, newline separated [manual entry]
categories: 
 - Containers
 - Reproducibility

---

# 🚢 Introduction to Containers

> Ensuring reproducibility in research is paramount. A key criteria for success is to avoid as much human intervention as possible when reproducing computational environments. **Containers** offer a robust solution for more complex and dependency-heavy software, allowing you to package its environment into a single, portable unit. 🎯

## 🎯 Key Use Cases for Containers in Researchers

1. **Short-Term Reproducibility and Portability:** 🛠 Share and run applications seamlessly across different systems without compatibility issues. Do you struggle with colleagues reproducing your code, even when your dependencies are well documented?
2. **Long-Term Preservation:** 🏛 Preserve the exact computational environment to reproduce analyses years later. How would someone reproduce the code in a paper you published 20 years from now with different OS, machine, etc?
3. **Continuous Integration and Deployment (CI/CD):** 🚀 Automate testing and deployment processes to maintain consistency across various environments. Do you struggle with reinstalling an application, scheduler, or new code in a server that needs to run? Do you currently do it manually?

::: {.callout-tip}
### Why Use Containers?
- 🏗 **Encapsulate** dependencies, ensuring consistent software execution.
- 🔄 **Minimize setup time** by eliminating the need for manual installations.
- 🚀 **Enable reproducibility** across different machines and operating systems.
- 🏛 **Preserve environments** to ensure results remain valid even years later.
:::

## 📦 Short-Term Reproducibility and Portability

> Sharing research often involves complex setups. Containers encapsulate the entire environment, allowing others to replicate results without intricate installations.

### **The Most Basic Research Use Case: Code & Data Publishing**

📄 **Scenario:** You publish a research paper that includes code, data, and analysis. Without proper environment control, reproducing the results might be difficult due to dependency mismatches.

✅ **Solution:** You can create a **container image** (a snapshot of your computational environment) that includes:

- The **operating system** 🖥 (specific Linux distribution)
- The **programming language** and its version 📌
- Required **libraries and dependencies** 📚
- Your **code and dataset** 📊

Example Tool: Binder allows researchers to create a containerized environment from a GitHub repository, enabling seamless sharing and execution.

### **High-Performance Computing (HPC) Clusters**

Some HPC clusters support containers, allowing users to reproduce complex environments seamlessly. Instead of manually setting up dependencies on an HPC cluster, researchers can package their software into a container and run it directly on the cluster. This eliminates compatibility issues and ensures that the same environment used in development is available during execution on the HPC system.

Popular containerization tools for HPC environments include **Apptainer** (previously Singularity), which provides a secure and scalable way to run containers in environments where Docker may not be supported due to security concerns.

This ensures that all necessary dependencies, including system libraries and hardware drivers, are encapsulated in a portable environment that can be deployed across different HPC clusters.

::: {.callout-caution}
#### When Containers Might Be Overkill
- 🔹 Simple scripts that require minimal dependencies.
- 🔹 Well-documented software that can be installed easily using package managers like Conda or pip.
- 🔹 Situations where a virtual environment is sufficient (e.g., Python's `venv`).
:::

## 🏛️ Long-Term Preservation

> Over time, software dependencies and environments evolve, posing challenges to reproducibility. Containers freeze the computational environment, ensuring that analyses can be rerun accurately in the future.

### **Why Containers Ensure Long-Term Reproducibility**

🕰️ Unlike Conda or pip environments, which rely on external repositories that may change or disappear, **container images are self-contained**. This guarantees:

- 🎯 **Exact replication** of results even 10 or 20 years later.
- 🚀 **Environment stability** without worrying about software updates or deprecations.
- 🔗 **Complete portability** across different computing infrastructures.

### **Jupyter Notebooks and Web Application Stacks**

🖥️ Many researchers rely on **Jupyter Notebooks** to conduct and document their analyses. Jupyter is a **complex web application stack** that includes:

- 📡 **A server-side service** that manages notebook execution.
- 🖥 **A frontend interface** that allows users to interact with their computations.
- 🐍 **Python-based interactive environments** with rich visualization capabilities.

📄 **Scenario:** A climate scientist packages their **data analysis pipeline and Jupyter Notebook** inside a container. Running the container doesn't just reproduce the analysis, but also:

- Ensures that **Python and all required dependencies** (NumPy, Pandas, Matplotlib, etc.) are properly installed.
- Preserves **OS-level dependencies** such as shared libraries that Python packages may require.
- Allows future researchers to **interactively explore and modify the computations** within a controlled, identical environment.

## ☁️ Advanced Use: Cloud Computing and Containers

The cloud is inherently **container-friendly** as it is built on the principle of virtualization. Cloud platforms such as AWS, Google Cloud, and Microsoft Azure provide seamless integration with containerized applications, enabling:

- 🚀 **Easy deployment of research applications** on scalable infrastructure.
- 📦 **Portability** between different cloud providers and on-premise setups.
- ⏳ **Efficient use of resources**, reducing the cost of maintaining complex software environments.

For advanced users, running containers in the cloud allows for efficient orchestration of machine learning models, data pipelines, and large-scale simulations without having to worry about system compatibility issues.

## 🚀 Conclusion

While containers provide powerful tools for reproducibility and automation, there is a **learning curve** associated with their use. Many researchers manage just fine with simpler environment management tools. **Only invest in containers when software complexity and runtime require it**—if you find yourself struggling with reproducing, redeploying, or maintaining software, containers may provide a significant advantage.

That said, you can also learn containerization for fun! But always remember: **make things as simple as possible and only as complex as necessary**. 🚀

## 📚 Further Reading

- [Docker Documentation](https://docs.docker.com)
- [Apptainer User Guide](https://apptainer.org/docs/)
- [Binder Project](https://mybinder.org/)
- [AWS Containers](https://aws.amazon.com/containers/)
- [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine)
- [Azure Container Instances](https://azure.microsoft.com/en-us/products/container-instances/)

---
💡 *By adopting containers, researchers and developers can enhance the reproducibility, portability, and longevity of their projects.* 🚀

