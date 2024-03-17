from flask import Flask, render_template, url_for, request
import pandas as pd
import subprocess


# Run the build script for TAILWIND CSS
subprocess.run(["npm", "run", "build:css"], check=True)

# Fetching data to be displayed
df = pd.read_csv('new-datasets/pop.csv')
fdf = pd.read_csv('new-datasets/final.csv')
sdf = pd.read_csv('new-datasets/sugg.csv')

# Utililty function for data
def data_util(book):
    book_data = []
    if sdf[sdf['book-title'] == book].index.shape[0] == 0:
        return book_data
    for name in sdf[sdf['book-title'] == book].values[0][1:]:
        for data in fdf[fdf['Book-Title'] == name].values:
            book_data.append(data)
    return book_data


app = Flask(__name__)

# Routes ...

# Home page

@app.route('/')
def index():
    return render_template('i.html')

# Top 50 book recommendations

@app.route('/top50')
def top50():
    return render_template('t50.html',
                           book=list(df['Book-Title'].values[:50]),
                           author=list(df['Book-Author'].values[:50]),
                           img=list(df['Image-URL-M'].values[:50]),
                           votes=list(df['Total_Votes'].values[:50]),
                           rating=list(df['Average_Rating'].values[:50]),
                           p_25=df['Average_Rating'][:50].describe()['25%'],
                           p_50=df['Average_Rating'][:50].describe()['50%'],
                           p_75=df['Average_Rating'][:50].describe()['75%'])

# Top 5 recommendations

@app.route('/recommend')
def recommend_ui():
    return render_template('r.html', title="Recommended For You")

# Processing user input

@app.route("/recommend_books", methods=["POST"])
def recommend():
    user_input = request.form.get('user_input')
    suggestions = data_util(str(user_input).strip())

    if len(suggestions) == 0:
        return render_template('r.html', data=[], title="No suggestions found for ", book_title=str(user_input))
    else:
        return render_template('r.html', data=suggestions[1:], title="Top 5 suggestions for ", book_title=str(user_input))

# About page
    
@app.route('/about')
def about():
    return render_template('a.html')


if __name__ == "__main__":
    app.run(debug=True)
