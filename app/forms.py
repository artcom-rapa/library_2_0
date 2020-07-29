# app/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField
from wtforms.validators import DataRequired


class BookForm(FlaskForm):
    author = StringField('author')
    title = StringField('title', validators=[DataRequired()])
    description = TextAreaField('description')
    rented = BooleanField('rented')


class AuthorForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    biography = TextAreaField('biography')
