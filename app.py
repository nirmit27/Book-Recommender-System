from flask import Flask, render_template, url_for, request
import pandas as pd

df = pd.read_csv('new-datasets/pop.csv')
fdf = pd.read_csv('new-datasets/final.csv')
sdf = pd.read_csv('new-datasets/sugg.csv')


def data_util(book):
    book_data = []
    if sdf[sdf['book-title'] == book].index.shape[0] == 0:
        return book_data
    for name in sdf[sdf['book-title'] == book].values[0][1:]:
        for data in fdf[fdf['Book-Title'] == name].values:
            book_data.append(data)
    return book_data


app = Flask(__name__)

# Top 50 Books route


@app.route('/')
def index():
    return render_template('index.html', title="Top 50 Books",
                           book=list(df['Book-Title'].values[:50]),
                           author=list(df['Book-Author'].values[:50]),
                           img=list(df['Image-URL-M'].values[:50]),
                           votes=list(df['Total_Votes'].values[:50]),
                           rating=list(df['Average_Rating'].values[:50]),
                           p_25=df['Average_Rating'][:50].describe()['25%'],
                           p_50=df['Average_Rating'][:50].describe()['50%'],
                           p_75=df['Average_Rating'][:50].describe()['75%'])

# Recommender System route


@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html', title="Recommended For You")


@app.route('/recommend_books', methods=['post'])
def recommend():
    user_input = request.form.get('user_input')
    suggestions = data_util(str(user_input).strip())
    if len(suggestions) == 0:
        return render_template('recommend.html', data=[], title="No suggestions found for ", book_title=str(user_input))
    else:
        return render_template('recommend.html', data=suggestions[1:], title="Top 5 suggestions for ", book_title=str(user_input))


if __name__ == "__main__":
    app.run(debug=True)
