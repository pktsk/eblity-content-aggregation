import pandas as pd

df = pd.read_csv('youtube_links.csv')
print(df["index"].iloc[2])