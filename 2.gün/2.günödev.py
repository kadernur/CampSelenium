# """ 
# AMAÇ:
# Derste işlenen konuların pekiştirilmesi.
# ÖDEV TANIMI:
# Bir öğrenci kayıt sistemi yazdığımızı düşünelim. Sistemimizdeki öğrencileri bir listede sadece ad soyad olacak şekilde tutalım.
# Bu öğrenci kayıt sistemine;
# Aldığı isim soy isim ile listeye öğrenci ekleyen
# Aldığı isim soy isim ile eşleşen değeri listeden kaldıran
# Listeye birden fazla öğrenci eklemeyi mümkün kılan
# Listedeki tüm öğrencileri tek tek ekrana yazdıran
# Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan
# Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)
# fonksiyonları geliştiriniz ve her bir fonksiyonu en az bir kere çağırarak konsolda test ediniz.
# Ödevde kullanacağınız döngülerin bir tanesi for bir tanesi while döngüsü olması istenmektedir.
# """


students=[]

def addStudent(name):
    students.append(name.capitalize())
    print(name.capitalize() + " added to the list. ")

    
addStudent("Nur")    

def removeStudent(name):
    if name in students:
        students.remove(name)
        print(name.capitalize() + " deleted to the list. ")
        
    else:
        print(name.capitalize()+ " the student is not in the list. ")
        
        
def addMultipleStudents():
    while True:
        name= input("Enter the name of the student you want to add (Press x to exit): ")
        if name=="x":
            break
        else:
           students.append(name.capitalize())
           print(name.capitalize() + " added to the list. ")
            
addMultipleStudents()          
            
def removeMultipleStudents():
       while True:
            name= input("Enter the name of the student you want to add (Press x to exit): ")
            if name=="x":
              break
            else:
                removeStudent(name)
            

def info():
    for student in students:
        print(student.capitalize())

info()      
def studentNo(student):
    if student in students:
        no= students.index(student) + 1
        print(student.capitalize() + " student's number: " + str(no))
        
    else:
        print(student.capitalize() + " the student is not in the list. ")

studentNo("Kader")

removeStudent("Sıla")

info()