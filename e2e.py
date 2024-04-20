import unittest
from selenium import webdriver


class TestAdminLogin(unittest.TestCase):
    def setUp(self):
        # Create a new instance of the Chrome driver
        self.driver = webdriver.Chrome()

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

    def test_valid_login(self):
        # Open the Django admin login page
        self.driver.get('http://localhost:8000/admin/')

        # Find the username input field and enter valid username
        username_element = self.driver.find_element(by='xpath', value='//input[@name="username"]')
        username_element.send_keys('admin')

        # Find the password input field and enter valid password
        password_element = self.driver.find_element(by='xpath', value='//input[@name="password"]')
        password_element.send_keys('your_password')

        # Find and click the Login button
        login_button = self.driver.find_element(by='xpath', value='//input[@type="submit"]')
        login_button.click()

        # Assert that we are redirected to the admin dashboard
        self.assertIn('admin', self.driver.current_url.lower())

    def test_invalid_login(self):
        # Open the Django admin login page
        self.driver.get('http://localhost:8000/admin/')

        # Find the username input field and enter invalid username
        username_element = self.driver.find_element(by='xpath', value='//input[@name="username"]')
        username_element.send_keys('invalid_username')

        # Find the password input field and enter invalid password
        password_element = self.driver.find_element(by='xpath', value='//input[@name="password"]')
        password_element.send_keys('invalid_password')

        # Find and click the Login button
        login_button = self.driver.find_element(by='xpath', value='//input[@type="submit"]')
        login_button.click()

        # Assert that we remain on the login page
        self.assertIn('login', self.driver.current_url.lower())


if __name__ == '__main__':
    unittest.main()
