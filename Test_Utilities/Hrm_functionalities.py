from Test_Data import user_credentials
from Test_Locators.locators import LoginPageLocators
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.support.select import Select


class HrmFunctionalities:
    def __init__(self):
        self.driver = webdriver.Edge()
        self.my_wait = WebDriverWait(self.driver, 10)
        self.locators = LoginPageLocators
        self.url = user_credentials.url
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(5)

    def login_to_orangehrm(self):
        """
        This function is for Logging into OrangeHRM
        :return: None
        """
        username_ele = self.my_wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, self.locators.username_ele_xpath)))  # getting user name Element
        username_ele.send_keys(user_credentials.user_name)  # giving input to the user
        password_ele = self.my_wait.until(
            EC.visibility_of_element_located((By.NAME, self.locators.password_ele_name_tag)))  # locating the password
        password_ele.send_keys(user_credentials.password)  # input giving to the password Element
        login_btn_ele = self.my_wait.until(EC.element_to_be_clickable((By.XPATH, self.locators.login_btn_xpath)))
        login_btn_ele.click()  # clicking on login button
        sleep(5)
        return None
        # print(self.driver.title)

    def reset_password_functionality(self):
        """
        This function is for reset password in OrangeHRM.
        :return: it returns a reset link text.
        """
        forget_password_btn_ele = self.my_wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.forget_password_btn_xpath)))
        forget_password_btn_ele.click()
        username_ele = self.my_wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, self.locators.username_ele_xpath)))  # getting user name Element
        username_ele.send_keys(user_credentials.user_name)  # giving input to the user
        reset_password_btn_ele = self.my_wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.reset_password_btn_xpath)))
        reset_password_btn_ele.click()

        reset_link_text_ele = self.my_wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.reset_text_link_xpath)))
        reset_text = reset_link_text_ele.text
        return reset_text

    def header_validation_on_admin_page(self):
        """
        This function deals with the header validation on admin page.
        Whether the all elements are displayed or not.
        :return: It returns successful message if all elements are displayed.
        """
        self.login_to_orangehrm()  # logging into OrangeHRM
        title = self.driver.title  # getting the title after logging into the OrangeHRM
        actual_title = "OrangeHRM"  # expected title

        """
        Comparing the title of the OrangeHRM with the expected title.
        If both are same then it is goes to header validation on Admin page.
        """

        if title == actual_title:
            admin_ele = self.my_wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.locators.admin_ele_xpath)))  # getting the admin page element in main menu
            admin_ele.click()  # clicking on the admin page menu
            list1 = user_credentials.list1
            # getting the list from user_credentials.py file which os contains the list of elements that are need to
            # validate.
            length = len(list1)  # getting the length of list1
            list2 = []  # creating an empty list

            """
            In the below for loop I'm accessing the ul --> unordered list item in Admin page..
            Then by using indexing.. accessing the each element in ul.
            Getting the text from each element.
            Then I'm validating the text of element with list of given inputs.
            If the element text and given input are same then I'm adding the "True" to the empty list2.
            After validating the all elements converting the list2 into set then all the duplicate item are eliminated.
            If all elements are visible then the set1 contain only on true item in it..
            finally getting the length of set if it equal to 1 then return Successful else it will return false. 
            """

            for i in range(1, length + 1):
                ele = self.my_wait.until(
                    EC.visibility_of_element_located(
                        (By.XPATH, self.locators.xpath_for_ul_element + "[" + str(
                            i) + "]")))  # getting the elements in ul by using indexing.
                actual = list1[(i - 1)]  # getting item from list1 by using indexing.
                if ele.text == actual:  # validating the element text and given input equal or not.
                    list2.append("True")  # if both are equal appending True to list2
                else:
                    list2.append("False")  # if both are not equal appending False to list2

            set1 = set(list2)  # converting the list into set. Then the duplicates are eliminated.
            # if all elements are present the set1 will contain only one True item.
            # So comparing the length of set is equal to 1 or not.
            if len(set1) == 1:
                return "Successful"  # if it is equal to 1 then returns Successful

            else:
                return "Unsuccessful"  # if it is not equal to 1 then returns Unsuccessful
        else:  # if the title of the page and expected title both are not same then it will return None.
            return None

    def main_menu_validation_on_admin_page(self):
        """
        This function deals with the header validation on Main menu.
        Whether the all elements are displayed or not.
        :return: It returns successful message if all elements are displayed.
        """
        self.login_to_orangehrm()  # logging into OrangeHRM
        list1 = user_credentials.list2
        # getting the list from user_credentials.py file which os contains the list of elements that are need to
        # validate.
        length = len(list1)  # getting the length of the list.

        list2 = []  # creating an empty list.

        """
        In the below for loop I'm accessing the ul --> unordered list item in Main menu..
        Then by using indexing.. accessing the each element in ul.
        Getting the text from each element.
        Then I'm validating the text of element with list of given inputs.
        If the element text and given input are same then I'm adding the "True" to the empty list2.
        After validating the all elements I'm converting the list2 into set..then all the duplicate item are eliminated.
        If all elements are visible then the set contain only on true item in it..
        finally getting the length of set if it equal to 1 then return Successful else it will return false. 
        """

        for i in range(1, length + 1):
            ele = self.my_wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.locators.admin_menu_xpath + "[" + str(
                        i) + "]")))  # getting the elements in ul by using indexing.
            actual = list1[(i - 1)]  # getting item from list1 by using indexing.
            if ele.text == actual:  # validating the element text and given input equal or not.
                list2.append("True")  # if both are equal appending True to list2
            else:
                list2.append("False")  # if both are not equal appending False to list2

        set1 = set(list2)  # converting the list into set. Then the duplicates are eliminated.
        # if all elements are present the set1 will contain only one True item.
        if len(set1) == 1:  # So comparing the length of set is equal to 1 or not.
            return "Successful"  # if it is equal to 1 then returns successful
        else:
            return "Unsuccessful"  # if it is not equal to 1 then returns Unsuccessful
