from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import sys


class presence_of_all_elements():
    def __init__(self, driver, locators_lst):
        self.driver = driver
        self.locators = locators_lst

    def __call__(self, driver):
        try:
            for locator in self.locators:
                element = self.driver.find_element(*locator)
            return True
        except:
            pass


def wait_to_click(driver, locator, timeout):
    element = WebDriverWait(driver, timeout).until(
        presence_of_all_elements(driver, [locator])
    )
    driver.find_element(*locator).click()


def wait_to_get_element(driver, locator, timeout):
    element = WebDriverWait(driver, timeout).until(
        presence_of_all_elements(driver, [locator])
    )
    return driver.find_element(*locator)



def wait_to_get_elements(driver, locator, timeout):
    element = WebDriverWait(driver, timeout).until(
        presence_of_all_elements(driver, [locator])
    )
    return driver.find_elements(*locator)



def try_until_success(callback, arg_lst=None, arg_dict=None, max_tries=None, reset=None,reset_arg_dict=None ):
    while True:
        try:
            if arg_lst is None and arg_dict is None:
                return callback()
            elif arg_dict is not None:
                return callback(**arg_dict)
            elif arg_lst is not None:
                return callback(*arg_lst)
            break
        except:
            e =sys.exc_info()[0]
            print(str(e), "=> Retrying...")
            if max_tries is not None:
                max_tries -= 1
                if max_tries < 1:
                    raise e
            if reset is not None:
                if reset_arg_dict is not None:
                    reset(**reset_arg_dict)
                else:
                    reset()

            

