import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("Movie_dataset.csv")

#insight: Most genres have similar ratings around 8, showing consistent movie quality.
plt.figure(figsize=(7,8))
df.groupby('Genre')['IMDB_Rating'].mean().sort_values(ascending=False).head(10).plot(kind='bar')
plt.title("Average Rating by Genre")
plt.ylim(6,9)
plt.xlabel("Genre")
plt.xticks(rotation=45, ha='right')
plt.ylabel("Average_Rating")
plt.tight_layout()
plt.savefig("Avg_Rating.png")
plt.show()


