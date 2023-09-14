import pytest
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from TestPageObjectModel.pages.login_page import LoginPage
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.wait import WebDriverWait



@pytest.fixture()
def driver():
    driver = webdriver.WebDriver()
    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()

def test_login(driver):
    login_page = LoginPage(driver)
    login_page.open_page('https://trytestingthis.netlify.app/')
    # time.sleep(1)
    login_page.enter_username('test')
    # time.sleep(1)
    login_page.enter_password('test')
    # time.sleep(1)
    login_page.click_login()
    # time.sleep(1)

    assert "Successful" in driver.page_source
    time.sleep(3)

