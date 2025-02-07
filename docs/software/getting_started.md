---
# Insert this YAML header (including the opening and closing ---) at the beginning of the document and fill it out accordingly

# We use this key to indicate the last reviewed date [manual entry, use YYYY-MM-DD]
date: 2025-02-07

# We use this key to indicate the last modified date [automatic entry]
date-modified: last-modified

# Do not modify
lang: en
language: 
  title-block-published: "Last reviewed"
  title-block-modified: "Last modified"

# Title of the document [manual entry]
title: Getting Started with Research Code

# Brief overview of the document (will be used in listings) [manual entry]
description: A guide to best practices in research coding, including version control, documentation, AI-assisted coding, and reproducibility.
hide-description: true

# Authors of the document, will not be parsed [manual entry]
author_1: Jose Carlos Urra Llanusa

# Maintainers of the document, will not be parsed [manual entry]
maintainer_1: Jose Carlos Urra Llanusa

# To whom reach out regarding the document, will not be parsed [manual entry]
corresponding: Jose Carlos Urra Llanusa

# Meaningful keywords, newline separated [manual entry]
categories: 
  - Research Software
  - Scientific Computing
  - AI in Coding
  - Reproducibility
  - Research Code Quality
  - Best Practices
  - Software Engineering for Researchers
---



# 🚀 Getting Started with Research Code: A Guide for TU Delft  

Improving research code quality doesn’t require perfection, but focusing on foundational best practices can transform your workflows. Adopt these habits progressively, and remember that even incremental improvements can significantly enhance your research impact.  

---

## 🏗️ Introduction  

### 🔬 Research Code vs. Production Code  
- **Research Code**: Typically exploratory and analysis-driven, developed with a focus on short-term results. Its structure and quality often prioritize immediate outcomes, such as data analysis and generating insights, over long-term maintainability.  
- **Production Code**: Built for stability, scalability, and maintainability, often adhering to rigorous industry-level coding standards.  

### 🎯 The Exploratory Nature of Research Code  
- Research often requires iterative experimentation, leading to quickly written code that may lack structure and documentation.  
- This approach is understandable given the goal of achieving results quickly. However, this short-term focus can hinder **reusability** and **reproducibility**.  

### 🔄 Why Code Reusability Matters  
- Reusable code ensures the continuity of scientific advancements, allowing researchers to build upon previous work.  
- Increasingly, scientific publishing demands code that meets higher standards of documentation and reproducibility to validate findings.  

---

## ⚠️ Common Challenges Researchers Face  

### 🔁 1. Reusability and Reproducibility  
- Lack of a clear structure makes code difficult to reuse for future projects or collaborators.  
- Inconsistent practices lead to challenges in reproducing results, a cornerstone of scientific integrity.  

### 📖 2. Lack of Documentation  
- Poor or absent documentation prevents others (or even the original coder) from understanding the code months or years later.  

### 🛠️ 3. Limited Code Quality  
- Non-modular, untested, or inefficient code hinders performance and scalability.  

### 🚀 4. Difficulty Scaling Up and Optimizing Computation  
- Inefficient code struggles with larger datasets or more complex simulations.  

### 🖥️ 5. Challenges with Computational Environments  
- Research code often relies on hardcoded paths, poorly managed dependencies, or specific system setups, making it difficult to run on different systems or folders.  

### ❌ Additional Challenges  
- Inconsistent naming conventions and lack of adherence to coding standards.  
- Heavy reliance on specific tools like Jupyter Notebooks, limiting modularity and scalability.  

---

## 🎯 Aiming for "Good Enough" Code Quality  

- "Good enough" quality depends on the discipline. Computationally intensive fields often demand higher standards.  
- At a minimum, researchers should aim to:  
  ✅ Use version control (e.g., Git).  
  ✅ Follow a standard folder and file naming convention.  
  ✅ Document code using inline comments and docstring standards.  
  ✅ Manage dependencies and environments effectively.  
  ✅ Write modular code and avoid excessive reliance on Jupyter Notebooks.  

---

## ❗ Bare Minimum Practices to Avoid Pain Later  

1. 🛑 **Version Control**: Without it, tracking changes and collaborating is near impossible.  
2. 🏗️ **Integrated Development Environment (IDE)**: Essential for debugging and maintaining code efficiently.  
3. 📦 **Dependency and Environment Management**: Tools like Conda or virtual environments ensure reproducibility.  
4. 📝 **Documentation**: Inline comments and consistent docstring standards make code understandable and usable.  
5. 🔄 **Standard Conventions**: Adopting naming and structuring conventions ensures consistency.  
6. 👥 **Feedback**: Test your code with others to ensure usability.  

---

## 🤖 AI in Research Code: A New Way to Learn Scientific Computing  

### 🧑‍💻 Pair Programming: How AI Changes the Game  

Traditionally, **pair programming** involves two roles:
1. **👨‍💻 The Driver**: Writes the code.  
2. **🧐 The Navigator**: Reviews, strategizes, and ensures best practices.  

With AI-assisted coding:
- The **researcher becomes more of a Navigator** 🧐  
  - Focuses on **scientific computing principles, software architecture, and performance**.  
  - Learns **how different implementations affect performance and reproducibility**.  

- **AI becomes the Driver** 🤖  
  - Handles **implementation, debugging, and refactoring** based on the researcher’s guidance.  
  - Automates repetitive or error-prone tasks.  

By taking on the **Navigator role**, researchers shift from low-level implementation to **a broader software engineering perspective**.  
This is assuming our researcher is not a computer scientist, then most likely AI can fall short in the Navigator role. As always these tools have limitations, but there are common solutions and design patterns that can be applied to many problems in research software.

---

## ✨ Final Thoughts  

AI in coding is **not just a shortcut**—it’s an opportunity for **learning and conceptual enrichment**. By using AI as a **pair programming partner**, researchers can:  
✅ **Develop better research code** that is structured and maintainable.  
✅ **Improve scientific reproducibility** by writing better-documented and optimized code.  
✅ **Shift to a more strategic role** in software development.  

By embracing **AI responsibly**, researchers can ensure their code contributes meaningfully to **scientific progress**. 🚀  
