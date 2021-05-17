import numpy as np
import pandas as pd

#rating = pd.read_csv("rating.csv")
anime = pd.read_csv("anime.csv")

items = np.array(anime.genre)


genres = input("Ps: keep the first letter as Capital \n Enter the genre: " )

val = [(genres in str(item)) for item in items]

#for item in items:
#    val = [("Drama" in str(item))]

X = anime.loc[val]

X_mod = X[['name', 'genre', 'type', 'episodes', 'rating']]

print(X_mod.head())




