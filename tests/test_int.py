import unittest
import time
from flask import url_for
from urllib.request import urlopen

from os import getenv
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from application import app, db, bcrypt
from application.models import Users, book_library, main_library
from werkzeug.security import generate_password_hash, check_password_hash

# Set test variables for test admin user
test_admin_first_name = "admin"
test_admin_last_name = "admin"
test_admin_email = "admin@email.com"
test_admin_password = "admin2020"

# creating test book entry
test_id = 1,
test_first_name = 'test'
test_surname = 'test'
test_title ='test'
test_pages =123
test_language = 'test'
test_user_id = 1

# creating test update book
test_id = 1,
test_update_first_name = 'U test'
test_update_surname = 'U test'
test_update_title ='U test'
test_update_pages =123456
test_update_language = 'U test'
test_update_user_id = 1

# creating a test rating
test_id = 1,
test_rating = 2
test_comment = 'test'
test_user_id = 1
test_book_id = 1

class TestBase(LiveServerTestCase):

	def create_app(self):
		app.config['SQLALCHEMY_DATABASE_URI'] = str(getenv('TEST_DB_URI'))
		app.config['SECRET_KEY'] = getenv('TEST_SECRET_KEY')
		return app

	def setUp(self):
		"""Setup the test driver and create test users"""
		print("--------------------------NEXT-TEST----------------------------------------------")
		chrome_options = Options()
		chrome_options.binary_location = "/usr/bin/chromium-browser"
		chrome_options.add_argument("--headless")
		self.driver = webdriver.Chrome(executable_path="/home/jacob_hp_grub/increment/chromedriver", chrome_options=chrome_options)
		self.driver.get("http://localhost:5000")
		db.session.commit()
		db.drop_all()
		db.create_all()

		# creating a test user

		# testuser = Users(
   		# 	id = 1,
		# 	first_name = 'testy',
		# 	last_name = 'Mctestface',
		# 	email = 'test@test.com',
		# 	password = 'test123'
		# )
		# # creating a test book
		# Test_book = book_library(
		# 	id = 1,
		# 	first_name = 'test',
		# 	surname = 'test',
		# 	title ='test',
		# 	pages =123,
		# 	language = 'test',
		# 	user_id = 1
		# )
		# # creating a test rating
		# Test_rate = main_library(
		# 	id = 1,
		# 	rating = 2,
		# 	comment = 'test',
		# 	user_id = 1,
		# 	book_id = 1
		# )
		# # adds the test data to the database
		# db.session.add(testuser)
		# db.session.add(Test_book)
		# db.session.add(Test_rate)
		# db.session.commit()


	def tearDown(self):
		self.driver.quit()
		print("--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")

	def test_server_is_up_and_running(self):
		response = urlopen("http://localhost:5000")
		self.assertEqual(response.code, 200)

class TestRegistration(TestBase):
	def test_registration(self):
		# Click register menu link
		self.driver.find_element_by_xpath('/html/body/div[1]/a[2]').click()
		time.sleep(1)

		# Fill in registration form
		self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(test_admin_email)
		self.driver.find_element_by_xpath('//*[@id="first_name"]').send_keys(test_admin_first_name)
		self.driver.find_element_by_xpath('//*[@id="last_name"]').send_keys(test_admin_last_name)
		self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(test_admin_password)
		self.driver.find_element_by_xpath('//*[@id="confirm_password"]').send_keys(test_admin_password)
		self.driver.find_element_by_xpath('//*[@id="submit"]').click()
		time.sleep(1)

		# Assert that browser redirects to login page
		assert url_for('login') in self.driver.current_url

