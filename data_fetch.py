import pandas as pd

df = pd.read_csv('datasets/suggestions.csv')
df.rename(columns={'Unnamed: 0': "book-title"}, inplace=True)

if __name__ == "__main__":
    print(df[:50].shape)
