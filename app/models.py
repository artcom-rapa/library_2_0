# app/models.py

from app import db
from sqlalchemy import create_engine


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String(100), index=True, unique=True)
    biography = db.Column(db.String(200))

    books_a = db.relationship("Book", backref="author", lazy="dynamic")
    books_r = db.relationship("AuthorsBooks", backref="author", lazy="dynamic")

    def __str__(self):
        return f"<Author: {self.id} {self.author_name}>"


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, index=True)
    description = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    rented_id = db.Column(db.Integer, db.ForeignKey('rented.id'))

    authors = db.relationship("AuthorsBooks", backref="book", lazy="dynamic")

    def __str__(self):
        return f"<Book: {self.id} {self.title[:50]}...>"


class AuthorsBooks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))

    def __str__(self):
        return f"<AuthorsBooks: {self.author_id} {self.book_id}...>"


authors_book = AuthorsBooks()


class Rented(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rented_status = db.Column(db.Integer, nullable=False)

    books = db.relationship("Book", backref="rented", lazy="dynamic")

    def __str__(self):
        return f"<Rent status is {self.rented_status}"


class Books:
    def __init__(self):
        self.books = []

    def all(self):
        list_books = []
        all_books = Book.query.all()
        for book in all_books:
            list_book = {}
            list_book['id'] = book.id
            list_book['title'] = book.title
            list_book['description'] = book.description
            for author in book.authors:
                list_book['author'] = author.name
            rented = Rented.query.get(book.rented_id).rented_status
            if rented > 0:
                list_book['rented'] = 'rented'
            else:
                list_book['rented'] = 'available'
            list_books.append(list_book)
        return list_books

    def get(self, id):
        return self.all()[id]

    def create(self, data):
        data.pop('csrf_token')
        all_books = Book.query.all()
        max_book_index = 0
        for a_book in all_books:
            max_book_index = max(max_book_index, a_book.id)
        book = Book()
        book.id = max_book_index + 1
        book.title = data['title']
        book.author = data['author']
        book.description = data['description']

        all_rented = Rented.query.all()
        new_rented = Rented()
        max_rented_index = 0
        for rented in all_rented:
            max_rented_index = max(max_rented_index, rented.id)
        new_rented.id = max_rented_index + 1
        new_rented.rented_status = 0 if data['rented'] is False else 1
        book.rented_id = new_rented.id

        all_authors = Author.query.all()
        b_author = Author()
        b_author.name = data['author']
        max_author_index = 0
        for author in all_rented:
            max_author_index = max(max_author_index, author.id)
        b_author.id = max_author_index + 1

        author_already_existed = False

        for author in all_authors:
            if b_author.name == author.name:
                author_book = authors_book.insert().values(author_id=author.id,
                                                           book_id=the_book.id)
                author_already_existed = True
        if author_already_existed is False:
            author_book = authors_book.insert().values(author_id=b_author.id,
                                                       item_id=the_book.id)
            db.session.add(b_author)

        engine = create_engine('sqlite:///library.db', echo=True)
        author_book.compile().params
        conn = engine.connect()
        conn.execute(author_book)

        db.session.add(new_rented)
        db.session.add(book)
        db.session.commit()

    def update(self, id, data):
        data.pop('csrf_token')
        the_book = Book.query.all()[id]
        the_book.title = data['title']
        the_book.description = data['description']

        the_author = Author.query.all()[id]
        the_author.name = data['author']

        if data['rented'] == True:
            the_book.rented.rented_status = 0
        else:
            the_book.rented.rented_status = 1
        db.session.commit()

    def delete(self, id):
        data.pop('csrf_token')
        the_book = Book.query.all()[id]
        rented = Rented().query.get(the_book.rented_id)

        db.session.delete(rented)
        db.session.delete(the_book)
        db.session.commit()


books = Books()
