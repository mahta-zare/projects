# machine-learning-project

This is just a not-so-complete description of the things I have done for my machine learning school project. There are lots of things one can interpret from the data and the actions that I have preformed on it. Many of these interpretations have NOT been mentioned in this description!:(

# Exercise-1
In Exersice 1 I am working on the Datapreprocessing.csv file. This file includes a few records of some countries and their attributes. The purpose of this exercise is to learn how to preprocess the data at hand. 
First, I use different methods of dealing with missing values in the dataset. Some of these methods leave our dataset in a much better condition that the others. 
Next, I dealed with the categorial variables using dummie variables
Then, since attributes Total population and Population growth hace different scales I uesed different feature scailing methods to scale them.
Nest, in order to find the ouliers i used IQR and z-score methods. After finding the ouliers with the z-score method, I preformed MLR once before removing them and once after. Each time I calculated the RMSE and and I noticed that once the ouliers are removed the RSME is smaller. So the final decision is to remove the ouliers.
Finally, I preformed polynomial regression on column Total Population (X) to find Corona Viruse Cases (Y) according to the formula: Y = aX^2 + bX + c 
Of course, because there is not enough data available, the result of the regression model is not acurate.

# Exercise-2
Here is the description of this exercise:
Congratulations! You just got some contract work with an Ecommerce company based
in New York City that sells clothing online but they also have in-store style and clothing
advice sessions. Customers come in to the store, have sessions/meetings with a personal
stylist, then they can go home and order either on a mobile app or website for the clothes
they want.
The company is trying to decide whether to focus their efforts on their mobile app experience
or their website. They’ve hired you on contract to help them figure it out!
We’ll work with the Ecommerce Customers csv file from the company. It has Customer
info, suchas Email, Address, and their color Avatar. Then it also has numerical value
columns:
Avg. Session Length: Average session of in-store style advice sessions.
Time on App: Average time spent on App in minutes
Time on Website: Average time spent on Website in minutes
Length of Membership: How many years the customer has been a member.
Do you think the company should focus more on their mobile app or on their website?



The dataset used in this exercise is uploaded under the name Ecommerce customers.csv

First, I used heatmap and pairplot to understand the correlation between columns.
Then, I preformed MLR on this dataset and calculated the MSE and the RMSE.
Next, I preformed K-fold cross validation and the RMSE equals sqrt(111) which is very large.
Finally, the answer to the question asked by the company is that they shoud focus more on the application rather than the website since the coefficient of the time spent on the application is about 40 according to the regression model but the cofficient of the time spent on the website is about 0.4 which is very small and insignificant.


# Exercise-3

The dataset for this exercise is available at: http://archive.ics.uci.edu/ml/datasets/Arrhythmia
First, I preprocessed the data. Then, I preformed the k nearest neighbors with k=1 and k=30 using the euclidean metric on the dataset. 
Next, using grid search I searched for the best k and the best metric for the k-fold cross validation.
