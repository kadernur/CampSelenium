
# AMAÇ:

# Derste gösterilen konuların pekiştirilmesi.

# ÖDEV TANIMI:

# Aşağıda verilen test caselerin hepsini "https://www.saucedemo.com/" sitesinde gerçekleştirmeniz istenmektedir.

# Yazacağınız tüm kodları oluşturduğunuz bir classda fonksiyonlar oluşturarak gerçekleştiriniz. Bu classın fonksiyonlarını çağırarak test ediniz.

# Test Caseler

# Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.
# Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.
# Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
# Kullanıcı adı ve şifre alanları boş geçildiğinde bu iki inputun yanında da kırmızı "X" ikonu çıkmalıdır. Daha sonra aşağıda çıkan uyarı mesajının kapatma butonuna tıklandığında bu "X" ikonları kaybolmalıdır. (Tek test casede işleyiniz)
# Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir.
# Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By


class Test_Sauce:

    def empty_username_password(self):
     #driver bağlantısı ve siteye erişim
     driver= webdriver.Chrome(ChromeDriverManager().install())
     driver.maximize_window()
     driver.get("https://www.saucedemo.com/")
     
     #username ve password inputlarına locate olma
     usernameInput=driver.find_element(By.ID,"user-name")
     passwordInput=driver.find_element(By.ID,"password")
     
     #veri göndermeden login butonuna tıklama işlemi
     loginBtn=driver.find_element(By.ID,"login-button")
     sleep(2)
     loginBtn.click()
     sleep(1)
     
     errorMessage = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
     testResult = errorMessage.text == "Epic sadface: Username is required"
     print(f"Test Sonucu: {testResult}")
     sleep(100)
     
     
    def empyt_password(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput=driver.find_element(By.ID,"password")
        
        usernameInput.send_keys("1")
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()
        sleep(2)
        errorMessage= driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print("Şifre Yanlis senaryosu")
        print(f"Test Sonucu: {testResult}")
        sleep(100)
     
    
    
    def locked_out_user(self):
        driver= webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        usernameInput= driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        
        #ilgili alanlara istenilen değeri gönderme işlevi
        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        
        sleep(2)
        loginBtn=driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()
        errorMessage = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print("Locked")
        print(f"Test Sonucu: {testResult}")
        sleep(100)
        
        
    def remove_error_icon(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        usernameInput.send_keys("")
        passwordInput.send_keys("")
        sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()
        sleep(2)
        
        errorIcon =driver.find_element(By.CLASS_NAME,"error-button")
        errorIcon.click()
        print("Error Button")
        sleep(100)

 
    def go_to_page(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()
        sleep(2)
        redirected = "https://www.saucedemo.com/inventory.html"
        print(redirected)
        sleep(100)
        
        
        
    def len_of_the_item(self):
         driver = webdriver.Chrome(ChromeDriverManager().install())
         driver.maximize_window()
         driver.get("https://www.saucedemo.com/")
         usernameInput = driver.find_element(By.ID, "user-name")
         passwordInput = driver.find_element(By.ID, "password")
         usernameInput.send_keys("standard_user")
         passwordInput.send_keys("secret_sauce")
         sleep(2)
         loginBtn = driver.find_element(By.ID, "login-button")
         sleep(2)
         loginBtn.click()
         sleep(2)
         
         listOfItems=driver.find_elements(By.CLASS_NAME,"inventory_item")
         print(f"Number of the Items:, {len(listOfItems)}")

testClass = Test_Sauce()
# testClass.empty_username_password()
# testClass.empyt_password()
# testClass.locked_out_user()
# testClass.remove_error_icon()
#testClass.go_to_page()
testClass.len_of_the_item()

