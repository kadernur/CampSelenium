from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class Test_Sauce:
    #kişinin doğru giriş yapmadığı test senaryosu
    def test_invalid_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        
        #inputlara id ile erişim
        usernameInput = driver.find_element(By.ID,"user-name")
        passwordInput = driver.find_element(By.ID,"password")
      
        #input alanlarına veri gönderme
        usernameInput.send_keys("1")
        passwordInput.send_keys("1")
        sleep(2)
        #login butonuna id ile erişim
        loginBtn = driver.find_element(By.ID,"login-button")
        sleep(2)
        #click ile butonun tıklanma işlevi
        loginBtn.click()
        
        #Xpath ile mesaja erisim
        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        #mesaj kontrolü
        testResult = errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        #sonucun ekrana yazırılması
        print(f"Test Sonucu: {testResult}")
        sleep(100)
        
        
 



testClass = Test_Sauce()
testClass.test_invalid_login()
