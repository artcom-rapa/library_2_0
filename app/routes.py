# app/roues.py

from flask import Flask, request, render_template, redirect, url_for

from app import db
from app.forms import BookForm, AuthorForm
from app.models import books, Author

app = Flask(__name__)
app.config["SECRET_KEY"] = "ninininini"


@app.route("/", methods=["GET", "POST"])
def index():
    return redirect(url_for("book_list"))


@app.route("/books/", methods=["GET", "POST"])
def book_list():
    books.all()
    form = BookForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            books.create(form.data)
        return redirect(url_for("books_list"))

    return render_template("books.html", form=form,
                           books=books, error=error)


@app.route("/books/<int:book_id>/", methods=["GET", "POST"])
def book_details(book_id):
    def __init__():
        pass

    book = books.get(book_id - 1)
    form = BookForm(data=book)

    if request.method == "POST":
        if request.form.get('delete'):
            books.delete(book_id - 1)
        elif form.validate_on_submit():
            if book_id > 0:
                books.update(book_id - 1, form.data)
            else:
                pass
        return redirect(url_for("books_list"))
    return render_template("book.html", form=form, book_id=book_id)


@app.route("/author/<string:author_id>/", methods=["GET", "POST"])
def author_details(author_id):
    a = Author.query.filter_by(name=author_id).first()
    if a is None:
        return "Author unknown!"



    author_dict = {
        'name': a.name,
        'biography': a.biography
    }

    form = AuthorForm(data=author_dict)

    if request.method == "POST":
        if form.validate_on_submit():
            a.name, a.biography = tuple(form.data.values())[:2]
            db.session.add(a)
            db.session.commit()

        return redirect(url_for("books_list"))
    return render_template("author.html", form=form, author_name=author_id)


if __name__ == "__main__":
    app.run(debug=True)
