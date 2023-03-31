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
from constants import globalConstants

class Test_SauceClass:
    
    def setup_method(self):
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get(globalConstants.URL)
        
        self.folderPath=str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)
        
        
    def teardown_method(self):
        self.driver.quit()
        
     
     #Kullanıcı adı ve şifre alanının boş girilmesi   
    def test_empty_username_password(self):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput=self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput=self.driver.find_element(By.ID,"password")
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
       
        self.driver.save_screenshot(f"{self.folderPath}/test_empty_username_password.png")
        assert errorMessage.text == "Epic sadface: Username is required"
        
        
     #sadece şifre alanının boş geçilmesi   
    def test_empty_password(self):
        self.waitForElementVisible((By.ID, "user-name"))
        usernameInput=self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput=self.driver.find_element(By.ID,"password")
        usernameInput.send_keys("1")
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        errorMessage =self.driver.find_element( By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        
        self.driver.save_screenshot(f"{self.folderPath}/test_empty_password.png")
        assert errorMessage.text == "Epic sadface: Password is required"
        
        
    # Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
    def test_locked_out_user(self):
        self.waitForElementVisible((By.ID, "user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID, "password"))
        passwordInput = self.driver.find_element(By.ID, "password")
        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        
        self.driver.save_screenshot(f"{self.folderPath}/test_locked_out_user.png")
        assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
       
    # Kullanıcı adı ve şifre alanları boş geçildiğinde bu iki inputun yanında da kırmızı "X" ikonu çıkmalıdır. Daha sonra aşağıda çıkan uyarı mesajının kapatma butonuna tıklandığında bu "X" ikonları kaybolmalıdır. (Tek test casede işleyiniz)
    def test_remove_error_icon(self):
        self.waitForElementVisible((By.ID, "user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID, "password"))
        passwordInput = self.driver.find_element(By.ID, "password")
        usernameInput.send_keys("")
        passwordInput.send_keys("")
        
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()

        errorIcon = self.driver.find_element(By.CLASS_NAME, "error-button")
        errorIcon.click()
    
        self.driver.save_screenshot(f"{self.folderPath}/test_remove_error_icon.png")
    
    #Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir.
        
    @pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce"), ("problem_user","secret_sauce"),("performance_glitch_user","secret_sauce")])
    def test_go_to_page(self,username,password):
        self.waitForElementVisible((By.ID, "user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID, "password"))
        passwordInput = self.driver.find_element(By.ID, "password")
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        
        self.driver.save_screenshot(f"{self.folderPath}/test-go_to_page-{username}-{password}.png")
        assert self.driver.current_url== "https://www.saucedemo.com/inventory.html"
        
        
    
    # Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.
        
    @pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce"), ("problem_user", "secret_sauce"), ("performance_glitch_user", "secret_sauce")])
    def test_len_of_the_item(self, username, password):
       self.waitForElementVisible((By.ID, "user-name"))
       usernameInput = self.driver.find_element(By.ID, "user-name")
       self.waitForElementVisible((By.ID, "password"))
       passwordInput = self.driver.find_element(By.ID, "password")
       usernameInput.send_keys(username)
       passwordInput.send_keys(password)
       loginBtn = self.driver.find_element(By.ID, "login-button")
       loginBtn.click()
       listOfItems = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
       self.driver.save_screenshot(f"{self.folderPath}/test-len_of_the_item-{username}-{password}.png")
       assert 6==len(listOfItems)
        
    
    
    #Logout kontrolü
    @pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce"), ("problem_user", "secret_sauce"), ("performance_glitch_user", "secret_sauce")])
    def test_logout(self,username,password):
       self.waitForElementVisible((By.ID, "user-name"))
       usernameInput = self.driver.find_element(By.ID, "user-name")
       self.waitForElementVisible((By.ID, "password"))
       passwordInput = self.driver.find_element(By.ID, "password")
       usernameInput.send_keys(username)
       passwordInput.send_keys(password)
       loginBtn = self.driver.find_element(By.ID, "login-button")
       loginBtn.click()
       
       self.waitForElementVisible((By.ID,"react-burger-menu-btn"))
       menu= self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[1]/div[1]/div/div[1]/div/button")
       menu.click()
       self.waitForElementVisible((By.ID,"logout_sidebar_link"))
       logoutBtn= self.driver.find_element(By.ID,"logout_sidebar_link")
       logoutBtn.click()
       self.driver.save_screenshot(f"{self.folderPath}/test-logout-{username}-{password}.png")
       assert self.driver.current_url == globalConstants.URL
       
       
       
    
    #Add to card/remove to card buton kontrolü
    
    @pytest.mark.parametrize("itemAdd,removeItem", [("add-to-cart-sauce-labs-backpack", "remove-sauce-labs-backpack"),
                                                    ("add-to-cart-sauce-labs-bike-light", "remove-sauce-labs-bike-light"),
                                                    ("add-to-cart-sauce-labs-bolt-t-shirt", "remove-sauce-labs-bolt-t-shirt")])
    def test_addToCart_removeToCart(self,itemAdd,removeItem):
        self.waitForElementVisible((By.ID, "user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID, "password"))
        passwordInput = self.driver.find_element(By.ID, "password")
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        self.waitForElementVisible((By.XPATH, "/html/body/div/div/div/div[2]/div/div"))
        ItemAdd = self.driver.find_element(By.ID, itemAdd)
        ItemAdd.click()
        
        self.waitForElementVisible((By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button"))
        RemoveItem = self.driver.find_element(By.ID, removeItem)
        RemoveItem.click()
        addtoCart = self.driver.find_element(By.XPATH,"//*[@id='add-to-cart-sauce-labs-backpack']")

        self.driver.save_screenshot(
            f"{self.folderPath}/test_addToCart_removeToCart-{itemAdd}-{removeItem}.png")
        assert addtoCart.text == "Add to cart"
       
       
       
       
    #bütün ürünlerin sepete eklenebilmesinin kontrolü
    
    def test_add_all_items(self):
        # self.waitForElementVisible((By.ID, "user-name"))
        # usernameInput = self.driver.find_element(By.ID, "user-name")
        # self.waitForElementVisible((By.ID, "password"))
        # passwordInput = self.driver.find_element(By.ID, "password")
        # usernameInput.send_keys("standard_user")
        # passwordInput.send_keys("secret_sauce")
        # loginBtn = self.driver.find_element(By.ID, "login-button")
        # loginBtn.click() 
        
        #yukarıdaki işlemlerin tekrarı olmaması için fonksiyon kullanıldı.
        self.test_go_to_page(username="standard_user",password="secret_sauce")
        self.waitForElementVisible((By.CLASS_NAME, 'btn_inventory'))
        Items = self.driver.find_elements(By.CLASS_NAME, "btn_inventory")
        for item in Items:
            item.click()
        
        self.waitForElementVisible((By.CLASS_NAME,"shopping_cart_container"))   
        
        cart= self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[1]/div[3]/a")
        cart.click()
        
        self.waitForElementVisible((By.CLASS_NAME,"cart_item"))
         
        cartItems= self.driver.find_elements(By.CLASS_NAME,"cart_item")
        
        self.driver.save_screenshot(f"{self.folderPath}/test_add_all_items.png")
        assert 6 ==len(cartItems)     
     
        
        
        
     #sepete ürün eklenditen sonra checkout işleminin kontrolü
     
    def test_order_checkout(self):
        self.test_add_all_items()
        self.waitForElementVisible((By.CLASS_NAME, "checkout_button"))
        checkoutBtn=self.driver.find_element(By.ID,"checkout")
        checkoutBtn.click()
        self.waitForElementVisible((By.ID,"checkout_info_container"))
        
        firstNameInput=self.driver.find_element(By.ID,"first-name")
        lastNameInput=self.driver.find_element(By.ID,"last-name")
        postalInput=self.driver.find_element(By.ID,"postal-code")
        
        firstNameInput.send_keys("Kader Nur")
        lastNameInput.send_keys("Tekin")
        postalInput.send_keys("1234")
        
        continueBtn=self.driver.find_element(By.ID,"continue")
        continueBtn.click()
        
        self.waitForElementVisible((By.ID,"finish"))
        finishBtn=self.driver.find_element(By.ID,"finish")
        finishBtn.click()
        self.waitForElementVisible((By.CLASS_NAME, 'complete-text'))
        successMessage = self.driver.find_element(By.CLASS_NAME, 'complete-text')
        
        self.driver.save_screenshot(f"{self.folderPath}/test_order_checkout.png")
        assert successMessage.text == "Your order has been dispatched, and will arrive just as fast as the pony can get there!"
        
        
        
        

    #checkout işlemi sırasında firstName alanının boş geçilmesi
    #bunun için ilk etapta bir fonksiyon yazıp checkout işlemlerini kapsamasını sağlamak istiyorum.
    def checkout(self):
        self.test_add_all_items()
        self.waitForElementVisible((By.CLASS_NAME, "checkout_button"))
        checkoutBtn = self.driver.find_element(By.ID, "checkout")
        checkoutBtn.click()
        self.waitForElementVisible((By.ID, "checkout_info_container"))

       

    def test_emptyfirstName_inCheckout(self):
        self.checkout()
        firstNameInput = self.driver.find_element(By.ID, "first-name")
        lastNameInput = self.driver.find_element(By.ID, "last-name")
        postalInput = self.driver.find_element(By.ID, "postal-code")

        lastNameInput.send_keys("Tekin")
        postalInput.send_keys("1234")
        
        continueBtn=self.driver.find_element(By.ID,"continue")
        continueBtn.click()
        errorMessage=self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/form/div[1]/div[4]/h3")
        
        self.driver.save_screenshot(f"{self.folderPath}/test_emptyfirstName_inCheckout.png")
        assert errorMessage.text == "Error: First Name is required"
        
         
    
    #checkout information sırasında cancel butonuyla sepete dönme kontrolü
    def test_fromCancelBtn_toCart(self):
        self.checkout()
        self.waitForElementVisible((By.ID,"cancel"))
        cancelBtn=self.driver.find_element(By.ID,"cancel")
        cancelBtn.click()
        self.waitForElementVisible((By.CLASS_NAME,"cart_footer"))
        
        self.driver.save_screenshot(f"{self.folderPath}/test_fromCancelBtn_toCart.png")
        assert self.driver.current_url == "https://www.saucedemo.com/cart.html"
       
     
     
     #filtreleme işlemi
     
    def test_filter_lowToHigh(self):
        self.test_go_to_page(username="standard_user", password="secret_sauce")
        self.waitForElementVisible((By.CLASS_NAME, "product_sort_container"))
        filterBtn = self.driver.find_element(By.CLASS_NAME, "product_sort_container")
        filterBtn.click()
        
        price_low_to_high=self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/span/select/option[3]")
        price_low_to_high.click()
        
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        
        expected_result=sorted([float(item.text[1:]) for item in items])
        
        actual_result = [float(item.text[1:]) for item in items]
        
        self.driver.save_screenshot(f"{self.folderPath}/test_test_filter_lowToHigh.png")
        assert actual_result == expected_result
        
        
        
        
         
        
        
    
    def waitForElementVisible(self,locator,timeout=5):
        WebDriverWait(self.driver,timeout).until(expected_conditions.visibility_of_element_located(locator))
    
    
    

    