import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("Movie_dataset.csv")
#Movie production varies by year, with some years having higher releases.
plt.figure(figsize=(7,6))
df['Released_Year'].value_counts().head(10).sort_index().plot(kind='bar')
plt.title("Number of Movies Released in Each Year")
plt.xlabel("Year")
plt.xticks(rotation=0)
plt.ylabel("Count")
plt.savefig("year_movie.png")
plt.show()