from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:1234@localhost/books_store"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# this is for routing

@app.route("/")
def hello_world():
    return render_template("index.html")



# this run the Flask
if __name__ == "__main__":
    app.run(debug=True)