from flask_testing import LiveServerTestCase
from selenium import webdriver
from flask import url_for
from os import getenv

from application import app, db
from application.models import Genres, Books, BookForm

class TestBase(LiveServerTestCase):
    def create_app(self):

        app.config.update(SQLALCHEMY_DATABASE_URI = "",
            SECRET_KEY = "",
            LIVESERVER_PORT = self.TEST_PORT,
            DEBUG = True,
            TESTING = True
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

class test_int_create_book(TestBase):
    def adding_new_book(self):
        self.driver.find_element_from_xpath('//*[@id="title"]').send_keys('Troy')
        self.driver.find_element_from_xpath('//*[@id="author_name"]').send_keys('Fry')
        self.driver.find_element_from_xpath('//*[@id="name"]').send_keys('History')
        self.driver.find_element_from_xpath('//*[@id="description"]').send_keys('Second of three')
        self.driver.find_element_from_xpath('//*[@id="submit"]').click()

        text = self.driver.find_element_by_xpath('/html/body/p[1]/b').text
        self.assertIn("Troy", text)

        text = self.driver.find_element_by_xpath('/html/body/p[1]').text
        self.assertIn("Troy - Fry", text)

        text = self.driver.find_element_by_xpath('/html/body/h3/u').text
        self.assertIn("History", text)

        text = self.driver.find_element_by_xpath('/html/body/p[2]/i').text
        self.assertIn("Second of three", text)

        entries = Books.query.all()
        self.assertEqual(len(entries), 2)




class test_int_home_page(TestBase):
    def read_home_page(self):
        entries = Books.query.all()
        self.assertEqual(len(entries), 1)

        text = self.driver.find_element_by_xpath('/html/body/p[1]/b').text
        self.assertIn("Mythos", text)

        text = self.driver.find_element_by_xpath('/html/body/p[1]').text
        self.assertIn("Mythos - Stephen", text)

        text = self.driver.find_element_by_xpath('/html/body/h3/u').text
        self.assertIn("History", text)

        text = self.driver.find_element_by_xpath('/html/body/p[2]/i').text
        self.assertIn("A Great Read", text)




class test_int_update_book(TestBase):
    def update_existing_book(self):
        update_title = find_element_from_xpath('//*[@id="title"]').send_keys('Cant hurt me')
        update_author = find_element_from_xpath('//*[@id="author_name"]').send_keys('David')
        update_genre = find_element_from_xpath('//*[@id="name"]').send_keys('self improvment')
        update_description = find_element_from_xpath('//*[@id="description"]').send_keys('A must read')
        update_submit = find_element_from_xpath('//*[@id="submit"]').click()


