from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

#ilgili web sitesine yönlendirme
driver.get("https://www.google.com.tr/")
sleep(5)

#istediğim elementi bulup seleniuma tanıttım.
input=driver.find_element(By.NAME, "q")

#ilgili inputa birşeyler yazmak istersem
input.send_keys("kodlama.io")

#google'da ara butonuna basılıp arama işleminin gerçekleştirilmesi

searchButton = driver.find_element(By.NAME,"btnK")
sleep(2)
searchButton.click()
sleep(2)
firstResult = driver.find_element(By.XPATH,"/ html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a")
firstResult.click()
#sleep(10)

#kurs sayısını bulalım.
listOfCourses= driver.find_elements(By.CLASS_NAME,"course-listing")
print(f"Kodlamaio sitesinde şu anda {len(listOfCourses)} adet kurs var. ")
while True:
    continue
 