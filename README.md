# CampSelenium
<img src="https://user-images.githubusercontent.com/63293055/229248678-c2164230-bd75-486c-b7e6-d80f0e953600.png" width="auto">
<p> Bu repom'da Pyhon ile selenium kampından öğrendiklerim ile  https://www.saucedemo.com/  sitesi üzerinden kendi belirlemiş olduğum aksiyonların test kodları yer almaktadır. Code refactoring ile ilerleme kat ettim. Repom'da projemin ilk hali ile son halini ayrı ayrı dosyalarda yer almaktadır.</p>
Bu dosyamda projemin ilk hali yer almaktadır. 

  + [Saucewithselenium:open_file_folder:  :(ilgili kodlar pytest kullanılmadan selenium ile yazılmıştır.)](https://github.com/kadernur/CampSelenium/blob/main/Selenium/sauceHomework.py)
  + [SaucewithseleniumandPYTEST:open_file_folder:  :(ilgili kodlar pytest ve selenium ile yazılmıştır. Ve bazı aksiyonlar eklenerek selenium ide ile de test edilmiştir.)](https://github.com/kadernur/CampSelenium/blob/main/Selenium/test_sauceHomework.py) 
+ [SaucewithseleniumandPYTEST:open_file_folder:  :(Projenin son halini içermektedir. İlgili site üzerinden gerekli aksiyonların eklenmesi ve clean code mantığıyla kodlarda iyileştirilmeler yapılmıştır.)](https://github.com/kadernur/CampSelenium/tree/main/SauceDemoSitesi) 


![image](https://user-images.githubusercontent.com/63293055/228060406-ddbc340d-3401-446d-8656-3e2d5fb6c92a.png)
![image](https://user-images.githubusercontent.com/63293055/229251883-2bf2d487-188b-4d9c-8f3c-3b531b6d292c.png)

# PROJE İÇERİĞİ

+ [SaucewithseleniumandPYTEST:open_file_folder:](https://github.com/kadernur/CampSelenium/tree/main/SauceDemoSitesi) 
### TEST FONKSİYONLARI
:heavy_check_mark: **test_empty_username_password**

Giriş sayfasında kullanıcı adı ve şifre alanının boş girilmesi

:heavy_check_mark: **test_emty_password**

 Giriş sayfasında  şifre alanının boş geçilmesi durumunu kontrol eder.
 
 :heavy_check_mark: **test_locked_out_user**
 
 Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajının kontrolünü sağlar.
 
 :heavy_check_mark: **test_remove_error_icon**
 
 Kullanıcı adı ve şifre alanları boş geçildiğinde bu iki inputun yanında da kırmızı "X" ikonu çıkmalıdır. Daha sonra aşağıda çıkan uyarı mesajının kapatma butonuna tıklandığında bu "X" ikonları kaybolmalıdır. (Tek test case)

 :heavy_check_mark: **test_go_to_page**
 
 Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir.
 
  :heavy_check_mark: **test_len_of_the_item**
  Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.
  
  :heavy_check_mark: **test_logout**
  
  giriş yapıldıktan sonra logout butonu ile çıkış işleminin başarılı gerçekleştirilmesi.
  
  :heavy_check_mark: **test_addToCart_removeToCart**
  
  Ürün container'ında yer alan addtocart butonu ile removetocart butonunun kontrolünü gerçekleştirir.
  
  :heavy_check_mark:**test_add_all_items**
  
  Bütün ürünlerin sepete eklenebilmesinin kontrolünü sağlar.
  
   :heavy_check_mark:**test_continueShopping**
   
   Sepet bölümünde yer alan continues Shopping butonu ile ürünlerin olduğu sayfaya başarılı yönlendirilmesinin kontrolünü sağlar.
   
   :heavy_check_mark: **test_order_checkout**
   
   Sepete ürün eklendikten sonra checkout işleminin kontrolünü sağlar.
   
   ![image](https://user-images.githubusercontent.com/63293055/229258099-bfcbe025-e2e5-44e8-9365-2324d85c27db.png)
   
   :heavy_check_mark: **test_emptyfirstName_inCheckout**
   
   Yukarıdaki görselde yer alan checkout işlemi sırasında doldulacak form üzerinden firstname alanının boş bırakılması sonucundaki hata mesajının kontrolünü sağlar.
   
   :heavy_check_mark:**test_emptylastName_inCheckout**
   
   Yukarıdaki görselde yer alan checkout işlemi sırasında doldulacak form üzerinden lastname alanının boş bırakılması sonucundaki hata mesajının kontrolünü sağlar.
   
   :heavy_check_mark:**test_emptypostalCode_inCheckout**
   
   Yukarıdaki görselde yer alan checkout işlemi sırasında doldulacak form üzerinden postalcode alanının boş bırakılması sonucundaki hata mesajının kontrolünü sağlar.
   
   :heavy_check_mark:**test_backHome**
   
   ![image](https://user-images.githubusercontent.com/63293055/229258284-99a9bc36-e73a-4a0b-8c02-9a526b006b80.png)
   
   Başarılı checkout işleminden sonra backHome butonu ile anasayfaya yönlendirme kontrolünü sağlar.
   
   :heavy_check_mark: **test_fromCancelBtn_toCart**
   
   Checkout  işleminden vazgeçip  cancel butonuyla sepete dönüş kontrolünü sağlar.
   
   :heavy_check_mark:**test_filter_lowToHigh**
   
   Düşük fiyattan yüksek fiyata göre   filtreleme işleminin kontrolünü sağlar.
   
   :heavy_check_mark:**test_filter_HighToLow**
   
   Yüksek fiyattan düşük fiyata filtreleme işleminin kontrolünü sağlar.
   
   :heavy_check_mark:**test_filter_z_to_a**
   
   Z'den A'ya filtreleme işleminin kontrolünü sağlar.
   
   :heavy_check_mark:**test_filter_a_to_z**
   
   A'dan Z'ye filtreleme işleminin kontrolünü sağlar.
   
   :heavy_check_mark:**test_resetApp**
   Menülerde yer alan Reset App butonu ile işlemlerin resetlenmesinin kontrolünü sağlar.
   
   :heavy_check_mark: **test_about**
   
   Menülerde yer alan About butonu il ilgili sayfaya yönlendirilmesinin  kontrolünü sağlar.
   
   :heavy_check_mark:**test_twitterIcon**
   
   İlgili sitenin tweeter adresine başarılı bir şekilde  yönlendirilmesinin kontrolünü gerçekleştirir.
   
  
  :heavy_check_mark:**test_facebookIcon**
  
   İlgili sitenin facebook adresine başarılı bir şekilde  yönlendirilmesinin kontrolünü gerçekleştirir.
   
   :heavy_check_mark:**test_linkedinIcon**
   
   İlgili sitenin linkedin adresine başarılı bir şekilde  yönlendirilmesinin kontrolünü gerçekleştirir.
   
  
 Yukarıda yer alan tüm test işlemlerini gerçekleştiren fonksiyonların her birini yardımcı fonksiyonlar ile clean code yazarak gerçekleştirdim. **Bunlar;**
 
 :wavy_dash: Sitede herhangi bir durumdan dolayı zaman gecikmeleri veya belirli şartların gerçekleşmesine kadar  bekleme süresi belirleyen **waitForElementVisible** fonsiyonu.
 
 :wavy_dash: **@pytest.mark.parametrize("username,password",getData1())** decorator'ünde kullanacağımız 3 farklı girdi için test işlemlerini gerçekleştirecek  gerekli değikenleri tutan ***getData1()** fonksiyonu
 
 :wavy_dash: farklı bir fonksiyon için decorator'ün kullanacağı itemlerı tutan **getItem** fonksiyonu.
  
 :wavy_dash:  test işlemleri sırasında alınacak scrreen shoot'lar için oluşturulan **saveScreenShoot(self, nameScreenShot)** fonksiyonu her testin kendi ismi ile bir screen shot işleminin gerçekleştirilmesini sağlar. Projenin ekran görünlerine buradan oluaşabilirsiniz.(https://github.com/kadernur/CampSelenium/tree/main/2023-03-31)
 
 (https://github.com/kadernur/CampSelenium/tree/main/2023-04-01) 
 
 :wavy_dash: **loginInform** fonksiyonu ile her test durumu için tekrar tekrar giriş işlemi yapamamak adına tek bir fonksiyondan bu işlem gerçekleştirildi.
 
 :wavy_dash:**checkout** fonksiyonu ile checkout işlemi için gerekli form elemanları üzerinden yapılan testler için  kod tekrarını önlemek amacıyla oluşturuldu.
  
  :wavy_dash:**filter** fonksiyonu ise filtreleme işlemleri üzerinden gerçekleştirilecek testler için filtreleme alanına kod tekrarları ile erişmeyi önlemek amacıyla yazılmış yardımcı fonksiyondur.
  
  + [PytestDecorator:open_file_folder:(Projede bazı yerlerde kullanmış olduğum decoratorler ile ilgili  bilgilere buradan erişebilirsiniz.)](https://github.com/kadernur/CampSelenium/blob/main/Selenium/PYTESTDECORATOR.MD)

 + [Constant:open_file_folder:](https://github.com/kadernur/CampSelenium/blob/main/SauceDemoSitesi/GlobalConstants/constants.py)

Kod kalitesini arttırmak için kullanmış olduğum locatorler ve gerekli bilileri constant klasörü altında tanımlayıp projemde kullandım. Bu yapı herhangi bir değişim söz konusu olduğu zaman her fonksiyona gidip değişim yerine tek bir yerden değişime olanak sağlar.Ve magic string kullanımının önüne geçmiş olur.
  
 
 
 
 
