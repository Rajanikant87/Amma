import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def Setup(request):

    driver = webdriver.Chrome(executable_path="D:\chromedriver.exe")
    driver.get("https://www.seleniumeasy.com/test/basic-checkbox-demo.html")
    driver.maximize_window()
    request.cls.driver = driver

    yield
    driver.close()
