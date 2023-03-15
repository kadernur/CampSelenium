# Bugünkü ödevin amacı değiken ve şart blokları konusunun pekiştirilmesi.

# burada kodlama.io sitesiindeki şart bloklarının kullanıldığı kısımların kodlarını yazıyor olacağım.



user_email="kadernur"
user_password="123456"

email=input("Email: ")
password=input("Password: ")

if user_email==email and user_password==password:
    print("Login successful")
    
elif user_email != email and user_password==password:
    print("username is wrong")
elif user_email==email and user_password != password:
    print("Password is incorrect")
    
else:
    print("User name and your password is incorrect")
    
    
course=True

if course:
    print("You have registered for the course. You can access the course content.")
else:
    print("You have not registered for the course. You can't access the course content.")
    
courses = ["Yazılım Geliştirici Yetiştirme Kampı (JAVA + REACT)","(2022) Yazılım Geliştirici Yetiştirme Kampı - JAVA", "Yazılım Geliştirici Yetiştirme Kampı (JavaScript)", "Yazılım Geliştirici Yetiştirme Kampı (C# + ANGULAR)", "(2023) Yazılım Geliştirici Yetiştirme Kampı - Python & Selenium"]

trainers=["Engin demiroğ","Halit kalaycı"]


for kurs in courses:
    print(kurs)


for trainer in trainers:
    print(trainer)
    
