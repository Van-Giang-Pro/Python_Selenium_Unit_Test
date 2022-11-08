import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import page


class PythonOrgSearch(unittest.TestCase):

	def setUp(self):
		chrome = Service('C:/Users/Admin/PycharmProjects/Python_Selenium_Unit_Test/chromedriver.exe')
		self.driver = webdriver.Chrome(service=chrome)
		self.driver.get("https://www.python.org")

	def test_example(self):
		print("Test")
		assert True

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()
