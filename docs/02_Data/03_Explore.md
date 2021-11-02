# Exploring the data
> This is also known as exploratory data analysis

Now during the exploration phase, we try to understand what patterns and values our data has. We’ll be using different types of visualizations and statistical testings to back up our findings.

**Objective:**
- Find patterns in your data through visualizations and charts
- Extract features by using statistics to identify and test significant variables

**Skills Required:**
- Python: Numpy, Matplotlib, Pandas, Scipy
- R: GGplot2, Dplyr
- Inferential statistics
- Experimental Design
- Data Visualization

```{note}
Tip: Have your “spidey senses” tingling when doing analysis. Have the sense to spot weird patterns or trends.
Design consideration: Most of the time people just go straight to the visual “lets get it done”. It’s all about the end user who will be interpreting it. Focus on your audience.
```

Visualizing, clustering, performing dimensionality reduction: these are all part of `looking at data.’ These tasks are sometimes described as “exploratory” in that no hypothesis is being tested, no predictions are attempted. Wolfgang Pauli would call these techniques “not even wrong,” though they are hugely useful for getting to know your data. Often such methods inspire predictive analysis methods used later. Tricks to know:

- You can see a lot by looking at your data. Zoom out if you need to, or use unix’s head to view the first few lines, or awk or cut to view the first few fields or characters.
- Single-feature histograms visually render the range of single features and their distribution. Since histograms of real-valued data are contingent on choice of binning, we should remember that they an art project rather than a form of analytics in themselves.
- Similarly, simple feature-pair scatter plots can often reveal characteristics of the data that you miss when just looking at raw numbers.
- Dimensionality reduction (MDS, SVD, PCA, PLS etc): Hugely useful for rendering high-demensional data on the page. In most cases we are performing ‘unsupervised’ dimensionality reduction (as in PCA), in which we find two-dimensional shadows which capture as much variance of the data as possible. Occasionally, low-dimensional regression techniques can provide insight, for example in this review article describing the Netflix Prize which features a scatterplot of movies (Fig. 3) derived from a regression problem in which one wishes to predict users’ movie ratings.
- Clustering: Unsupervised machine learning techniques for grouping observations; this can include grouping nodes of a graph into “modules” or “communities”, or inferring latent variable assignments in a generative model with latent structure (e.g., Gaussian mixture modeling, or K-means, which can be derived via a limiting case of Gaussian mixture modeling).