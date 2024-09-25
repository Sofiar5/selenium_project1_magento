import pytest
from selenium.webdriver.common.by import By
import time
import allure


# Constants
LOGIN_URL = "https://magento.softwaretestingboard.com/customer/account/login/"
ACCOUNT_URL = "https://magento.softwaretestingboard.com/customer/account/"
EMAIL = "sofiavetisyan22@gmail.com"
PASSWORD = "AGBU123!@#"
NEW_PASSWORD = "AGBU123!@#"


@pytest.mark.regression
@allure.title("Test for invalid login")
def test_invalid_login(driver):
    with allure.step("Open the login page"):
        driver.get(LOGIN_URL)

    with allure.step("Enter an invalid email"):
        email_input = driver.find_element(By.ID, "email")
        email_input.send_keys("invalidemail@gmail.com")

    with allure.step("Enter an invalid password"):
        password_input = driver.find_element(By.ID, "pass")
        password_input.send_keys("invalidpass")

    with allure.step("Click the 'Login' button"):
        login_button = driver.find_element(By.ID, "send2")
        login_button.click()

    time.sleep(3)

    with allure.step("Check for error message"):
        error_message = driver.find_element(By.XPATH,
                                            "//div[contains(@class, 'message-error')]")
        assert "Please wait and try again later" in error_message.text
        allure.attach(driver.get_screenshot_as_png(), name="Invalid Login Screenshot",
                      attachment_type=allure.attachment_type.PNG)

@pytest.mark.smoke
@pytest.mark.regression
@allure.title("Test for successful login")
def test_login(driver):
    with allure.step("Open the login page"):
        driver.get(LOGIN_URL)

    with allure.step("Enter a valid email"):
        email_input = driver.find_element(By.ID, "email")
        email_input.send_keys(EMAIL)

    with allure.step("Enter a valid password"):
        password_input = driver.find_element(By.ID, "pass")
        password_input.send_keys(PASSWORD)

    with allure.step("Click the 'Login' button"):
        login_button = driver.find_element(By.ID, "send2")
        login_button.click()

    time.sleep(3)

    with allure.step("Verify user is redirected to the account page"):
        assert driver.current_url == ACCOUNT_URL
        allure.attach(driver.get_screenshot_as_png(), name="Login Success Screenshot",
                      attachment_type=allure.attachment_type.PNG)

@pytest.mark.regression
@allure.title("Test for changing password with incorrect current password")
def test_change_password_incorrect_current(driver):
    with allure.step("Open the account page"):
        driver.get(ACCOUNT_URL)
    with allure.step("Navigate to the change password page"):
        change_password_link = driver.find_element(By.LINK_TEXT, "Change Password")
        change_password_link.click()

    with allure.step("Enter an incorrect current password"):
        current_password_input = driver.find_element(By.ID, "current-password")
        current_password_input.send_keys("incorrectpassword")

    with allure.step("Enter a new password"):
        new_password_input = driver.find_element(By.ID, "password")
        new_password_input.send_keys(NEW_PASSWORD)

    with allure.step("Confirm the new password"):
        confirm_new_password_input = driver.find_element(By.ID, "password-confirmation")
        confirm_new_password_input.send_keys(NEW_PASSWORD)

    with allure.step("Save the changes"):
        save_button = driver.find_element(By.XPATH, "//button[@title='Save']")
        save_button.click()

    time.sleep(3)

    with allure.step("Verify error message for incorrect current password"):
        error_message = driver.find_element(By.XPATH,
                                            "//div[contains(@class, 'message-error')]")
        assert "The password doesn't match this account." in error_message.text
        allure.attach(driver.get_screenshot_as_png(),
                      name="Incorrect Current Password Screenshot",
                      attachment_type=allure.attachment_type.PNG)

@pytest.mark.regression
@allure.title("Test for password mismatch confirmation")
def test_change_password_mismatch(driver):
    with allure.step("Open the account page"):
        driver.get(ACCOUNT_URL)

    with allure.step("Navigate to the change password page"):
        change_password_link = driver.find_element(By.LINK_TEXT, "Change Password")
        change_password_link.click()

    with allure.step("Enter the correct current password"):
        current_password_input = driver.find_element(By.ID, "current-password")
        current_password_input.send_keys(PASSWORD)

    with allure.step("Enter a new password"):
        new_password_input = driver.find_element(By.ID, "password")
        new_password_input.send_keys(NEW_PASSWORD)

    with allure.step("Enter a mismatched confirmation password"):
        confirm_password_input = driver.find_element(By.ID, "password-confirmation")
        confirm_password_input.send_keys("mismatchedpassword")

    with allure.step("Save the changes"):
        save_button = driver.find_element(By.XPATH, "//button[@title='Save']")
        save_button.click()

    time.sleep(3)

    with allure.step("Verify error message for mismatched passwords"):
        error_message = driver.find_element(By.ID, "password-confirmation-error")
        assert "Please enter the same value again." in error_message.text
        allure.attach(driver.get_screenshot_as_png(),
                      name="Password Mismatch Screenshot",
                      attachment_type=allure.attachment_type.PNG)

@pytest.mark.smoke
@pytest.mark.regression
@allure.title("Test for successful password change")
def test_change_password(driver):
    with allure.step("Open the account page"):
        driver.get(ACCOUNT_URL)

    with allure.step("Navigate to the change password page"):
        change_password_link = driver.find_element(By.LINK_TEXT, "Change Password")
        change_password_link.click()

    with allure.step("Enter the correct current password"):
        current_password_input = driver.find_element(By.ID, "current-password")
        current_password_input.send_keys(PASSWORD)

    with allure.step("Enter the new password"):
        new_password_input = driver.find_element(By.ID, "password")
        new_password_input.send_keys(NEW_PASSWORD)

    with allure.step("Confirm the new password"):
        confirm_password_input = driver.find_element(By.ID, "password-confirmation")
        confirm_password_input.send_keys(NEW_PASSWORD)

    with allure.step("Save the changes"):
        save_button = driver.find_element(By.XPATH, "//button[@title='Save']")
        save_button.click()

    with allure.step("Verify success message"):
        success_message = driver.find_element(By.XPATH,
                                              "//div[contains(@class, 'message-success')]")
        assert "You saved the account information." in success_message.text
        allure.attach(driver.get_screenshot_as_png(),
                      name="Password Change Success Screenshot",
                      attachment_type=allure.attachment_type.PNG)