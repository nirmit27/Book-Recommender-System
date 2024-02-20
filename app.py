from flask import Flask, render_template, url_for
import pandas as pd

df = pd.read_csv('datasets/top50_updated.csv')

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="Top 50 Books",
                           book = list(df['Book-Title'].values[:50]),
                           author = list(df['Book-Author'].values[:50]),
                           img = list(df['Image-URL-M'].values[:50]),
                           votes = list(df['Total_Votes'].values[:50]),
                           rating = list(df['Average_Rating'].values[:50]),
                           min_rating = df['Average_Rating'].min(),
                           mean_rating = df['Average_Rating'].mean(),
                           max_rating = df['Average_Rating'].max())


if __name__ == "__main__":
    app.run(debug=True)

# Command : export FLASK_DEBUG=1 && flask run
