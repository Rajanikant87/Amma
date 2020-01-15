from selenium.webdriver.common.by import By


class TestContactUs:

    def __init__(self, driver):
        self.driver = driver

    InputForms = (By.XPATH, "//a[text()='Input Forms']")
    InputFormSubmission = (By.LINK_TEXT, "Input Form Submit")
    FName = (By.XPATH, "//input[@placeholder='First Name']")
    LName = (By.XPATH, "//input[@placeholder='Last Name']")
    Dpd = (By.XPATH, "//select[@name='state']")

    def LinkForm2(self):
        return self.driver.find_element(*TestContactUs.InputForms)

    def test_InputFormSubmission_Link(self):
        return self.driver.find_element(*TestContactUs.InputFormSubmission)

    def test_FirstName(self):
        return self.driver.find_element(*TestContactUs.FName)

    def test_LastName(self):
        return self.driver.find_element(*TestContactUs.LName)

    def test_DrpList(self):
        return self.driver.find_element(*TestContactUs.Dpd)

