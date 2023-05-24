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
import openpyxl
from GlobalConstants import constants
from selenium.webdriver.support.ui import Select

class Test_SauceDemoClass:
    
    def setup_method(self):
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get(constants.URL)
        self.folderPath=str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)
        
        
    def teardown_method(self):
        self.driver.quit()
        
    def waitForElementVisible(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))


    def getData1():
    # veriyi al
       return [("standard_user", "secret_sauce"), ("problem_user", "secret_sauce"), ("performance_glitch_user", "secret_sauce")]


    def getItem():
        return  [("add-to-cart-sauce-labs-backpack", "remove-sauce-labs-backpack"),
                                       ("add-to-cart-sauce-labs-bike-light",
                                        "remove-sauce-labs-bike-light"),
                                       ("add-to-cart-sauce-labs-bolt-t-shirt", "remove-sauce-labs-bolt-t-shirt")]

    def loginInform(self,username,password):
      self.waitForElementVisible((By.ID, constants.user_id))
      usernameInput = self.driver.find_element(By.ID, constants.user_id)
      self.waitForElementVisible((By.ID, constants.password_id))
      passwordInput = self.driver.find_element(By.ID, constants.password_id)
      usernameInput.send_keys(username)
      passwordInput.send_keys(password)
      loginBtn = self.driver.find_element(By.ID, constants.login_id).click()
        

    def saveScreenShoot(self, nameScreenShot):
        self.driver.save_screenshot(f"{self.folderPath}/{nameScreenShot}.png")

    # Kullanıcı adı ve şifre alanının boş girilmesi
    def test_empty_username_password(self):
        self.loginInform(username="",password="")   
        errorMessage = self.driver.find_element(By.XPATH, constants.empyt_login_Xpath)
        self.saveScreenShoot("test_empty_username_password")
        assert errorMessage.text == constants.empyt_login_message
        
        
     #sadece şifre alanının boş geçilmesi  
     
    def test_emty_password(self):
        self.loginInform(username="1",password="")
        errorMessage=self.driver.find_element(By.XPATH,constants.emty_passwordLogin_Xpath)
        self.saveScreenShoot("test_empty_password")
        assert errorMessage.text==constants.emty_passwordLogin_message
        
        
    # Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
    
    def test_locked_out_user(self):
     self.loginInform(username=constants.locked_user,password=constants.locked_password)
     errorMessage=self.driver.find_element(By.XPATH,constants.locked_outMessage_Xpath)
     self.saveScreenShoot("test_locked_out_user")
     assert errorMessage.text==constants.locked_outMessage
     
     
    # Kullanıcı adı ve şifre alanları boş geçildiğinde bu iki inputun yanında da kırmızı "X" ikonu çıkmalıdır. Daha sonra aşağıda çıkan uyarı mesajının kapatma butonuna tıklandığında bu "X" ikonları kaybolmalıdır. (Tek test casede işleyiniz)

    def test_remove_error_icon(self):
        self.loginInform(username=" ",password=" ")
        errorIcon = self.driver.find_element(By.CLASS_NAME,constants.errorIconClass_Name).click()
        self.saveScreenShoot("test_remove_error_icon")


   # Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir.
    @pytest.mark.parametrize("username,password",getData1())
    def test_go_to_page(self,username,password):
      self.loginInform(username,password)
      self.saveScreenShoot(f"{self.folderPath}/test-go_to_page-{username}-{password}.png")
      assert self.driver.current_url==constants.product_list_url
      
      
      
    # Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.

    @pytest.mark.parametrize("username,password", getData1())
    def test_len_of_the_item(self, username, password):
        self.loginInform(username,password)
        listOfItems = self.driver.find_elements(By.CLASS_NAME, constants.itemContainer_Classname)
        self.driver.save_screenshot(f"{self.folderPath}/test-len_of_the_item-{username}-{password}.png")
        assert 6==len(listOfItems)
        
        
    # Logout kontrolü
    @pytest.mark.parametrize("username,password", getData1())
    def test_logout(self, username, password):
        self.loginInform(username, password)
        self.waitForElementVisible((By.ID,constants.menu_id))
        menu=self.driver.find_element(By.XPATH,constants.menuBtn_Xpath).click()
        self.waitForElementVisible((By.ID,constants.logout_Id))
        logoutBtn=self.driver.find_element(By.ID,constants.logout_Id).click()
        self.driver.save_screenshot( f"{self.folderPath}/test-logout-{username}-{password}.png")
        assert self.driver.current_url == constants.URL
        

     # Add to card/remove to card buton kontrolü
    @pytest.mark.parametrize(" itemAdd, removeItem", getItem())
    def test_addToCart_removeToCart(self, itemAdd, removeItem):
        self.loginInform(username="standard_user",password="secret_sauce")
        ItemAdd = self.driver.find_element(By.ID, itemAdd).click()
        RemoveItem = self.driver.find_element(By.ID, removeItem).click()
        addtoCart = self.driver.find_element(By.XPATH, constants.labsBackpac_xpath)
        self.driver.save_screenshot(f"{self.folderPath}/test_addToCart_removeToCart-{itemAdd}-{removeItem}.png")
        assert addtoCart.text == constants.addToCard_text
        
      
       
       
    #bütün ürünlerin sepete eklenebilmesinin kontrolü
    def test_add_all_items(self):
        self.test_go_to_page(username="standard_user", password="secret_sauce")
        self.waitForElementVisible((By.CLASS_NAME,constants.itemContainer_Classname))
        Items = self.driver.find_elements(By.CLASS_NAME, constants.ItemsClass_name)
        for item in Items:
            item.click()
            
        self.waitForElementVisible((By.CLASS_NAME,constants.CartContainer_className))
        cart= self.driver.find_element(By.XPATH,constants.cart_Xpath).click()
        self.waitForElementVisible((By.CLASS_NAME,constants.catItems_className))
         
        cartItems= self.driver.find_elements(By.CLASS_NAME,constants.catItems_className)
        self.saveScreenShoot("test_add_all_items")
        assert 6 == len(cartItems)


     # continueShopping button kontrolü

    def test_continueShopping(self):
        self.test_add_all_items()
        self.waitForElementVisible((By.ID,constants.continueShoppingBtnId))
        ContinueShoppingBtn=self.driver.find_element(By.ID,constants.continueShoppingBtnId).click()
        self.saveScreenShoot("test_continueShopping")
        assert self.driver.current_url == constants.product_list_url
        


    # checkout işlemi sırasında firstName alanının boş geçilmesi
    # bunun için ilk etapta bir fonksiyon yazıp checkout işlemlerini kapsamasını sağlamak istiyorum.
    
    def checkout(self, firstname, lastname, postalno):
        self.test_add_all_items()
        self.waitForElementVisible((By.CLASS_NAME, constants.checkoutBtn_ClassName))
        checkoutBtn = self.driver.find_element(By.ID, constants.checkoutId).click()
        self.waitForElementVisible((By.ID, constants.checkoutInfo_ContainerId))
        firstNameInput = self.driver.find_element(By.ID, constants.CheckoutFirstNameId)
        lastNameInput = self.driver.find_element(By.ID, constants.CheckoutLastNameId)
        postalInput = self.driver.find_element(By.ID,constants.CheckoutPostalId)

        firstNameInput.send_keys(firstname)
        lastNameInput.send_keys(lastname)
        postalInput.send_keys(postalno)
        
        
    # sepete ürün eklenditen sonra checkout işleminin kontrolü
    def test_order_checkout(self):
      
        self.checkout(firstname="kader",lastname="Tekin",postalno="123")
        continueBtn = self.driver.find_element(By.ID, constants.continueBtn_Id).click()
        self.waitForElementVisible((By.ID, constants.finishbtn_Id))
        finishBtn = self.driver.find_element(By.ID,constants.finishbtn_Id).click()
        self.waitForElementVisible((By.CLASS_NAME,constants.completeText_ClassName))
        successMessage = self.driver.find_element(By.CLASS_NAME, constants.completeText_ClassName)
        self.saveScreenShoot("test_order_checkout")
        assert successMessage.text == constants.CheckoutSuccessMessage

     
     #backHome buton kotrolü
    def test_backHome(self):
        self.test_order_checkout()
        backHomeBtn=self.driver.find_element(By.ID,constants.BackHomeBtn_Id).click()
        self.saveScreenShoot("test_backHome")
        assert self.driver.current_url== constants.product_list_url
         
     
    
        
             
         
    #ckeckoutinfo kısmında firstname'in boş geçilmesi durumu
    def test_emptyfirstName_inCheckout(self): 
        self.checkout(firstname="", lastname="Tekin", postalno="123")
        continueBtn = self.driver.find_element(By.ID, constants.continueBtn_Id).click()
        errorMessage = self.driver.find_element(By.XPATH, constants.emptyfirstName_inCheckoutMessage_Xpath)
        self.saveScreenShoot("test_emptyfirstName_inCheckout")
        assert errorMessage.text == constants.emptyfirstName_inCheckout_ErrorMessage
      
        
     # ckeckoutinfo kısmında lastname'in boş geçilmesi durumu
    def test_emptylastName_inCheckout(self):
         self.checkout(firstname="kader",lastname="",postalno="1234")
         continueBtn = self.driver.find_element(By.ID, constants.continueBtn_Id).click()
         errorMessage=self.driver.find_element(By.XPATH,constants.emptylastName_inCheckoutMessage_Xpath)
 
         self.saveScreenShoot("test_emptylastName_inCheckout")
         assert errorMessage.text==constants.emptylastName_inCheckout_ErrorMessage
         
         
         
    # ckeckoutinfo kısmında postalcode'in boş geçilmesi durumu
       
    def test_emptypostalCode_inCheckout(self):
        self.checkout(firstname="kader", lastname="Tekin", postalno="")
        continueBtn = self.driver.find_element(By.ID, constants.continueBtn_Id).click()
        errorMessage=self.driver.find_element(By.XPATH,constants.emptyPostalCode_inCheckoutMessage_Xpath)
        self.saveScreenShoot("test_emptypostalCode_inCheckout")
        assert errorMessage.text==constants.emptypostalCode_inCheckout_ErrorMessage
      
     
    #checkout information sırasında cancel butonuyla sepete dönme kontrolü 
    def test_fromCancelBtn_toCart(self):
        self.checkout(firstname="", lastname="", postalno="")
        self.waitForElementVisible((By.ID, constants.cancelBtn_Id))
        cancelBtn = self.driver.find_element(By.ID, constants.cancelBtn_Id).click()
        self.waitForElementVisible((By.CLASS_NAME, constants.cartFooter_ClassName))

        self.saveScreenShoot("test_fromCancelBtn_toCart")
        assert self.driver.current_url == constants.cartURL
        
        
        


     # filtreleme işlemleri
     
    def filter(self):
        self.test_go_to_page(username="standard_user", password="secret_sauce")
        self.waitForElementVisible((By.CLASS_NAME, constants.filterBtn_ClassName))
        filterBtn = self.driver.find_element(By.CLASS_NAME, constants.filterBtn_ClassName).click()
        
     #düşükfiyattanYüksekfiyata  filtreleme
    def test_filter_lowToHigh(self):
       self.filter()
       price_low_to_high=self.driver.find_element(By.XPATH,constants.filterLowToHigh_Xpath).click()
       items=self.driver.find_elements(By.CLASS_NAME,constants.itemPrice_ClassName)
       expected_result=sorted([float(item.text[1:]) for item in items])
       actual_result=[float(item.text[1:]) for item in items]
       self.saveScreenShoot("test_test_filter_lowToHigh")
       assert actual_result == expected_result


       
    #yüksek fiyattan düşük fiyata filtreleme
    
    def test_filter_HighToLow(self):
        self.test_go_to_page(username="standard_user", password="secret_sauce")
        self.waitForElementVisible((By.CLASS_NAME, constants.filterBtn_ClassName))
        filterBtn = self.driver.find_element(By.CLASS_NAME, constants.filterBtn_ClassName)
        select = Select(filterBtn)

        select.select_by_value(constants.filterHighToLow_Value)

        self.waitForElementVisible((By.CLASS_NAME, constants.item_className))
        item_name = self.driver.find_element(By.CLASS_NAME, constants.item_className)
        self.saveScreenShoot("test_filter_HighToLow")
        assert item_name.text == constants.HighItem_Name

    
    #çok içime sığmadı bu çözüm Ya 2.üründen itibaren sıralama yanlışsa :( tekrardan bak bunların çözümüne!!! 
    # Z'den a'ya filtreleme
    def test_filter_z_to_a(self):
        self.test_go_to_page(username="standard_user", password="secret_sauce")
        self.waitForElementVisible((By.CLASS_NAME, constants.filterBtn_ClassName))
        filterBtn = self.driver.find_element(By.CLASS_NAME, constants.filterBtn_ClassName)
        select = Select(filterBtn)
        select.select_by_value(constants.filterZtoA_value)
        self.waitForElementVisible((By.CLASS_NAME, constants.item_className))
        item_name = self.driver.find_element(By.CLASS_NAME, constants.item_className)
        self.saveScreenShoot("test_filter_z_to_a")
        assert item_name.text == constants.ZtoAItem_Name
        
        
    # a'dan z'ye filtreleme
    def test_filter_a_to_z(self):
        self.test_go_to_page(username="standard_user", password="secret_sauce")
        self.waitForElementVisible((By.CLASS_NAME, constants.filterBtn_ClassName))
        filterBtn = self.driver.find_element(By.CLASS_NAME, constants.filterBtn_ClassName)
        select = Select(filterBtn)
        select.select_by_value(constants.filterAtoZ)
        self.waitForElementVisible((By.CLASS_NAME, constants.item_className))
        item_name = self.driver.find_element(By.CLASS_NAME, constants.item_className)
        self.saveScreenShoot("test_filter_a_to_z")
        assert item_name.text == constants.AtoZItem_Name
        
    @pytest.mark.parametrize("sort_by",[("az"),("za")])    
    def test_Refilter(self,sort_by:str):
         self.test_go_to_page(username="standard_user", password="secret_sauce")
         
         match sort_by:
             case "az":
                 Select(self.driver.find_element(By.CLASS_NAME,
                                                 "product_sort_container")).select_by_index(0)
                 
                 items=[item.text for item in self.driver.find_elements(
                     By.CLASS_NAME, "inventory_item_name"
                 )]
                 items_sorted_az=sorted(items)
                 assert items  == items_sorted_az
                 
             case "za":
                Select(self.driver.find_element(By.CLASS_NAME,
                                                 "product_sort_container")).select_by_index(1)
                
                items=[item.text for item in self.driver.find_elements(
                     By.CLASS_NAME, "inventory_item_name"
                 )]
                
                items_sorted_za=sorted(items, reverse=True)
                assert items== items_sorted_za

                
                 
                
        
        
        
        
    # reset App state kontrolü
    def test_resetApp(self):
        self.test_add_all_items()
        self.waitForElementVisible((By.ID, constants.menu_id))
        menu = self.driver.find_element(By.XPATH, constants.menuBtn_Xpath).click()
        resetBtn = self.driver.find_element(By.ID, constants.resetBtnId).click()
        self.waitForElementVisible((By.CLASS_NAME, constants.CartContainer_className))
        cart = self.driver.find_element(By.XPATH, constants.cart_Xpath).click()
        cartItems = self.driver.find_elements(By.CLASS_NAME, constants.catItems_className)
        self.saveScreenShoot("test_resetApp")
        assert 0 == len(cartItems)
        
    
    #menü kısmında about buton kontrolü
    
    def test_about(self):
        self.test_go_to_page(username="standard_user", password="secret_sauce")
        menu = self.driver.find_element(By.XPATH, constants.menuBtn_Xpath).click()
        aboutBtn=self.driver.find_element(By.ID,constants.aboutBtnId).click()
        self.waitForElementVisible((By.CLASS_NAME,"css-jengxu"))
        self.saveScreenShoot("test_about")
        assert self.driver.current_url == constants.aboutURL
        
        
        
    #footer kısmının kontrolü
    
    #twitter icon kontrolü
    
    def test_twitterIcon(self):
        self.test_go_to_page(username="standard_user", password="secret_sauce")
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        self.waitForElementVisible((By.CLASS_NAME, constants.footerClassName))
        twitterIcon=self.driver.find_element(By.XPATH,constants.twitterXpath).click()
        
        # switch_to_window:farklı web sitelerinin bulunduğu yeni bir sekme ve pencere açar.
        self.driver.switch_to.window(self.driver.window_handles[1])
        
        self.saveScreenShoot("test_twitterIcon")
        assert self.driver.current_url == constants.twitterURL
        
        
    #facebook icon kontrolü
    def test_facebookIcon(self):
        self.test_go_to_page(username="standard_user", password="secret_sauce")
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

        self.waitForElementVisible((By.XPATH, constants.facebookXpath))
        facebookIcon = self.driver.find_element(By.XPATH, constants.facebookXpath)
        facebookIcon.click()

        self.driver.switch_to.window(self.driver.window_handles[1])
        self.saveScreenShoot(" test_facebookIcon")

        assert self.driver.current_url == constants.facebookURL
        
    
    #linkedin icon kontrolü

    def test_linkedinIcon(self):
        self.test_go_to_page(username="standard_user", password="secret_sauce")
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

        self.waitForElementVisible((By.XPATH, constants.linkedinXpath))
        linkedinIcon = self.driver.find_element(By.XPATH, constants.linkedinXpath)
        linkedinIcon.click()

        self.driver.switch_to.window(self.driver.window_handles[1])

        self.saveScreenShoot("test_linkedinIcon")
        assert self.driver.current_url == constants.linkedinURL
        
    

  