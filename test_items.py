from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import math
import os 
import pytest

def test_contains_the_add_to_cart_button(browser):
    
    link1 = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link1)
    butt = browser.find_element_by_css_selector("button.btn-add-to-basket")
    time.sleep(10)
   
    assert butt is not None, 'Кнопка не найдена'
    #if butt !=None:
    #    print("Кнопка найдена")
    
if __name__ == "__main__":
    test_contains_the_add_to_cart_button(browser)
    print("All tests passed!")    

