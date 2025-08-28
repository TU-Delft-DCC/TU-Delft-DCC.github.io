# Code Quality
```{note}
 The following content have been copied as is from the utrecht university github repository called ["Best practices in Writing reproducible code](https://utrechtuniversity.github.io/workshop-computational-reproducibility/docs/index.html). Retrieved on September, 2021.
```
Let's start making our code readable and reusable!

This section covers the following topics:

* code readability
* reusable code
* defensive programming

Like the previous chapter, we have 3 short videos and accompanying exercises. 
Watch the video, then apply the exercises to your own project.
**Note:** these exercises get you to work on your code in detail.
Depending on how many issues you discover, it may take some time to refactor your code.
Today, focus on identifying issues, and mark them with #TODO or equivalent, so you can find them later.
**We recommend spending a maximum of 20 minutes on each exercise.**
However, if you have time, do get started with refactoring your code!
While code refactoring can be a time consuming exercise, it is also a great way to learn from your past mistakes, up your coding game, and significantly improve your code at the same time.

_Tip! Use #TODO or //TODO (depending on your comment marker) to easily find your tasks later on. Many IDEs extract these into a task list!_

The slides are linked below for reference, and be sure to ask for help when you need it!

## Readability

### Video
<iframe src="https://player.vimeo.com/video/463572640" width="100%" height="400px">
</iframe>
<!-- ```{r}
vembedr::embed_url("https://vimeo.com/463572640")
``` -->

### Slides
<iframe src="../../slides/slides_code-quality.html#3" width="100%" height="400px">
</iframe>
<!-- ```{r}
knitr::include_url("../../slides/slides_code-quality.html#3")
``` -->

### Exercise
- Use a linter to run through your code and identify style issues.
- Edit your code to improve the style compatibility, based on the feedback from your linter.
  If you work with Python, consider applying [autopep8](https://pypi.org/project/autopep8/) to automatically fix linting issues.
- For the R users: a course participant found [styler](https://styler.r-lib.org/), which may do the same for R!
- If you find code that is hard to read, or variable names that need adjusting, make a note to work on it.
  (Again, use #TODO or another consistent label!)

## Reusability

### Video
<iframe src="https://player.vimeo.com/video/463647105" width="100%" height="400px">
</iframe>
<!-- ```{r}
vembedr::embed_url("https://vimeo.com/463647105")
``` -->

### Slides
<iframe src="../../slides/slides_code-quality.html#12" width="100%" height="400px">
</iframe>
<!-- ```{r}
knitr::include_url("../../slides/slides_code-quality.html#12")
``` -->

### Exercise

Visualize your code.
- Use yellow for scripted code, purple for structured code (for-loops, functions, etc.), and green for comments
- Use any tool that works for you (powerpoint, word, paint, or good old pencils and paper)
- During this exercise, try to identify yellow parts that can be structured and turned into (a) function(s). Label them, or rewrite them if you have time.
- Make a screenshot or picture of your visualization, and share it on Teams!

## Robustness

### Video
<iframe src="https://player.vimeo.com/video/463647105" width="100%" height="400px">
</iframe>
<!-- ```{r}
vembedr::embed_url("https://vimeo.com/463647105")
``` -->

### Slides
<iframe src="../../slides/slides_code-quality.html#21" width="100%" height="400px">
</iframe>
<!-- ```{r}
knitr::include_url("../../slides/slides_code-quality.html#21")
``` -->

### Exercise

- Identify assumptions in your code
  - What assumptions/expectations exist on your data or (user) input?
  - What assumptions/expectations exist on the input of (a) function(s)?

Based on the assumptions/expectations you were able to identify, work on increasing the robustness of your code.
Choose one:
- Make the input/data assumptions explicit
  - Option 1: Explicitly state assumptions on data or input in your README.md.
  - Option 2: Write a piece of code that tests the validity of data/input, and reports an error if the expectations are not met.
- Test the input for a function. Modify the code inside your function to:
  - check the value of the arguments passed to your function using if/else statements;
  - raise an error in case an argument is out of the range of acceptable values.
