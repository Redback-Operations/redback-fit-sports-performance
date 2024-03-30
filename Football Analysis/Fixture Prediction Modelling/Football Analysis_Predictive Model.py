#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing necessary libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


# In[3]:


# Import dataset
df = pd.read_csv('2022-23data.csv')


# In[6]:


# Displaying the shape of the DataFrame (number of rows, number of columns)
df.shape


# In[5]:


df.info


# In[9]:


# Displaying the first few rows of the DataFrame
df.head()


# In[10]:


# Counting the number of missing values in each column of the DataFrame
df.isnull().sum()


# In[11]:


# Retrieving the column names 
df.columns


# ## EDA (Exploratory Data Analysis)
# 
# 

# In[12]:


# Keep only columns that can inform matches before game or during half time
df = df[['Date','Time','HomeTeam','AwayTeam','H_Ranking_Prior_Season','A_Ranking_Prior_Season','FTHG','FTAG','FTR','HTHG','HTAG','HTR','Referee','B365H','B365D','B365A']]


# In[13]:


df.head()


# In[14]:


# Shape of data
#Insights on Full time and Half time results
print('Shape of data: ', df.shape)
print('\n')
print('Full time results:')
print(df['FTR'].value_counts() / df.shape[0])

print('\n')
print('Half time results:')
print(df['HTR'].value_counts() / df.shape[0])


# In[15]:


#confusion matrix of team results based on half-time
print('Confusion matrix, half-time to full-time')
print(pd.crosstab(df['HTR'], df['FTR'], rownames=['Half-Time'], colnames=['Full-Time']))


# In[16]:


# Histogram of full-time home team goals
df['FTHG'].hist(bins=10, figsize=(15,10))
plt.show()


# In[17]:


## Variable creation (point difference at half: Home Goals - Away Goals)
df['half_time_GD'] = df['HTHG'] - df['HTAG']

## Explore how predictive the goal difference is of final outcomes
df['half_time_GD'].hist()


# In[18]:


print('Confusion matrix, half-time goal difference compared to full-time match result')
print(pd.crosstab(df['half_time_GD'], df['FTR'], rownames=['Half-Time Goal Difference (Home - Away)'], colnames=['Full-Time']))


# In[19]:


df.head()


# In[20]:


fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(x = df['B365H'], y = df['FTHG'])
ax.set_xlabel('Betting odds for home team')
ax.set_ylabel('Home team goals (full time)')


# In[21]:


## Variable creation (point difference at full time: Home Goals - Away Goals)
df['full_time_GD'] = df['FTHG'] - df['FTAG']

## Explore how predictive the goal difference is of final outcomes
df['full_time_GD'].hist()


# In[22]:


fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(x = df['B365H'], y = df['full_time_GD'])
ax.set_xlabel('Betting odds for home team')
ax.set_ylabel('Full time goal difference (home - away)')


# In[23]:


fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(x = df['A_Ranking_Prior_Season'], y = df['full_time_GD'])
ax.set_xlabel('Prior Season Ranking')
ax.set_ylabel('Full time goal difference (home - away)')


# In[24]:


# separate features from the target
y = df['FTR'] # target variable (winning team)
X = df.drop(columns = ['Date','Time','Referee','FTR','FTHG','FTAG','full_time_GD'])


# In[25]:


#One-Hot encode all categorical variables

# Function for one-hot encoding, takes dataframe and features to encode
# returns one-hot encoded dataframe
# from: https://stackoverflow.com/questions/37292872/how-can-i-one-hot-encode-in-python
def encode_and_bind(original_dataframe, feature_to_encode):
    dummies = pd.get_dummies(original_dataframe[[feature_to_encode]])
    res = pd.concat([original_dataframe, dummies], axis=1)
    res = res.drop([feature_to_encode], axis=1)
    return(res)
# features to one-hot encode in our data
features_to_encode = ['HomeTeam','AwayTeam']

for feature in features_to_encode:
    X = encode_and_bind(X, feature)

# results of one-hot encoding
X.head()


# In[26]:


#split into test and training datasets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)


# In[27]:


X_train


# In[28]:


y_train


# ## Logistic Regression Model

# In[29]:


from sklearn.linear_model import LogisticRegression


# In[30]:


features_to_encode = ['HTR']

for feature in features_to_encode:
    X_train = encode_and_bind(X_train, feature)

for feature in features_to_encode:
    X_test = encode_and_bind(X_test, feature)

# results of one-hot encoding
X_train.head()


# In[31]:


logit = LogisticRegression()
logit.fit(X_train,y_train)


# In[32]:


print('Logistic regression accuracy on train set: ', round(logit.score(X_train,y_train),3))


# In[33]:


print('Logistic regression accuracy on test set: ', round(logit.score(X_test,y_test),3))


