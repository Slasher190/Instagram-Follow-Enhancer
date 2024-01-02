from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# import time

class Instagram: 
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()

    def diver_initialization(self, url: str):
        self.driver.get(url)
    
    def close_driver(self):
        self.driver.quit()
        
    def login_instagram(self, user_name: str, password: str):
        
        user_name_ = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "._aa48 input[name='username']")))
        user_name_.send_keys(user_name)
        
        password_ = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "._aa48 input[name='password']")))
        password_.send_keys(password)
        
        login = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "._acan._acap._acas._aj1-._ap30")))
        login.click()
        
        not_now = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".x1i10hfl.xjqpnuy")))
        not_now.click()
        
        not_now_notification = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "._a9--._ap36._a9_1")))
        not_now_notification.click()