class Human:
   
    
    #♦built-in yani constructor diyebiliriz.
    def __init__(self, name):
        self.name=name
        print("Bir human instance çalıştı")
        
    def talk(self , sentence):
        name="Nur"
        print(f"{self.name} is talking in {sentence}")
        
    def walk(self):
        print("human is walking...")
        
        
#  instance yani newlemek       
human1=Human("Miraç")
human1.talk("the garden")
human1.walk()

#paket importu
from selenium import webdriver

