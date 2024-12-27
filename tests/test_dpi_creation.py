import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

chrome_driver_path = "C:\Program Files\chromedriver"  # Provide the path to your chromedriver
driver = webdriver.Chrome()

class CreateDpiTest(StaticLiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Chrome()  # Use ChromeDriver
        self.selenium.implicitly_wait(10)

    def tearDown(self):
        self.selenium.quit()

    def test_create_dpi(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/dpi/create/'))  # Navigate to DPI creation page

        # Fill the form fields
        dpi_name_field = self.selenium.find_element(By.NAME, 'name')
        dpi_name_field.send_keys('Test DPI Name')

        # Submit the form
        submit_button = self.selenium.find_element(By.XPATH, '//*[@type="submit"]')
        submit_button.click()

        # Wait for the page to load
        time.sleep(2)

        # Check if DPI was created
        success_message = self.selenium.find_element(By.CLASS_NAME, 'success-message')
        self.assertIn('DPI created successfully', success_message.text)

if __name__ == '__main__':
    CreateDpiTest()
