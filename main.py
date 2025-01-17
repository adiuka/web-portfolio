from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5

# Configure the app:

app = Flask(__name__)
app.config['SECRET_KEY'] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap5(app)

@app.route('/')
def render_home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)