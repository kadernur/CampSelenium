from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date
class Test_DemoClass:
    
    #her testten önce çağrılır
    def setup_method(self):
        
        self.driver= webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        
        self.folderPath=str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)
        
        
    
    #her testten sonra çağrılır.
    def teardown_method(self):
        self.driver.quit()
        
    def test_demoFunc(self):
       
       #3A action arrange assert
       
       text="Hello"
       assert text=="Hello" 
       
       
    @pytest.mark.parametrize("username,password",[("1","1"),("kullaniciadim","sifrem")])   
    def test_invalid_login(self,username,password):
         # en fazla 5 saniye olacak şekilde user-name id'li elementin görünmesini bekle
        self.waitForElementVisible((By.ID,"user-name"))
        # inputlara id ile erişim
        usernameInput = self.driver.find_element(By.ID, "user-name")
    
        self.waitForElementVisible((By.ID,"password"),3)
        passwordInput = self.driver.find_element(By.ID, "password")

        # input alanlarına veri gönderme
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)

        # login butonuna id ile erişim
        loginBtn = self.driver.find_element(By.ID, "login-button")

        # click ile butonun tıklanma işlevi
        loginBtn.click()

        # Xpath ile mesaja erisim
        errorMessage = self. driver.find_element( By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        # mesaj kontrolü
        
        #ScreenShot
        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login-{username}-{password}.png")
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        # sonucun ekrana yazırılması



    def waitForElementVisible(self,locator,timeout=5):
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(locator))
