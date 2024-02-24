import pandas as pd

df = pd.read_csv('final-datasets/final_data.csv')
sdf = pd.read_csv('final-datasets/suggestions.csv')

# Data Cleaning

df.drop_duplicates('Book-Title', inplace=True)
df.drop(columns=['Unnamed: 0'], inplace=True)
df.rename(columns={'num_rating_x': 'num_r',
          'avg_rating_x': 'avg_r'}, inplace=True)
df['avg_r'] = round(df['avg_r'], 2)

sdf.drop_duplicates('book-title', inplace=True)
sdf.set_index('book-title', inplace=True)
sdf.drop(columns=['Unnamed: 0'], inplace=True)

# Utility Functions for fetching the data


def data_util1(book):
    return df[df['Book-Title'] == book]


def data_util2(book):
    res = []
    try:
        x = sdf.loc[book]
    except KeyError as e:
        return res
    for sugg in x.values:
        res.append(data_util1(sugg))
    return res


def data_util3(book):
    res = []
    x = data_util2(book)
    if len(x) == 0:
        return []
    for item in data_util2(book):
        res.append(item)
    return res

# Driver code


if __name__ == "__main__":
    ans = data_util3('Anime')
    if len(ans) == 0:
        print('No such entry!')
    else:
        for row in ans:
            for value in row.values:
                print(
                    f"Title : {value[0]}\nAuthor : {value[1]}\nImage : {value[2]}\nVotes : {value[3]}\nRating :     {round(value[4], 2)}\n")
            print()
