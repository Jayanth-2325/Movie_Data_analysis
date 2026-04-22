import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("Movie_dataset.csv")
genre_counts = df['Genre'].value_counts().head(5)
plt.figure()
#Drama dominates the dataset, showing it is the most common genre.
plt.pie(genre_counts, labels=genre_counts.index, autopct='%1.1f%%')
plt.title("Top 5 Movie Genres Distribution")
plt.savefig("Top5_genre_distribution.png")
plt.show()
