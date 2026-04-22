import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("Movie_dataset.csv")
top_directors=df.groupby('Director')['IMDB_Rating'].mean().sort_values(ascending=False).head(8)
plt.figure()
top_directors.plot(kind='bar')
#Top directors consistently produce highly rated movies.
plt.title('Director rating analyze')
plt.xticks(rotation=300)
plt.ylim(6,9)
plt.tight_layout()
plt.xlabel('Directors')
plt.ylabel('Rating')
plt.savefig('director_rating.png')
plt.show()