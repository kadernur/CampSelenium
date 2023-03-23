faiz = 1.59
vade = "36"
krediAdi = "İhtiyaç Kredisi"

print(type(faiz)) # type => veri tipini öğrenmek için kullanılır.

print(type(vade))
print(type(krediAdi))

print(int(vade) + 12) # int => string veri tipini integer veri tipine çevirir.
#print(int(krediAdi) # Hata verir. Çünkü krediAdi bir string veri tipidir.)

faiz = str(faiz) # str() => integer veri tipini string veri tipine çevirir.
print(type(faiz))

vade = int(input("Lütfen istediğiniz vade sayısını giriniz: "))
print(type(vade))

vade = vade +12 

# String Interpolation => String ifadeleri birleştirmek için kullanılır.
print("Seçtiğimiz vade sonucu ortaya çıkan vade oranı: " , vade)
print("Seçtiğimiz vade sonucu ortaya çıkan vade oranı:{vade}".format(vade=vade)) # format() => string ifadeleri birleştirmek için kullanılır.

isim = "Kader"
metin = "Merhaba, benim adım {isim}".format(isim=123)
print(metin)


#f-string => String ifadeleri birleştirmek için kullanılır.

metin = f"Merhaba,  {isim}"
print(metin)

# Listeler
krediler = ["İhtiyaç Kredisi", "Konut Kredisi", "Taşıt Kredisi"]
print(krediler)
print(type(krediler))

print(krediler[0]) # [] => listelerdeki elemanlara ulaşmak için kullanılır.

print(len(krediler)) # len() => listelerdeki eleman sayısını öğrenmek için kullanılır.

# print(krediler[3]) # Hata verir. Çünkü listelerde 3. eleman yoktur.

krediler.append("Özel Kredi") # append() => listeye eleman eklemek için kullanılır.

krediler.append("X kredisi")
print(krediler)

krediler.pop(0) # pop() => listelerden eleman silmek için kullanılır. İndeks numarası verilmezse son eleman silinir.
print(krediler)

krediler.remove("Taşıt Kredisi") # remove() => listelerden istenilen elemanı silmek için kullanılır.
print(krediler)

krediler.extend(["Y Kredisi","Z kredisi"]) # extend() => listeye birden fazla eleman eklemek için kullanılır.
print(krediler)


# for döngüsü
""" 
for döngüsü => listelerdeki elemanları tek tek dolaşmak için kullanılır.
for değişken in liste:
    yapılacak işlemler
    
range() => belirtilen sayıya kadar olan sayıları tek tek dolaşmak için kullanılır.
range(start,stop,step) => start => başlangıç değeri, stop => bitiş değeri, step => artış miktarı
"""

for i in range(10):
    print(i)
print("**************")

for i in range(5,10):
    print(i)
    
print("**************")

#range fonksiyonu ile float veri tipi kullanılamaz

krediler = ["İhtiyaç Kredisi", "Konut Kredisi", "Taşıt Kredisi"]
for kredi in krediler:
    print(kredi)
print("**************")
for i in range(len(krediler)):
    print(krediler[i])
    
# while döngüsü
""" 
while döngüsü => belirtilen şarta göre döngüyü çalıştırmak için kullanılır.
"""

i = 0
while i < 10:
    print("x")
    i += 1
print("**************")

while True:
    print("x")
    break # break => döngüyü sonlandırmak için kullanılır.

print("--------------------")

i = 0
while i < len(krediler):
    print(krediler[i])
    i += 1
    if krediler[i] == "Konut Kredisi":
        break
    


# Fonksiyonlar
"""  
Fonksiyonlar => bir işi birden fazla yerde kullanmak için kullanılır.
"""

fiyat = 100
indirim = 20
yeniFiyat = fiyat - indirim

def calculate():
    print(100 - 20)

calculate()

def calculateDiscountPrice(price,discount):
    print(price - discount)

calculateDiscountPrice(100,20)

def sayHello(name):
    print("Merhaba " + name)
    
sayHello("Kader")
sayHello("Nur")


def calculateDiscountPrice(price,discount):
    return price - discount

yeniFiyat = calculateDiscountPrice(100,20)
print(yeniFiyat)