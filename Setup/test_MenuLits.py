import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from Individual_Pageas.test_Ajax_Form import TestAjaxForm
from Individual_Pageas.test_Checkbox import Checkboxlink
from Individual_Pageas.test_Contact_Us import TestContactUs
from Individual_Pageas.test_Dropdown import DropdownList
from Individual_Pageas.test_InputForms import TestTextField
from Individual_Pageas.test_RadioButton import RadioButtonDemo
from Individual_Pageas.test_Search_Select import TestSearchSelect
from Utilities.test_Base_Class import TestBaseClass
import datetime


class TestMenuLists(TestBaseClass):

    def test_InputFiles(self):
        obj = TestTextField(self.driver)
        obj.test_LinkForm().click()
        obj.test_Simple_Form_Demo().click()
        obj.test_MessageField()
        obj.test_Show_Message_Button().click()
        obj.test_display()
        obj.test_LinkForm().click()

    def test_Checkbox(self):
        check = Checkboxlink(self.driver)
        check.CheckBox_Link().click()
        check.single_Checkbox().click()
        check.Multiple_Checkboxes()

    def test_RadioButtons(self):
        Radio = RadioButtonDemo(self.driver)
        Radio.LinkForm1().click()
        Radio.RadiobuttonList().click()
        Radio.RadioOption()

    def test_Dvalues(self):
        Sv = DropdownList(self.driver)
        Sv.LinkForm2().click()
        Sv.DrpListLink().click()
        s1 = Select(Sv.DrpVales())
        s1.select_by_index(3)
        time.sleep(2)

    def test_ContactUs(self):
        CU = TestContactUs(self.driver)
        CU.LinkForm2().click()
        CU.test_InputFormSubmission_Link().click()
        CU.test_FirstName().send_keys("Asha")
        CU.test_LastName().send_keys("Jamadar")
        s3 = Select(CU.test_DrpList())
        s3.select_by_index(3)
        time.sleep(2)

    def test_AjaxFormLoading(self):
        Ax = TestAjaxForm(self.driver)
        Ax.test_LinkForm().click()
        Ax.test_AjaxFormLoading().click()
        Ax.test_NameField().send_keys("Welcome")
        Ax.test_Comments().send_keys("Hurry Up...!!!")
        Ax.test_Sbutton().click()
        time.sleep(2)

    def test_Jquery(self):
        Jq = TestSearchSelect(self.driver)
        Jq.test_LinkForm3().click()
        Jq.test_SeachLink().click()
        time.sleep(2)
        Jq.test_searchfield().click()
        Jq.test_valuesofList().click()







