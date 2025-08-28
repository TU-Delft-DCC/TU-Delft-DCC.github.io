# Accessibility & Reproducibility
```{note}
 The following content have been copied as is from the utrecht university github repository called ["Best practices in Writing reproducible code](https://utrechtuniversity.github.io/workshop-computational-reproducibility/docs/index.html). Retrieved on September, 2021.
```
Last but not least, let's make our code accessible for others! 

The following topics are covered:
* obtaining a doi and ensuring accessibility
* dealing with requirements and dependencies

Here are your last videos and accompanying exercises. 
Watch the video, then apply the exercises to your own project. 
Use the slides linked above for reference, and be sure to ask for help when you need it!

## Dependencies

### Video
<iframe src="https://player.vimeo.com/video/464028630" width="100%" height="400px">
</iframe>
<!-- ```{r}
vembedr::embed_url("https://vimeo.com/464028630")
``` -->

### Slides
<iframe src="../../slides/slides_reproducibility.html#3" width="100%" height="400px">
</iframe>
<!-- ```{r}
knitr::include_url("../../slides/slides_reproducibility.html#3")
``` -->


### Exercise
Address dependencies and language versions in your README.
- What version of your coding language is required?
- Which packages does a user need to install before running your project?
  What versions?
- Can you provide their installation instructions?


## Binder

### Video
<iframe src="https://player.vimeo.com/video/464010497" width="100%" height="400px">
</iframe>
<!-- ```{r}
vembedr::embed_url("https://vimeo.com/464010497")
``` -->

### Exercise (optional)

**For R**

- Generate a file called `runtime.txt`, either in the root of your project, or in a (hidden) folder called `.binder/`.
- Write in the file: `r-2020-10-02` -- or specify the R version with `r-3.6-2020-10-02`.
- Write a file called `install.R`, in `.binder/` or in root, and use it to write install code for your packages, e.g.:
  ```
  install.packages("ggplot2")
  install.packages("dplyr")
  ```
- Binderise your project by following the instructions via [mybinder.org](https://mybinder.org/)

**For Python**

Binder automatically loads Python 3.6.

- Add dependencies to your binder in the requirements.txt file like this:
  ```
  numpy==1.14.5
  pandas==1.1.2
  ```
- Binderise your project by following the instructions via [mybinder.org](https://mybinder.org/)


## Archiving

### Video
<iframe src="https://player.vimeo.com/video/463947879" width="100%" height="400px">
</iframe>
<!-- ```{r}
vembedr::embed_url("https://vimeo.com/463947879")
``` -->

### Slides
<iframe src="../../slides/slides_reproducibility.html#7" width="100%" height="400px">
</iframe>
<!-- ```{r}
knitr::include_url("../../slides/slides_reproducibility.html#7")
``` -->

### Exercise (optional)

- Follow the workflow [outlined in this guide](https://guides.github.com/activities/citable-code/) to archive your code to Zenodo.
  Use the [Sandbox version of Zenodo](http://sandbox.zenodo.org/) to make sure your repository is not actually archived permanently!