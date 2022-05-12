# Modeling and Machine Learning
> “Models are opinions embedded in mathematics” — Cathy O’Neil

Predictive Power Example: One great example can be seen in Walmart’s supply chain. Walmart was able to predict that they would sell out all of their Strawberry Pop-tarts during the hurricane season in one of their store location. Through data mining, their historical data showed that the most popular item sold before the event of a hurricane was Pop-tarts. As crazy it sounds, this is a true story and brings up the point on not to underestimate the power of predictive analytics.

Now comes the fun part. Models are general rules in a statistical sense.Think of a machine learning model as tools in your toolbox. You will have access to many algorithms and use them to accomplish different business goals. The better features you use the better your predictive power will be. After cleaning your data and finding what features are most important, using your model as a predictive tool will only enhance your business decision making.

> Predictive Analytics is emerging as a game-changer. Instead of looking backward to analyze “what happened?” Predictive analytics help executives answer “What’s next?” and “What should we do about it?” (Forbes Magazine, April 1, 2010)

**Objective:**

- In-depth Analytics: create predictive models/algorithms
- Evaluate and refine the model

**Skills Required:**
- Linear algebra & Multivariate Calculus
- Machine Learning: Supervised/Unsupervised algorithms
- Evaluation methods
- Machine Learning Libraries: Python (Sci-kit Learn) / R (CARET)


## Models: always bad, sometimes ugly
Whether in the natural sciences, in engineering, or in data-rich startups, often the ‘best’ model is the most predictive model. E.g., is it 'better’ to fit one’s data to a straight line or a fifth-order polynomial? Should one combine a weighted sum of 10 rules or 10,000? One way of framing such questions of model selection is to remember why we build models in the first place: to predict and to interpret. While the latter is difficult to quantify, the former can be framed not only quantitatively but empirically. That is, armed with a corpus of data, one can leave out a fraction of the data (the “validation” data or “test set”), learn/optimize a model using the remaining data (the “learning” data or “training set”) by minimizing a chosen loss function (e.g., squared loss, hinge loss, or exponential loss), and evaluate this or another loss function on the validation data. Comparing the value of this loss function for models of differing complexity yields the model complexity which minimizes generalization error. The above process is sometimes called “empirical estimation of generalization error” but typically goes by its nickname: “cross validation.” Validation does not necessarily mean the model is “right.” As Box warned us, “all models are wrong, but some are useful”. Here, we are choosing from among a set of allowed models (the `hypothesis space’, e.g., the set of 3rd, 4th, and 5th order polynomials) which model complexity maximizes predictive power and is thus the least bad among our choices.

Above we mentioned that models are built to predict and to interpret. While the former can be assessed quantitatively ('more predictive' is 'less bad’) the latter is a matter of which is less ugly, and is in the mind of the beholder. Which brings us to…