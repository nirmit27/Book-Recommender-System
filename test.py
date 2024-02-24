import pandas as pd

df = pd.read_csv('new-datasets/pop.csv')
fdf = pd.read_csv('new-datasets/final.csv')
sdf = pd.read_csv('new-datasets/sugg.csv')


def data_util(book):
    book_data = []
    if sdf[sdf['book-title'] == x].index.shape[0] == 0:
        return book_data
    for name in sdf[sdf['book-title'] == book].values[0][1:]:
        for data in fdf[fdf['Book-Title'] == name].values:
            book_data.append(data)
    return book_data


if __name__ == "__main__":
    x = "anime"
    print(sdf[sdf['book-title'] == x].index.shape[0])
