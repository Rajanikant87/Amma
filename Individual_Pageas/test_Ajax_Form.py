from selenium.webdriver.common.by import By


class TestAjaxForm:

    def __init__(self, driver):
        self.driver = driver

    InputForms = (By.XPATH, "//a[text()='Input Forms']")
    AjaxtForm = (By.LINK_TEXT,"Ajax Form Submit")
    Name = (By.ID, "title")
    Comment = (By.ID, "description")
    Sbutton = (By.ID, "btn-submit")

    def test_LinkForm(self):
        return self.driver.find_element(*TestAjaxForm.InputForms)

    def test_AjaxFormLoading(self):
        return self.driver.find_element(*TestAjaxForm.AjaxtForm)

    def test_NameField(self):
        return self.driver.find_element(*TestAjaxForm.Name)

    def test_Comments(self):
        return self.driver.find_element(*TestAjaxForm.Comment)

    def test_Sbutton(self):
        return self.driver.find_element(*TestAjaxForm.Sbutton)

