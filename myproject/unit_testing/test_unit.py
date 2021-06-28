from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Genres, Books, BookForm

class TestBase(TestCase):
    def create_app(self):

        app.config.update(SQLALCHEMY_DATABASE_URI = "sqlite:///",
            SECRET_KEY = "mnssdfoihuvgjfhgdxerzqa",
            DEBUG = True,
            WTF_CSRF_ENABLED = False
            )
        return app

    def setUp(self):
        db.create_all()


        sample1 = Genres(name = 'History')
        sample2 = Books(title = 'Mythos', author_name = 'Stephen', description = 'A Great Read', finished = False, genre = Genres(name = 'History'))

        db.session.add(sample1)
        db.session.add(sample2)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestRead(TestBase):
    def test_read_home(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'History', response.data)
        self.assertIn(b'Mythos', response.data)
        self.assertIn(b'Stephen', response.data)
        self.assertIn(b'A Great Read', response.data)

    def test_read_add(self):
        response = self.client.get(url_for('add_new_book'))
        self.assertEqual(response.status_code, 200)

    def test_read_update(self):
        response = self.client.get(url_for('update', title = 'title'))
        self.assertEqual(response.status_code, 200)

class TestCreate(TestBase):
    def test_add_book(self):
        response = self.client.post(url_for('add_new_book'), follow_redirects = True, data = dict(title = "Cant Hurt Me", author_name = "David", name = "Self Improvment", description = "A Must Read", finished = True))
        self.assertIn(b"Cant Hurt Me", response.data)
        self.assertIn(b"David", response.data)
        self.assertIn(b"Self Improvment", response.data)
        self.assertIn(b"A Must Read", response.data)

    def test_add_same_genre(self):
        response = self.client.post(url_for('add_new_book'), follow_redirects = True, data = dict(title = "Heroes", author_name = "Stephen Fry", name = "History", description = "The second book on the topic", finished = False))
        self.assertIn(b"History", response.data)

class TestUpdate(TestBase):
    def test_update_book(self):
        response = self.client.post(url_for('update', title = 'Mythos'), follow_redirects = True, data = dict(title = "Troy", author_name = "Fry", name = "History", description = "The next installment in the series", finished = True))
        self.assertIn(b"Troy", response.data)
        self.assertIn(b"Fry", response.data)
        self.assertIn(b"History", response.data)
        self.assertIn(b"The next installment in the series", response.data)

class TestDelete(TestBase):
    def test_delete_book(self):
        response = self.client.delete(url_for('delete', title = 'Mythos'), follow_redirects = True)
        self.assertNotIn(b'Mythos', response.data)
        self.assertNotIn(b'Stephen', response.data)
        self.assertNotIn(b'History', response.data)
        self.assertNotIn(b'A Great Read', response.data)