class TestLogin(TestBase):
	def test_login(self):
		self.driver.find_element_by_xpath("/html/body/div[1]/a[2]").click()
		time.sleep(1)

		# Fill in registration form
		self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(test_admin_email)
		self.driver.find_element_by_xpath('//*[@id="first_name"]').send_keys(test_admin_first_name)
		self.driver.find_element_by_xpath('//*[@id="last_name"]').send_keys(test_admin_last_name)
		self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(test_admin_password)
		self.driver.find_element_by_xpath('//*[@id="confirm_password"]').send_keys(test_admin_password)
		self.driver.find_element_by_xpath('//*[@id="submit"]').click()
		time.sleep(1)
		
		self.driver.find_element_by_xpath('/html/body/div[1]/a[1]').click()
		assert url_for('login') in self.driver.current_url
		time.sleep(1)

		self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(test_admin_email)
		self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(test_admin_password)
		self.driver.find_element_by_xpath('//*[@id="submit"]').click()
		time.sleep(2)
		assert url_for('main_lib') in self.driver.current_url

class Test_new_entry(TestBase):
	def test_new_entry(self):
		self.driver.find_element_by_xpath("/html/body/div[1]/a[2]").click()
		time.sleep(1)

		# Fill in registration form
		self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(test_admin_email)
		self.driver.find_element_by_xpath('//*[@id="first_name"]').send_keys(test_admin_first_name)
		self.driver.find_element_by_xpath('//*[@id="last_name"]').send_keys(test_admin_last_name)
		self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(test_admin_password)
		self.driver.find_element_by_xpath('//*[@id="confirm_password"]').send_keys(test_admin_password)
		self.driver.find_element_by_xpath('//*[@id="submit"]').click()
		time.sleep(1)

		self.driver.find_element_by_xpath('/html/body/div[1]/a[1]').click()
		time.sleep(1)

		self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(test_admin_email)
		self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(test_admin_password)
		self.driver.find_element_by_xpath('//*[@id="submit"]').click()
		time.sleep(2)

		# Click new entry
		self.driver.find_element_by_xpath('/html/body/div[1]/a[2]').click()
		assert url_for("new_entry") in self.driver.current_url
		time.sleep(3)
		# Fill in new entry form
		self.driver.find_element_by_xpath('/html/body/div[2]/form/input[2]').send_keys(test_first_name)
		self.driver.find_element_by_xpath('//*[@id="surname"]').send_keys(test_surname)
		self.driver.find_element_by_xpath('//*[@id="title"]').send_keys(test_title)
		self.driver.find_element_by_xpath('/html/body/div[2]/form/input[5]').send_keys(test_pages)
		self.driver.find_element_by_xpath('/html/body/div[2]/form/input[6]').send_keys(test_language )
		self.driver.find_element_by_xpath('//*[@id="submit"]').click()
		time.sleep(3)
		# Assert that browser redirects to main page
		# assert url_for('main_lib') in self.driver.current_url

class Test_new_rate(TestBase):
	def test_rate(self):
		self.driver.find_element_by_xpath("/html/body/div[1]/a[2]").click()
		time.sleep(1)

		# Fill in registration form
		self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(test_admin_email)
		self.driver.find_element_by_xpath('//*[@id="first_name"]').send_keys(test_admin_first_name)
		self.driver.find_element_by_xpath('//*[@id="last_name"]').send_keys(test_admin_last_name)
		self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(test_admin_password)
		self.driver.find_element_by_xpath('//*[@id="confirm_password"]').send_keys(test_admin_password)
		self.driver.find_element_by_xpath('//*[@id="submit"]').click()
		time.sleep(1)

		self.driver.find_element_by_xpath('/html/body/div[1]/a[1]').click()
		time.sleep(1)

		self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(test_admin_email)
		self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(test_admin_password)
		self.driver.find_element_by_xpath('//*[@id="submit"]').click()
		time.sleep(2)

		# Click new entry
		self.driver.find_element_by_xpath('/html/body/div[1]/a[3]').click()
		assert url_for("rate") in self.driver.current_url
		time.sleep(3)
		# Fill in new entry form
		self.driver.find_element_by_xpath('//*[@id="rating"]').send_keys(2)
		self.driver.find_element_by_xpath('//*[@id="comment"]').send_keys('test')
		self.driver.find_element_by_xpath('//*[@id="submit"]').click()
		time.sleep(3)

