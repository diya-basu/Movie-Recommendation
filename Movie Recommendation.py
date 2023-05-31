#importing all the neccessary modules
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random

def index(index):
    return df[df.index==index]["title"].values[0]

def get_index_title(title):
    return df[df.title== title]["index"].values[0]


df=pd.read_csv("Dataset.csv")
features=['keywords','cast','genres','director']


for ft in features: 
    df[ft]=df[ft].fillna('')

def combine_features(row):
    try: 
        return row['keywords']+" "+row['cast']+" "+row["genres"]+" "+row["director"]
    except:
        print("Error:", row)

df["combi_features"]=df.apply(combine_features,axis=1)

countvector = CountVectorizer()

count_matrix = countvector.fit_transform(df["combi_features"])
cos_sim=cosine_similarity(count_matrix)

print("\nUser,please enter a movie you like:")
movie_user_likes = input()
movie_index = get_index_title(movie_user_likes)


print("\nWe recommend the following movies to you:")

similar_mov =  list(enumerate(cos_sim[movie_index]))

movies = sorted(similar_mov,key=lambda x:x[1],reverse=True)

i=0
for element in movies:
        print(index(element[0]))
        i=i+1
        if i>10:
                break
        else:
                pass
                

