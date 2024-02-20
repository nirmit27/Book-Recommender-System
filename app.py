from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="Book Recommender System")


if __name__ == "__main__":
    app.run(debug=True)

# Command : export FLASK_DEBUG=1 && flask run
