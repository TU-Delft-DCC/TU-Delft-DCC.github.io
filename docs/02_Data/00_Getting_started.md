# Getting started 
- Learn basic concepts to work with data
- Understand the background 
- Understand the skills associated to working with data

When it comes to data, there are two main groups of activities that are quite generic in research: 
- 1. Working with data, 
- 2. Publishing the data as part your research (this mostly known as research data)**. 

In this guide we aim to give you a compact overview of aspects, considerations and things to keep in mind if you are planning to work with large or potenitially large volumes of data. 


## Publishing (FAIR) data
Lets start at the end. Lets assume you have data to share with your scientific community and you want to make it in such a way that is as impactful and useful as possible. This implies you want your data to be compliant with FAIR principles/criteria.

![](https://www.openaire.eu/images/Guides/EC_FAIR_data.png)

## Working with data in research
Science has been widely impacted by software development practices, computer science and data science. The **OSEMN (Obtain, Scrub, Explore, Model, Interpret) framework** for data science has been widely adopted since the concept was introduced in 2010. It is not the only framework out there, but we will work with OSEMN for the simple reason that it's easy to remember. 

### Context and goals come first
> A problem well stated is a problem half-solved.

Start with the end in mind, that gives  a standard to evaluate the decisions to be made on the way to get there. (Then go from a plan A to a plan that works :)) Otherwise, we you run the risk of deciding that decisions are good just because they work with the dataset that we've found. 

We should be in the business of building models that solve problems, not inventing problems that our models happen to solve.

Bare in mind that in the context of science, data is diverse, specific and domain focused, therefore aligning with your field and understanding the specifics of your domain is crucial. Always rely on your community, find champions in your field (or similar fields) and learn from them.

### Start with an abstract or design
In ["OSEMN is Awesome, but AOSEMN is Awesomer"](https://datasciencemvp.com/articles/2019/04/16/aosemn/), Cliff Clive, gives great tips on how to start a data science research project by writing an abstract: 

> At the start of your project, you won't be able to summarize the work you haven't done yet. But you should be able to put together ideas for most of these questions. And putting some thought into spelling out how you will know when you've got an answer is going to be extremely helpful for establishing the right perspective at the beginning.

> A good abstract should answer these questions:

> - **End User:** who has this problem and what are their needs?
> - **Problem Statement:** what are you trying to solve?
> - **Motivation:** why does this problem matter and how will our results meet that need?
> - **Approach:** what data should be useful for solving the problem and what kinds of models will able to turn the data into a solution?
Results: what will our model output look like and how can we put it to use?
>- **Conclusions:** once we have our results, how can we evaluate them to show that the model is working?

> If we can provide well thought out answers to the first three questions, and provide a plan and conditions for success for the last three, we are setting ourselves up for a quick and effective workflow.

::: info

This is also a great start for a data management plan by the way 

:::

### OSEMN
![](https://s2.research.com/wp-content/uploads/2020/07/24110111/data-science-process-1.jpg)

1. Obtaining, storing and using/analyzing data
2. Scrub data
3. Explore data
4. Model data
5. Interpret results

The following sections try to give you an overview of these different steps, but also basic skills you would need to go through them, and some examples of more advanced or complex scenarios. 

## References
[1]J. Brownlee, “How To Work Through A Problem Like A Data Scientist,” Machine Learning Mastery, Dec. 18, 2014. https://machinelearningmastery.com/how-to-work-through-a-problem-like-a-data-scientist/ (accessed Oct. 25, 2021).

[2]“Snapshot.” Accessed: Oct. 25, 2021. [Online]. Available: https://machinelearningmastery.com/how-to-work-through-a-problem-like-a-data-scientist/


[3]“Data Science Curriculum for self-study,” KDnuggets. https://www.kdnuggets.com/data-science-curriculum-for-self-study.html/ (accessed Oct. 25, 2021).

[4]“Snapshot.” Accessed: Oct. 25, 2021. [Online]. Available: https://www.kdnuggets.com/2020/02/data-science-curriculum-self-study.html

[5]“dataists » A Taxonomy of Data Science.” http://www.dataists.com/2010/09/a-taxonomy-of-data-science/ (accessed Oct. 25, 2021).

[6]“Snapshot.” Accessed: Oct. 25, 2021. [Online]. Available: http://www.dataists.com/2010/09/a-taxonomy-of-data-science/

[7]C. Byrne, “Development Workflows for Data Scientists,” p. 28.
              
[8]“Byrne - Development Workflows for Data Scientists.pdf.” Accessed: Oct. 29, 2021. [Online]. Available: https://resources.github.com/downloads/development-workflows-data-scientists.pdf

[9]H. Laser et al., “Data Science as a Service - Prototyping an integrated and consolidated IT infrastructure combining enterprise self-service platform and reproducible research (In: International Journal On Advances in Software, ISSN 1942-2628),” vol. 13, pp. 104–115, Jul. 2020.

[10]“Full Text PDF.” Accessed: Oct. 25, 2021. [Online]. Available: https://www.researchgate.net/profile/Svetlana-Gerbel/publication/341234847_Data_Science_as_a_Service_-_Prototyping_an_integrated_and_consolidated_IT_infrastructure_combining_enterprise_self-service_platform_and_reproducible_research_In_International_Journal_On_Advances_in_So/links/5f07115fa6fdcc4ca459b678/
Data-Science-as-a-Service-Prototyping-an-integrated-and-consolidated-IT-infrastructure-combining-enterprise-self-service-platform-and-reproducible-research-In-International-Journal-On-Advances-in-So.pdf

[11]“ResearchGate Link.” Accessed: Oct. 25, 2021. [Online]. 
Available: https://www.researchgate.net/publication/341234847_Data_Science_as_a_Service_-_Prototyping_an_integrated_and_consolidated_IT_infrastructure_combining_enterprise_self-service_platform_and_reproducible_research_In_International_Journal_On_Advances_in_So

[12]C. Clive, “OSEMN is Awesome, but AOSEMN is Awesomer,” Data Science MVP, Apr. 16, 2019. https://datasciencemvp.com/articles/2019/04/16/aosemn/ (accessed Oct. 29, 2021).

[13]R. Lao, “A Beginner’s Guide to the Data Science Pipeline,” Medium, Dec. 19, 2019. https://towardsdatascience.com/a-beginners-guide-to-the-data-science-pipeline-a4904b2d8ad3 (accessed Oct. 25, 2021).

[14]“Snapshot.” Accessed: Oct. 25, 2021. [Online]. Available: https://towardsdatascience.com/
a-beginners-guide-to-the-data-science-pipeline-a4904b2d8ad3

[15]“data-science-process-1.jpg (1020×800).” https://s2.research.com/wp-content/uploads/2020/07/24110111/data-science-process-1.jpg (accessed Oct. 29, 2021).

[16]“OSEMN is Awesome, but AOSEMN is Awesomer - Data Science MVP.” https://datasciencemvp.com/articles/2019/04/16/aosemn/ (accessed Oct. 29, 2021).

[17]“What is a Data Pipeline? Process and Examples,” Stitch. https://www.stitchdata.com/resources/what-is-data-pipeline/ (accessed Oct. 25, 2021).

[18]“Snapshot.” Accessed: Oct. 25, 2021. [Online]. Available: https://www.stitchdata.com/resources/what-is-data-pipeline/












