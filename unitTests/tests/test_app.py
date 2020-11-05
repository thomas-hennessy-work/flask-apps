# Import the necessary modules
import unittest
from flask import url_for
from flask_testing import TestCase

# import the app's classes and objects
from app import app, db, Register

# Create the base class
class TestBase(TestCase):
    def create_app(self):

        # Pass in testing configurations for the app. Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True
                )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # Create table
        db.create_all()

        # Create test registree (A test person to add to the database(called register))
        sample1 = Register(name="MissWoman")

        # save users to database
        db.session.add(sample1)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()

# Write a test class for testing that the home page loads but we are not able to run a get request for delete and update routes.
class TestViews(TestBase):

    def test_home_get(self):
        #Did the test seccessfully get to the home page
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

        #same as above but for the update page. 405, shouldnt be allowed using this method
    def test_update_get(self):
        response = self.client.get(url_for('update'))
        self.assertEqual(response.status_code,405)

    def test_delete_get(self):
        response = self.client.get(url_for('delete'))
        self.assertEqual(response.status_code,405)

# Test adding 
class TestAdd(TestBase):
    def test_add_post(self):
        response = self.client.post(
            url_for('home'),
            data = dict(name="MrMan")
        )
        #when on the home page, dose mrman exist?
        #b is for bytes (how the data is gathered)
        self.assertIn(b'MrMan',response.data)

# Test updating

class TestUpdate(TestBase):
    def test_update_post(self):
        response = self.client.post(
            url_for('update'),
            data = dict(oldname="MissWoman", newname="MissLady"),
            follow_redirects=True
            )
        self.assertEqual(response.status_code,200)
# Test Deleting

class TestDelete(TestBase):
    def test_delete_post(self):
        response = self.client.post(
            url_for('delete'),
            data = dict(name="MissWoman"),
            follow_redirects=True
            )
        self.assertEqual(response.status_code,200)
