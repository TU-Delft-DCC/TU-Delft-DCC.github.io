# Interpreting and Storytelling

“If you can’t explain it to a six year old, you don’t understand it yourself.” — Albert Einstein

**Objective:

Identify business insights: return back to business problem
Visualize your findings accordingly: keep it simple and priority driven
Tell a clear and actionable story: effectively communicate to non-technical audience
Skills Required:

Business Domain Knowledge
Data Visualization Tools: Tablaeu, D3.JS, Matplotlib, GGplot, Seaborn
Communication: Presenting/Speaking & Reporting/Writing

It’s story time! The most important step in the pipeline is to understand and learn how to explain your findings through communication. Telling the story is key, don’t underestimate it. It’s about connecting with people, persuading them, and helping them. The art of understanding your audience and connecting with them is one of the best part of data storytelling.

“I believe in the power of storytelling. Stories open our hearts to a new place, which opens our minds, which often leads to action” — Melinda Gates

Emotion plays a big role in data storytelling. People aren’t going to magically understand your findings. The best way to make an impact is telling your story through emotion. We as humans are naturally influenced by emotions. If you can tap into your audiences’ emotions, then you my friend, are in control. When you’re presenting your data, keep in mind the power of psychology. The art of understanding your audience and connecting with them is one of the best part of data storytelling.

Best Practice: A good practice that I would highly suggest to enhance your data storytelling is to rehearse it over and over. If you’re a parent then good news for you.Instead of reading the typical Dr. Seuss books to your kids before bed, try putting them to sleep with your data analysis findings! Because if a kid understands your explanation, then so can anybody, especially your Boss!

Consider the task of automated digit recognition. The value of an algorithm which can predict ‘4’ and distinguish from ‘5’ is assessed by its predictive power, not on theoretical elegance; the goal of machine learning for digit recognition is not to build a theory of ‘3.’ However, in the natural sciences, the ability to predict complex phenomena is different from what most mean by ‘understanding’ or ‘interpreting.’

The predictive power of a model lies in its ability to generalize in the quantitative sense: to make accurate quantitative predictions of data in new experiments. The interpretability of a model lies in its ability to generalize in the qualitative sense: to suggest to the modeler which would be the most interesting experiments to perform next.

The world rarely hands us numbers; more often the world hands us clickstreams, text, graphs, or images. Interpretable modeling in data science begins with choosing a natural set of input features — e.g., choosing a representation of text in terms of a bag-of-words, rather than bag-of-letters; choosing a representation of a graph in terms of subgraphs rather than the spectrum of the Laplacian. In this step, domain expertise and intuition can be more important than technical or coding expertise. Next one chooses a hypothesis space, e.g., linear combinations of these features vs. exponentiated products of special functions or lossy hashes of these features’ values. Each of these might have advantages in terms of computational complexity vs interpretability. Finally one chooses a learning/optimization algorithm, sometimes including a “regularization” term (which penalizes model complexity but does not involve observed data). For example, interpretability can be aided by learning by boosting or with an L1 penalty to yield sparse models; in this case, models which can be described in terms of a comprehensible number of nonzero weights of, ideally, individually-interpretable features. Rest assured that interpretability in data science is not merely a desideratum for the natural scientist.

Startups building products without the perspective of multi-year research cycles are often both exploring the data and constructing systems on the data at the same time. Interpretable models offer the benefits of producing useful products while at the same time suggesting which directions are best to explore next.

For example, at bit.ly, we recently completed a project to classify popular content by click patterns over time and topic. In most cases, topic identification was straightforward, e.g., identifying celebrity gossip (you can imagine those features!). One particular click pattern was difficult to interpret, however; with further exploration we realized that people were using bit.ly links on images embedded in a page in order to study their own real-time metrics. Each page load counted as a ‘click’ (the page content itself was irrelevant), and we discovered a novel use case ‘in the wild’ for our product.