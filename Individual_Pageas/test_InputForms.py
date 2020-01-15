from selenium.webdriver.common.by import By


class TestTextField:
    def __init__(self, driver):
        self.driver = driver

    InputForms = (By.XPATH, "//a[text()='Input Forms']")
    SimpleFormDemo = (By.LINK_TEXT,"Simple Form Demo")
    MessageField = (By.ID,"user-message")
    ShowMoreButton = (By.XPATH, "//button[text()='Show Message']")
    Message = (By.ID,"display")

    def test_LinkForm(self):
        return self.driver.find_element(*TestTextField.InputForms)

    def test_Simple_Form_Demo(self):
        return self.driver.find_element(*TestTextField.SimpleFormDemo)

    def test_MessageField(self):
        global MSGF
        MSGF = self.driver.find_element(*TestTextField.MessageField)
        MSGF.send_keys("Ome Shree")

    def test_Show_Message_Button(self):
        return self.driver.find_element(*TestTextField.ShowMoreButton)

    def test_display(self):
        Msg = self.driver.find_element(*TestTextField.Message).text
        assert MSGF.text in Msg