from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField, TextAreaField
from application import db
from wtforms.validators import DataRequired, Length, ValidationError

class Genres(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), nullable = False)
    books = db.relationship('Books', backref = 'genre')

    def __init__(self, name):
        self.name = name

class Books(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(30), nullable = False, unique = True)
    author_name = db.Column(db.String(30))
    description = db.Column(db.String(100))
    finished = db.Column(db.String(10))
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'), nullable = False)

    def __init__(self, title, author_name, description, finished, genre):
        self.title = title
        self.author_name = author_name
        self.description = description
        self.finished = finished
        self.genre = genre

class BookForm(FlaskForm):
    title = StringField('Title of the Book:', validators = [DataRequired(), Length(min = 1, max = 30)])
    author_name = StringField('Name of the Author:', validators = [Length(min=0, max = 30)])
    name = StringField('Genre of the Book:', validators = [DataRequired(), Length(min = 1, max = 30)])
    description = TextAreaField('Short description of the Book:', validators = [Length(min = 0, max = 100)])
    finished = SelectField('Have you finished reading the Book?', choices = [('True', 'Yes'), ('False', 'No')])
    submit = SubmitField('Add Book to Reading List:')

    def validate_title(self, title):
        books = Books.query.all()
        for book in books:
            if book.title == title.data:
                raise ValidationError('This book is already in the library')
