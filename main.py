from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
import os

# Configure the app:

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')
Bootstrap5(app)

@app.route('/')
def render_home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=False, port=5001)
    