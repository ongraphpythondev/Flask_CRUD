import datetime
from flask import Flask , render_template , request , redirect , url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:1234@localhost/books_crud"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

    
class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    author = db.Column(db.String())
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __repr__(self):
        return f"id = {self.id} name = {self.name}"
    


# this is for routing
@app.route("/")
def book():
    books = Book.query.order_by(Book.created).all()
    return render_template("book.html" , books = books)

@app.route("/add" , methods=['GET','POST'])
def books():
    if request.method == "GET":
        return render_template("add.html")
    elif request.method == "POST":
        name = request.form["name"]
        author = request.form["author"]
        

        book_obj =Book(name=name, author = author )
        db.session.add(book_obj)
        db.session.commit()

        return redirect(url_for("book"))


@app.route("/delete/<pk>" )
def delete(pk):
        

        book_obj =Book.query.filter_by(id = pk).first()
        db.session.delete(book_obj)
        db.session.commit()

        return redirect(url_for("book"))


@app.route("/update/<pk>" , methods=['GET','POST'])
def update(pk):
    
    book_obj =Book.query.filter_by(id = pk).first()
    if request.method == "GET":
        return render_template("update.html" , book_name = book_obj.name , author = book_obj.author , id = book_obj.id)
    elif request.method == "POST":
        
        print(book_obj)
        name = request.form["name"]
        author = request.form["author"]
        

        book_obj.name = name
        book_obj.author = author
        db.session.commit()
        return redirect(url_for("book"))



# this run the Flask
if __name__ == "__main__":
    app.run(debug=True)