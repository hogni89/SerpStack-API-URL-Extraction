## Introduction
With trillions of bytes of data getting produced every day, Industries are looking forward to using these data to gain more and more insights that can help them grow exponentially. Thus, there is an ever-growing demand for Machine Learning Engineers and Data Scientists who can analyze textual data and do Natural Language Processing using state-of-the-art tools to uncover valuable information from the raw data. In this article, we are going to read about one such advanced Python package named TextBlob that is used for performing NLP tasks and use it to perform text classification using Decision Trees in Python.
## What is classification in Machine Learning?
Before we proceed, we must understand what classification means in terms of Machine Learning. Classification is a task where we build a predictive model that can separate entities into separate groups/classes based on their respective labels.  
## What are Decision Trees?
Decision Trees are one of the most powerful and widely used machine learning algorithm that is based on the supervised learning approach. As the name suggests a decision tree is a prediction model structured in the form of a tree that is built using recursive splitting of the internal nodes which represents testing on certain features. The branches of the tree represent the outcome of the test and each leaf node denotes the final outputs that are labels in our case. This ML algorithm is greedy in nature and follows a top-down where the most important feature is located at the top (known as the root node) and the leaves represent corresponding classes/labels. It can be used to perform both classification and regression tasks. Here, we will be using it to perform the classification of textual data.
## Implementing Decision Tree Classifier in Python with TextBlob
As discussed earlier TextBlob provides us the ability to perform NLP tasks efficiently. It is built on top of NLTK and pattern is used to do common tasks such as: sentiment analysis, language translation, parts of speech tagging, spelling correction, noun-phrase extraction, classification, etc. The main of this tutorial is to use it for performing a classification task.
But before, we dive straight into it, we first need to install all the dependencies that we will require during the course of making our classification model. We will begin with installing the TextBlob package to our system. TextBlob is a pip-installable package and therefore can be installed by executing a simple command in our command prompt:

  `pip install -U textblob`
  
  We also need to install specific corpora of text to be able to work with  Textblob, it can be downloaded using the command:
  
  `python -m textblob.download_corpora`
 
 Now, that we've downloaded and installed all the dependencies we can start writing the code for our program. To start with we will import the necessary libraries.
 ```
#Importing important libraries
from textblob import TextBlob
from textblob import classifiers
import pandas as pd
```
We will be performing a binary classification task to classify given movie reviews in two classes as either positive or negative. I am using here a subset of the IMDB movie review dataset that has two features, first feature represents the reviews and the second feature is our target class/label. The dataset can be downloaded from [train dataset](https://tinyurl.com/subsetdataset)
```
data = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Train.csv')
print("Shape of the data frame is: ",data.shape)
```

`Shape of the data frame is: (150, 2)`

Our dataset consists of 150 rows and 2 columns as we discussed earlier. We can do some EDA to visualize our dataset for gaining a clear picture of our data.

`data.head()`

![First five rows in the dataset](https://drive.google.com/file/d/1zW6gBTpGCyN2IrdbT6k8xDlSy1OVXqbP/view?usp=sharing)

Printing one of the reviews in the dataset

```print(data['review'][0])```

```mature intelligent and highly charged melodrama unbelivebly filmed in China in 1948. wei wei's stunning performance as the catylast in a love triangle is simply stunning if you have the oppurunity to see this magnificent film take it```

Now that we have a fair understanding of our dataset, we can start with building our model.
To make our classification model we can call the **DecisionTreeClassifier** method present inside the **textblob.classifier** class which implements decision tree algorithm, as it is implemented inside the NLTK package.

```
with  open('/content/drive/MyDrive/Colab Notebooks/Train.csv', 'r') as train_obj:
	dt = classifiers.DecisionTreeClassifier(train_set = train_obj, format="csv")
```
The **DecisionTreeClassifier()**method accepts two arguments:

 - train_set: It is the training data that can be in the form of a list of tuples like (text, classification) or any file. The text should either be iterable or a string.
 - format: If we pass a file inside the train_ set parameter, then format contains the format of the file like "csv" or "json". If None value is passed, it tries to detect the file format itself. 

After we finish the training of the model, we can call the **classify()** method to classify anything we want. Here, I'm passing a sample string to see how our model classifies it.

`dt.classify("This is an amazing movie! I loved it totally.")`
`'pos'`
So, we can see our model outputs a label for our text.
Let's check the accuracy of our model on a test dataset. It can be downloaded from: [test dataset](https://tinyurl.com/imdbtestset). The accuracy can be 
```
with  open('/content/drive/MyDrive/Colab Notebooks/Test.csv', 'r') as test_obj:
	print('The accuracy of our model is: ',cl.accuracy(test_obj,format="csv"))
```
`The accuracy of our model is: 0.5714285714285714`

So, we can see our model has an accuracy of 57.14% over the test dataset.

## Conclusion
Text classification is one of the common tasks implemented throughout the industry. If we write code from scratch to build a text classifier thn it will become quite a tedious task to do so. Hence, the TextBlob package comes as a lifesaver for us using which we can create a text classification model in a really quick time.
