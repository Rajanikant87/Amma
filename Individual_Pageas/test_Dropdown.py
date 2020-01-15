from datetime import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DropdownList:

    def __init__(self, driver):
        self.driver = driver

    InputForms = (By.XPATH, "//a[text()='Input Forms']")
    DrpLink = (By.LINK_TEXT, "Select Dropdown List")
    DpList = (By.ID, "select-demo")
    MultiValue = (By.XPATH, "//select[@id='multi-select']")

    def LinkForm2(self):
        return self.driver.find_element(*DropdownList.InputForms)

    def DrpListLink(self):
        return self.driver.find_element(*DropdownList.DrpLink)

    def DrpVales(self):
        return self.driver.find_element(*DropdownList.DpList)