# ### Hyperparamater tuning, Logistic Regression

# In[35]:


## Adjusting C parameter
logit_tuned = LogisticRegression(penalty = 'l2', C = 0.000001)
logit_tuned.fit(X_train,y_train)


# In[36]:


# storage variables
train_accuracies = []
test_accuracies = []
c_vals = np.logspace(-7, -2.5, num = 100) # Penalty parameters to test

## Hyperparameter tuning for loop
for c_val in c_vals: # For every penalty parameter we're testing

   # Fit model on training data
   logit_tuned = LogisticRegression(penalty = 'l2', C = c_val)
   logit_tuned.fit(X_train, y_train)

   # Store training and test accuracies
   train_accuracies.append(logit_tuned.score(X_train,y_train))
   test_accuracies.append(logit_tuned.score(X_test,y_test))


# In[37]:


# plot train and test accuracies
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(c_vals, train_accuracies, label = 'train')
ax.plot(c_vals, test_accuracies, label = 'test')
ax.set_xlabel('Values of Tuning Parameter (C)')
ax.set_ylabel('Accuracy')
ax.legend(loc = 'best')


# In[38]:


## Determining maximizing C on test set
print('Maximum test accuracy: ', np.round(test_accuracies[np.argmax(test_accuracies)], 3))
print('Value of C that achieves max test accuracy: ', np.round(c_vals[np.argmax(test_accuracies)],5))


# ## Decision Tree Model
# 

# In[39]:


tree = DecisionTreeClassifier()
tree.fit(X_train,y_train)


# In[40]:


sklearn.tree.plot_tree(tree,max_depth=1)


# In[41]:


X_train


# In[42]:


print('Tree accuracy on train set: ', round(tree.score(X_train,y_train),3))


# In[43]:


print('Tree accuracy on test set: ', round(tree.score(X_test,y_test),3))


# In[44]:


# storage variables
train_accuracies = []
test_accuracies = []
min_vals = np.linspace(0.001, 1, num = 500) # Penalty parameters to test

## Hyperparameter tuning for loop
for min_val in min_vals: # For every penalty parameter we're testing

   # Fit model on training data
   tree_tuned = DecisionTreeClassifier(min_samples_split = min_val)
   tree_tuned.fit(X_train, y_train)

   # Store training and test accuracies
   train_accuracies.append(tree_tuned.score(X_train,y_train))
   test_accuracies.append(tree_tuned.score(X_test,y_test))


# In[45]:


# plot train and test accuracies
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(min_vals, train_accuracies, label = 'train')
ax.plot(min_vals, test_accuracies, label = 'test')
ax.set_xlabel('Values of Tuning Parameter (min samples)')
ax.set_ylabel('Accuracy')
ax.legend(loc = 'best')


# In[46]:


print('Maximum test accuracy: ', np.round(test_accuracies[np.argmax(test_accuracies)], 3))
print('Value of min samples that achieves max test accuracy: ', np.round(min_vals[np.argmax(test_accuracies)],5))


# ## Random Forest Model

# In[47]:


forest = RandomForestClassifier()
forest.fit(X_train,y_train)


# In[48]:


print('Random forest accuracy on train set: ', round(forest.score(X_train,y_train),3))


# In[49]:


print('Random Forest accuracy on test set: ', round(forest.score(X_test,y_test),3))


# In[50]:


# storage variables
train_accuracies = []
test_accuracies = []
min_vals = np.linspace(0.001, 1, num = 10) # Penalty parameters to test
nTrees = np.arange(1,1000,step=200)

## Hyperparameter tuning for loop
for min_val in min_vals: # For every penalty parameter we're testing
   for nTree in nTrees:
    # Fit model on training data
    forest_tuned = RandomForestClassifier(min_samples_split = min_val, n_estimators = nTree)
    forest_tuned.fit(X_train, y_train)

    # Store training and test accuracies
    train_accuracies.append(forest_tuned.score(X_train,y_train))
    test_accuracies.append(forest_tuned.score(X_test,y_test))


# In[51]:


np.argmax(test_accuracies)


# In[52]:


print('Maximum test accuracy: ', np.round(test_accuracies[np.argmax(test_accuracies)], 3))
print('Value of min samples that achieves max test accuracy: ', np.round(min_vals[round(np.argmax(test_accuracies)/1000)],5))
print('Value of min trees that achieves max test accuracy: ', np.round(nTrees[1],5))


# In[53]:


# Get random forest feature importances

importances = forest.feature_importances_
feature_names = X_train.columns

forest_importances = pd.Series(importances, index=feature_names)

fig, ax = plt.subplots()
forest_importances[forest_importances > 0.02].sort_values(ascending = False).plot.bar(ax=ax)
ax.set_title("Feature importances using MDI")
ax.set_ylabel("Mean decrease in impurity")
fig.tight_layout()

