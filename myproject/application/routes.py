from flask import render_template, request, url_for, redirect
from application import app, db
from application.models import Genres, Books, BookForm

@app.route('/', methods = ['GET'])
@app.route('/home', methods = ['GET'])
def home():

    genres_in_table = Genres.query.all()
    books_in_table = Books.query.all()

    return render_template('home.html', genres_in_table = genres_in_table, books_in_table = books_in_table)

@app.route('/add', methods = ['GET', 'POST'])
def add_new_book():
    form = BookForm()

    if form.validate_on_submit():
        title = form.title.data
        author_name = form.author_name.data
        name = form.name.data
        description = form.description.data
        finished = form.finished.data

        current_genre = Genres.query.filter_by(name= name).all()
        if len(current_genre) != 0:
            genre = Genres.query.filter_by(name= name).first()
            book = Books(title, author_name, description, finished, genre)
            db.session.add(book)
            db.session.commit()

        else:
            genre = Genres(name)
            db.session.add(genre)
            db.session.commit()
            book = Books(title, author_name, description, finished, genre)
            db.session.add(book)
            db.session.commit()

        return redirect(url_for('home'))
    return render_template('add.html', form = form)

@app.route('/update/<title>', methods = ['GET', 'POST'])
def update(title):
    form = BookForm()
    book = Books.query.filter_by(title = title).all()
    if form.validate_on_submit():
        for i in book:
            i.title = form.title.data
            i.author_name = form.author_name.data
            i.name = form.name.data
            i.description = form.description.data
            i.finished = form.finished.data
            db.session.commit()
        return redirect(url_for('home'))

    elif request.method == 'GET':
        return render_template('update.html', form = form, book = book)

@app.route('/delete/<title>')
def delete(title):
    book_to_delete = Books.query.filter_by(title = title).first()
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))