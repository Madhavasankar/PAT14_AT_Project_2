import pytest
from Test_Utilities.Hrm_functionalities import HrmFunctionalities


class TestCase3:

    def test_tc_pim_03(self):
        """
        This Test case deals header validation on Main menu Page of OrangeHRM.
        :return: It reruns the Successful text if all elements are visible.
        """
        _expected_text = "Successful"  # expected text
        validation_text = HrmFunctionalities().main_menu_validation_on_admin_page()  # actual text
        assert validation_text == _expected_text  # Validating both expected and actual msgs equal or  not
        print("Main menu validation on admin page done successful")  # printing the validation successful text
