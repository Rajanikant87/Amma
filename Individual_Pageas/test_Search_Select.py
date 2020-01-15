from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestSearchSelect:

    def __init__(self,driver):
        self.driver = driver

    InputForms = (By.XPATH, "//a[text()='Input Forms']")
    Jqr = (By.LINK_TEXT, "JQuery Select dropdown")
    SelectField = (By.XPATH, "//span[@class='select2-selection__arrow']")
    Values = (By.XPATH, "//select[@id='country']/option")

    def test_LinkForm3(self):
        return self.driver.find_element(*TestSearchSelect.InputForms)

    def test_SeachLink(self):
        return self.driver.find_element(*TestSearchSelect.Jqr)

    def test_searchfield(self):
        return self.driver.find_element(*TestSearchSelect.SelectField)

    def test_valuesofList(self):
        vlist = self.driver.find_elements(*TestSearchSelect.Values)
        for i in vlist:
            print(i.text)
            if i.text == "Denmark":
                return i

