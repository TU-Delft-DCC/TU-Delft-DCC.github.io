## Getting started
```{note}
 The following content have been copied as is from the  [Aalto scientific computing website](https://scicomp.aalto.fi/scicomp/zen-of-scicomp/#what-aspects-can-you-improve)
```

## Production code vs research code
Yes, many things about software development may not apply to you:

### Production code:
- you sort of know what the target is
- code is the main result
- must be maintainable for the future

### Research code:
- you don't know what the target is
- code is secondary

But research code *often becomes important in the future*, so not all can be an unmaintainable mess...



Research code pyramid
---------------------

I know that *not all* research code will be perfect.
But if you don't build on a good base, you will end up with misery.


```{figure} ../../img/zen-of-scicomp-pyramid.svg
---
---
The zen of scientific computing
```

```{figure} ../../img/zen-of-scicomp-tower.svg
---
---
Unstable research software
```

```{figure} ../../img/zen-of-scicomp-block.svg
---

---
Inneficient and overwhelming approach to software
```


Yes, you can't do everything perfectly
--------------------------------------

Not everything you do will be perfect.  But it has to be good enough
to:

* be correct
* be changed without too much difficulty
* be run again once reviews come in
* ideally, not wasted once you do something new
* .. and sometimes, becomes important and evolve

Even as a scientist, you need to know the levels of maturity so that
you can do the right thing *for your situation*.

It takes skill and practice to do this right.  *But it is part of
being a scientist.*

This talk's outline:

* Describe different factors that influence code quality
* Describe what the maturity levels are and when you might need them



What aspects can you improve?
-----------------------------

Below are many different aspects of scientific computing which you can
improve.

Some are good for everyone.  Some you may not need yet.  Different
levels of maturity are presented for each topic, so that you can
think about what is *right for you*.



Version control
---------------

Version control allows you to track changes and progress.

For example, you can figure out what you just broke or when you
introduced a bug.  You can always go back to other versions.

Version control is essential to *any* type of collaboration.

* L0: no version control
* L1: local repo, just commit for yourself
* L2: shared repo, multiple collaborators push directly
* L3: shared repo, pull-request workflow

