
# PYTEST DECORATOR
<p>PyTest, genellikle çok amaçlı, ancak özellikle aşağıdakiler için açık kaynaklı Python tabanlı bir test çerçevesidir. İşlevsel ve API testi.
Pip (Python için Paket Yükleyici) PyTest kurulumu için gereklidir.
API, veritabanları ve kullanıcı arayüzlerini test etmek için basit veya karmaşık metin kodunu destekler.
Basit sözdizimi, kolay test yürütme için faydalıdır.
Zengin eklentiler ve testleri paralel olarak çalıştırabilir.
Testlerin herhangi bir alt kümesini çalıştırabilir.</p>

![image](https://user-images.githubusercontent.com/63293055/227895710-a2ee4083-178d-4f11-a763-101080eaaf03.png)

Kullanılan bazı decoratorler şunlardır;

# @pytest.mark.parametrize

Bir testin işlevinin farklı parametrelerle çalıştırılmasını sağlar. 
Aşağıdaki kod örneğinde username ve password değişkenlerine (1,1) değerleri ve (kullaniciadim,sifrem) değerleri olmak üzere testin 2 farklı parametre ile çalıştırılmasını temsil eder.

`@pytest.mark.parametrize("username,password",[("1","1"),("kullaniciadim","sifrem")])`

# @pytest.mark.skip

Test işlemi sırasında belirtilen fonksiyonun, çalıştırılmadan es geçilmesini sağlar.

`@pytest.mark.skip(reason="pass")`

# @pytest.mark.timeout

Testin belirli bir sürede tamamlanması gerektiğini ifade eder ve testin sonsuza kadar çalışmasını önler.

`@pytest.mark.timeout(300)`

# @pytest.fixture

Test işlemlerinden önce gerekli olan verileri sağlayacak kodun çalışmasını sağlayan yapıdır.

`import pytest`

`@pytest.fixture`

`def input_value():`

   `input = 39`
   
   `return input`
   

`def test_divisible_by_3(input_value):`

  ` assert input_value % 3 == 0`

`def test_divisible_by_6(input_value):`


# @pytest.mark.order
Test işlemleri sırasında belirlemiş olduğumuz sıralamaya göre fonksiyonların çalışmasını sağlayan yapıdır

# @pytest.mark.xfail
Bir testin herhangi bir nedenle başarısız olmasını beklediğiniz anlamına gelir. 
Yaygın bir örnek, henüz uygulanmayan bir özellik veya henüz düzeltilmemiş bir hata için yapılan testtir.
Başka bir deyişle ;Test işlemleri sırasında belirtilen fonksiyonun, hata vermesinin mümkün olduğunu belirtir. Yani fonksiyon hata verdiğinde bize bildirilmeden es geçilmesini sağlayan yapıdır.

Reason: Hatanın sebebini açıklar.

`@pytest.xfail(reason="bug")`

Strict: Parametre testlerinin daha sıkı kontrol edilmesini sağlar. Yani test edilmek istenen 
davranışın gerçekten test edildiğinden emin olunması gereken durumlarda kullanılır.

`@pytest.xfail(strict=True)`


Run: çalıştırılmasını engeller.
`@pytest.xfail(run=False)`
