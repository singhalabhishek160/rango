# pandas-which will allow to read data and present data and remove filter data andto even change data acc to our logic use pd



# numpy-allow mathematical things like in matlab work on array and matrices use np


# scipy-allow mathematical things like in matlab


# matplotlib-it will gaive review of the data and allow us to sort and trend of the dta use plt


#scikit-learn  = is actually machine learning use sklearn
import pandas as pd
import matplotlib.pyplot as plt


games = pd.read_csv("games.csv")
print(games.average_rating)
# Print the first row of all the games with scores greater than 0.
print(games[games["average_rating"] > 0].iloc[0])
games = games[games["users_rated"] > 0]
# Remove any rows with missing values.

games = games.dropna(axis=0)
plt.hist(games["average_rating"])
plt.show()

