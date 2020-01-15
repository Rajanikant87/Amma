from selenium.webdriver.common.by import By


class RadioButtonDemo:

    def __init__(self,driver):
        self.driver = driver

    InputForms = (By.XPATH, "//a[text()='Input Forms']")
    RadioButtonLInk = (By.LINK_TEXT, "Radio Buttons Demo")
    Rcheck1 = (By.XPATH, "//label[@class='radio-inline']")

    def LinkForm1(self):
        return self.driver.find_element(*RadioButtonDemo.InputForms)

    def RadiobuttonList(self):
        return self.driver.find_element(*RadioButtonDemo.RadioButtonLInk)

    def RadioOption(self):
        Roption = self.driver.find_elements(*RadioButtonDemo.Rcheck1)
        for i in Roption:
            print(i.text)
            if i.text == "Male":
                i.click()
            elif i.text == "5 to 15":
                i.click()