Resources:
- [Github](https://github.com)
- [TU Delft gitlab](https://gitlab.tudelft.nl)
- [Code refinery lessons, git intro](https://coderefinery.github.io/git-intro/)


<!-- * `Github <https://github.com>`__, `CodeRefinery Gitlab <https://coderefinery.org/repository/>`__,
  your institution's equivalent, and many more.
* `CodeRefinery <https://coderefinery.org>`__ lessons, `git-intro
  <https://coderefinery.github.io/git-intro/>`__ and
  `git-collaborative <https://coderefinery.github.io/github-without-command-line/>`__)
* Software Carpentry `Git-novice lesson <https://swcarpentry.github.io/git-novice/>`__ -->


Modular code
------------

Modularity is one of the basic prerequisites to be able to understand,
maintain, and reuse things - and also hard to get right at the beginning.

Don't worry too much, but always think about how to make things
reusability.

* L0: bunch of copy-and-paste scripts
* L1: important code broken out into functions
* L2: separation between well-maintained libraries and daily working
  scripts.

Resources:
- [CodeRefinery](http://cicero.xyz/v3/remark/0.14.0/github.com/coderefinery/modular-code-development/master/talk.md)



Organized workspaces
--------------------

You will need to store many files.  Are they organized, so that you
can find them later, or will you get lost in your own mess?

* L0: no particular organization system
* L1: different types of data separated (original
  data/code/scratch/outputs)
* L2: projects cleanly separated, named, and with a purpose



Workflow/pipeline automation
----------------------------

When you are doing serious work, you can't afford to just manage stuff
by hand.  Task automation allows you to do more faster.

Something such as ``make`` can automatically detect changed input
files and code and automatically generate the outputs.

* L0: bunch of scripts you have to run and check output of by hand.
* L1: hand-written management scripts, each output can be traced to
  its particular input and code.
* L2: ``make`` or other workflow management tool to automate things.
* L3: Full automation from original data to final figures and data

Resources:

- [CodeRefinery Reproducible Research lesson](https://coderefinery.github.io/reproducible-research/)



Reproducibility of environment
------------------------------

Is someone else able to (know and) install the libraries needed to run
your code?  Will a change in another package break your code?

Scientific software is notoriously bad at managing its dependencies.

* L0: no documentation
* L1: state the dependencies somewhere, tested to ensure they work
* L2: pin exact versions used to generate your results
* L3: containerized workflow or equivalent

Resources:

- [CodeRefinery Reproducible Research lesson](https://coderefinery.github.io/reproducible-research/)



Documentation
-------------

If you don't say what you do, there's no way to understand it.  **You**
won't be able to understand it later, either.

At minimum, there should be some README files that explain the big
picture.  There are fancier systems, too.

* L0: nothing except scattered code comments
* L1: script-level comments and docstrings explaining overall logic
* L2: simple README files explaining big picture and main points
  [example](https://version.aalto.fi/gitlab/afof/tracing-products/-/tree/master)
* L3: dedicated documenentation including tutorials, reference, etc.

Resources:

* [CodeRefinery Documentation lesson](https://coderefinery.github.io/documentation/)



Testing
-------

You have to test your code at least once when you first run it.  How
do you know you don't break something later?

Testing gives you a way to ensure things always work (and are correct)
in the future by letting you run *every* test automatically.

There's nothing more liberating than knowing "tests still pass, I
didn't break anything".  It's extremely useful for debugging, too.

* L0: ad-hoc and manually
* L1: defensive programming (assertions), possibly some test data and
  scripts
* L2: structured, comprehensive unit/integration/system tests (e.g. ``pytest``)
* L3: continuous integration testing on *all* commits  (e.g. Github Actions)

If code is easy to test, it is *usually* easy to reuse, too.
Furthermore, making code testable makes it reusable.

Resources:

* [CodeRefinery Testing lesson](https://coderefinery.github.io/testing/)
* [GitHub Actions](https://github.com/features/actions)


Licensing
---------

You presumably want people to use your work so they will cite you.  If
you don't have a license, they won't (or they might and not tell anyone).

Equally, you want to use other people's work.  You need to check their
licenses.

* L0: no license given / copy and paste from other sources
* L1: license file in repo / careful to not copy incompatible code
* L2: license tracked per-file and all contributors known.

Resources:

* [CodeRefinery Software social coding ](http://cicero.xyz/v3/remark/0.14.0/github.com/coderefinery/social-coding/master/talk.md))
* https://choosealicense.com/



Distribution
------------

Code can be easy to reuse, but not easy to get.  Luckily there are
good systems for sharing code.

* L0: code not distributed
* L1: code provided only if someone asks
* L2: code on a website
* L3: version control system repo is public
* L4: packaged, tagged, and versioned releases

Resources:

* [Python: Packaging tutorial](https://packaging.python.org/tutorials/packaging-projects/)
* Similar for any other language you may use


Reuse
-----

Are you aware of what what others have already figured out through
their great effort?

Choosing the right thing to build off of is not always easy, but you must

* L0: reinvent everything yourself
* L1: use some existing tools and libraries
* L2: deep study of existing solutions and tools, reuse them when appropriate

Resources:

* I don't know where to refer you to right now.



Collaboration
-------------

Is science like monks working in their cells, or a community effort?

These skills move so fast that learning peer-to-peer is one of the
best ways to do it.

There's a whole other art of applying these skills which isn't taught
in classes.

If you don't work together, you will fall behind.


* L0: you work alone and re-invent everything
* L1: you occasionally talk about results or problems
* L2: collaborative package development
* L3: code reviews, pair programming, etc.
* L4: community project welcoming other contributors

Resources:

* [Most every CodeRefinery lesson](https://coderefinery.org/lessons/)
* Plenty more



The future
----------

Science with computers can be extremely enjoyable... or miserable.

We are here to help you.  You are here to others.

Will we?