# class Test_update_entries(TestBase):
# 	def test_update_lib(self):
# 		self.driver.find_element_by_xpath("/html/body/div[1]/a[2]").click()
# 		time.sleep(1)

# 		# Fill in registration form
# 		self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(test_admin_email)
# 		self.driver.find_element_by_xpath('//*[@id="first_name"]').send_keys(test_admin_first_name)
# 		self.driver.find_element_by_xpath('//*[@id="last_name"]').send_keys(test_admin_last_name)
# 		self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(test_admin_password)
# 		self.driver.find_element_by_xpath('//*[@id="confirm_password"]').send_keys(test_admin_password)
# 		self.driver.find_element_by_xpath('//*[@id="submit"]').click()
# 		time.sleep(1)

# 		self.driver.find_element_by_xpath('/html/body/div[1]/a[1]').click()
# 		time.sleep(1)

# 		self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(test_admin_email)
# 		self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(test_admin_password)
# 		self.driver.find_element_by_xpath('//*[@id="submit"]').click()
# 		time.sleep(2)

# 		# Click update entry
# 		self.driver.find_element_by_xpath('/html/body/div[5]/p/a[1]').click()
# 		assert url_for("update_lib/<book_id>") in self.driver.current_url
# 		time.sleep(3)
# 		# Fill in new entry form
# 		self.driver.find_element_by_xpath('/html/body/div[2]/form/input[2]').send_keys(test_update_first_name)
# 		self.driver.find_element_by_xpath('//*[@id="surname"]').send_keys(test_update_surname)
# 		self.driver.find_element_by_xpath('//*[@id="title"]').send_keys(test_update_title)
# 		self.driver.find_element_by_xpath('/html/body/div[2]/form/input[5]').send_keys(test_update_pages)
# 		self.driver.find_element_by_xpath('/html/body/div[2]/form/input[6]').send_keys(test_language )
# 		self.driver.find_element_by_xpath('//*[@id="submit"]').click()
# 		time.sleep(3)

# # 	# the deleting a book
# 	def test_delete_books(self):
# 		self.driver.find_element_by_xpath('/html/body/div[5]/p/a[1]').click()
# 		time.sleep(1)

# 		# Fill in registration form
# 		self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(test_admin_email)
# 		self.driver.find_element_by_xpath('//*[@id="first_name"]').send_keys(test_admin_first_name)
# 		self.driver.find_element_by_xpath('//*[@id="last_name"]').send_keys(test_admin_last_name)
# 		self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(test_admin_password)
# 		self.driver.find_element_by_xpath('//*[@id="confirm_password"]').send_keys(test_admin_password)
# 		self.driver.find_element_by_xpath('//*[@id="submit"]').click()
# 		time.sleep(1)

# 		self.driver.find_element_by_xpath('/html/body/div[5]/p/a[1]').click()
# 		time.sleep(1)

# 		self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(test_admin_email)
# 		self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(test_admin_password)
# 		self.driver.find_element_by_xpath('//*[@id="submit"]').click()
# 		time.sleep(2)

# 		# Click update entry
# 		self.driver.find_element_by_xpath('/html/body/div[5]/p/a[2]').click()
# 		assert url_for("delete_book/<book_id>") in self.driver.current_url
# 		time.sleep(3)
# 		# Fill in new entry form
# 		self.driver.find_element_by_xpath('/html/body/div[2]/form/input[2]').send_keys(test_update_first_name)
# 		self.driver.find_element_by_xpath('//*[@id="surname"]').send_keys(test_update_surname)
# 		self.driver.find_element_by_xpath('//*[@id="title"]').send_keys(test_update_title)
# 		self.driver.find_element_by_xpath('/html/body/div[2]/form/input[5]').send_keys(test_update_pages)
# 		self.driver.find_element_by_xpath('/html/body/div[2]/form/input[6]').send_keys(test_language )
# 		self.driver.find_element_by_xpath('//*[@id="submit"]').click()
# 		time.sleep(3)

if __name__ == "__main__":
	unittest.main(port=5000)

