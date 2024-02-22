from flask import Flask, render_template, url_for, request
import pandas as pd

from data_fetch import data_util3 as sf

df = pd.read_csv('datasets/pop.csv')

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
    res = ''
    user_input = request.form.get('user_input')
    suggestions = sf(str(user_input))
    for suggestion in suggestions:
        for x in suggestion.values:
            res += f"{str(x)}<br>"
    return res


if __name__ == "__main__":
    app.run(debug=True)

# Command : export FLASK_DEBUG=1 && flask run
