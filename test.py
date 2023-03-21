import pandas as pd
import numpy as np
import scipy.stats
import seaborn as sns
from sklearn.metrics.pairwise import cosine_similarity

ratings=pd.read_csv('ratings.csv')
movies=pd.read_csv('movies.csv')
ratings.head()
#print("Hello World")

print('The ratings dataset has', ratings['userID'].nunique(), 'unique users.')
print('The ratings dataset has', ratings['movieID'].nunique(), 'unique movies.')
print('The ratings dataset has', ratings['rating'].nunique(), 'unique ratings.')
print('The unique ratings are', sorted(ratings['rating'].unique()))

df=pd.merge(ratings, movies, on='movieId', how='inner')
df.head()

agg_ratings=df.groupby('title').agg(mean_rating=('rating','mean'),
                                    number_of_ratings=('rating', 'count')).reset_index()
agg_ratings_GT100=agg_ratings[agg_ratings['number_of_ratings']>100]
agg_ratings_GT100.info()