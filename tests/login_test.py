from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from TestPageObjectModel.pages.login_page import LoginPage
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service



@pytest.fixture()
def driver():
    service = Service(executable_path='D:/pythonProject/TestPageObjectModel/chromedriver.exe')
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, 10)
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
