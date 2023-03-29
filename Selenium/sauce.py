from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from constants import globalConstants

class Test_Sauce:
    
    def __init__(self):
        self. driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get(globalConstants.URL)
        
    #kişinin doğru giriş yapmadığı test senaryosu
    def test_invalid_login(self):
       
    
        #en fazla 5 saniye olacak şekilde user-name id'li elementin görünmesini bekle
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        
        
        #inputlara id ile erişim
        usernameInput = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "password")))
        
        passwordInput = self.driver.find_element(By.ID, "password")
      
        #input alanlarına veri gönderme
        usernameInput.send_keys("1")
        passwordInput.send_keys("1")
        
        #login butonuna id ile erişim
        loginBtn = self.driver.find_element(By.ID, "login-button")
        
        #click ile butonun tıklanma işlevi
        loginBtn.click()
        
        #Xpath ile mesaja erisim
        errorMessage = self. driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        #mesaj kontrolü
        testResult = errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        #sonucun ekrana yazırılması
        print(f"Test Sonucu: {testResult}")
    
    
    def test_valid_login(self):
        #giriş sayfasının yenilenmesi
        self.driver.get(globalConstants.URL)
        
        # en fazla 5 saniye olacak şekilde user-name id'li elementin görünmesini bekle
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "user-name")))

        
        usernameInput = self.driver.find_element(By.ID, "user-name")
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "password")))

        passwordInput = self.driver.find_element(By.ID, "password")
         
         # Action Chains
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput, "standard_user")
        actions.send_keys_to_element(passwordInput, "secret_sauce")
        actions.perform()
        # usernameInput.send_keys("standard_user")
        # passwordInput.send_keys("secret_sauce")

        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        
        #javaScript execute edilme işlevi
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(20)
        
 
 



testClass = Test_Sauce()
testClass.test_invalid_login()
testClass.test_valid_login()
