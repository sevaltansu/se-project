import time

import pytest
from selenium.webdriver.common.by import By


class TestLoginPage:
    def test_valid_login(self,driver):
        driver.get("https://www.saucedemo.com/")
        time.sleep(2)

        username_input=driver.find_element(By.ID,"user-name")
        username_input.send_keys("standard_user")

        password_input=driver.find_element(By.ID,"password")
        password_input.send_keys("secret_sauce")

        login_btn=driver.find_element(By.ID,"login-button")
        login_btn.click()

        actual_url=driver.current_url
        assert actual_url=="https://www.saucedemo.com/inventory.htmls" #introducing an issue

        time.sleep(2)


    @pytest.mark.parametrize("username,password,error",[
        ("locked_out_user","secret_sauce","Epic sadface: Sorry, this user has been locked out."),
        ("invalidUser", "invalidPass", "Epic sadface: Username and password do not match any user in this service")])
    def test_invalid_login(self,driver,username,password,error):
        driver.get("https://www.saucedemo.com/")
        time.sleep(2)

        username_input=driver.find_element(By.ID,"user-name")
        username_input.send_keys(username)

        password_input=driver.find_element(By.ID,"password")
        password_input.send_keys(password)

        login_btn=driver.find_element(By.ID,"login-button")
        login_btn.click()

        error_msg_h3=driver.find_element(By.TAG_NAME, "h3")
        error_msg_text=error_msg_h3.text
        assert error_msg_text==error

        time.sleep(2)
