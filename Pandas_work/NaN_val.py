import pandas as pd

movie_rating = pd.read_csv("movie_scores.csv")
print(movie_rating)

#conditional check for NULL Values
Row_with_no_ratings = movie_rating[(movie_rating['pre_movie_score'].isnull()) & (movie_rating['first_name'].notnull())]

#Filling NULL Values
movie_rating['pre_movie_score'] = movie_rating['pre_movie_score'].fillna(movie_rating["pre_movie_score"].mean())
movie_rating['post_movie_score'] = movie_rating['post_movie_score'].interpolate(method = 'linear')

#Dropping NULL Values
#print(movie_rating.dropna())
