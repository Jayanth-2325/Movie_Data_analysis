import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("Movie_dataset.csv")
gross_movie=df.groupby('Series_Title')['Gross'].sum().sort_values(ascending=False).head(10)
gross_movie = gross_movie / 1_000_000
plt.figure(figsize=(7,6))
gross_movie.plot(kind='bar')
#A few blockbuster movies generate significantly higher revenue than others.
plt.title('Which movie have a highest gross')
plt.xlabel('Series_Title')
plt.xticks(rotation=300)
plt.ylabel('Gross (Million USD)')
plt.tight_layout()
plt.savefig("Movie_gross.png")
plt.show()
