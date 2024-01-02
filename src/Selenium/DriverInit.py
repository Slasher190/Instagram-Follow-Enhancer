from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class DriverInitialization: 
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()

    def diver_initialization(self, url: str):
        self.driver.get(url)
        time.sleep(2)
    
    def close_driver(self):
        self.driver.quit()
        
    def login_instagram(self):
        print("successful...")