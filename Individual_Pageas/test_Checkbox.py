from selenium.webdriver.common.by import By


class Checkboxlink:

    def __init__(self, driver):
        self.driver = driver

    ckLink = (By.LINK_TEXT, "Checkbox Demo")
    scheckbox = (By.ID, "isAgeSelected")
    checkboxes = (By.XPATH, "//div[@class='col-md-6 text-left']//div[2]//div[2]//div/label")

    def CheckBox_Link(self):
        return self.driver.find_element(*Checkboxlink.ckLink)

    def single_Checkbox(self):
        return self.driver.find_element(*Checkboxlink.scheckbox)

    def Multiple_Checkboxes(self):
        cList = self.driver.find_elements(*Checkboxlink.checkboxes)
        for i in cList:
            i.click()
            i.is_selected()
        self.driver.get_screenshot_as_file("Sampe.jpg")




