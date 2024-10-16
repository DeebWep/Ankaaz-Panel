#Ankaaz-Panel
##Ankaaz-Panel, pentester ve güvenlik araştırmacıları için geliştirilen bir araç setidir. Bu araç, admin panel bulma, directory brute force ve PHP reverse shell oluşturma gibi temel web güvenlik testlerini otomatikleştirmek için kullanılır.

Özellikler:
Admin Panel Finder: Web sitelerinde admin panellerini bulmanızı sağlar.
Directory Bruteforce: Farklı dizinleri brute force ile tarayarak potansiyel hassas dosya ve dizinleri bulur.
Reverse PHP Shell Generator: Hedef sistemlere uzaktan erişim sağlayacak bir PHP reverse shell dosyası oluşturur.
Kurulum
Repositori'yi klonlayın:

bash
Copy code
git clone https://github.com/DeebWep/Ankaaz-Panel.git
cd Ankaaz-Panel
Gerekli bağımlılıkları yükleyin:

bash
Copy code
pip install -r requirements.txt
Virtual Environment kullanarak izole bir ortamda çalışabilirsiniz:

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # Linux/MacOS
.\venv\Scripts\activate    # Windows
Kullanım
Ana Menü
Araç başlatıldığında ana menü karşınıza çıkacaktır:

bash
Copy code
[1]  Admin Panel Finder
[2]  Directory Bruteforce
[3]  Reverse PHP Shell Generator
[4]  Çıkış
Admin Panel Finder
Bu özellik, hedef sitelerde admin panellerini aramanızı sağlar.

Menüde 1 seçeneğini seçin.
Hedef URL'yi girin (örn: http://example.com).
Admin panel araması başlayacaktır.
Directory Bruteforce
Bu özellik, dizin brute force işlemi yaparak hedef sitelerde var olabilecek dizinleri bulur.

Menüde 2 seçeneğini seçin.
Hedef URL'yi girin (örn: http://example.com).
Araç, wordlists/directory-list-2.3-medium.txt listesindeki dizinlere karşı tarama yapacaktır.
Reverse PHP Shell Generator
Bu özellik, hedef sistemlere sızmak için bir PHP reverse shell dosyası oluşturur.

Menüde 3 seçeneğini seçin.
İstenilen IP adresi ve port numarasını girin.
Araç, girilen bilgileri kullanarak bir PHP shell dosyası oluşturacaktır.
Gereksinimler
Python 3.x
requests, colorama, colored, pyuseragents gibi Python kütüphaneleri (Otomatik olarak yüklenir.)
Dosya Yapısı
ankaaz-panel.py: Ana Python betiği.
wordlists: Araç tarafından kullanılan wordlist dosyaları.
admin-panel-directorylist.txt: Admin panel bulma aracı için kullanılan yol listesi.
directory-list-2.3-medium.txt: Directory brute force işlemi için kullanılan liste.
reverse_shell_template.txt: PHP reverse shell şablonunu içerir.
