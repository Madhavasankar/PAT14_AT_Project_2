import pytest
from Test_Utilities.Hrm_functionalities import HrmFunctionalities


class TestCase2:

    def test_tc_pim_02(self):
        """
        This Test case deals header validation on Admin Page of OrangeHRM.
        :return: It reruns the Successful text if all elements are visible.
        """
        _expected_validation_text = "Successful"  # expected message
        validation_text = HrmFunctionalities().header_validation_on_admin_page()  # actual message
        assert validation_text == _expected_validation_text  # validating both actual and
        # expected text is equal or not
        print("Headers validation on admin page done successfully")  # printing the validation successful msg
