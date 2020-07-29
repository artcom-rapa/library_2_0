# library.py
from app import app, db
from app.models import Author, Book, Rented


@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "Author": Author,
        "Book": Book,
        "Rented": Rented
    }
