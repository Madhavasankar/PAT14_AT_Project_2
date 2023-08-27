import pytest
from Test_Utilities.Hrm_functionalities import HrmFunctionalities


class TestCase1:

    def test_tc_pim_01(self):
        """
        This Test case deals with the reset password on OrangeHRM.
        :return: It returns the Reset Password link sent successfully message
        """
        _expected_successful_msg = "Reset Password link sent successfully"  # expected msg
        success_text = HrmFunctionalities().reset_password_functionality()  # getting actual msg
        assert success_text == _expected_successful_msg  # validating both are equal or not
        print(success_text)  # printing the reset password link sent successfully msg
