# Ankaaz-Panel

**Ankaaz-Panel pentesterlər və təhlükəsizlik tədqiqatçıları üçün hazırlanmış alətdir. Bu alət admin panel kəşf, directory brute force, və PHP reverse shell yaradılması kimi əsas web təhlükəsizlik testlərini avtomatlaşdırılması üçün istifadə olunur. Gələcəkdə daha da inkişaf etdiriləcək.**

![image](https://github.com/user-attachments/assets/13839422-cbef-4a02-9350-b3f4ba4baf56)

## Xüsusiyyətlər: ##

**Admin Panel Finder: Veb saytlarda admin panellərini tapmağa imkan verir.
Directory Bruteforce: Müxtəlif qovluqları kobud güclə skan edərək potensial həssas faylları və qovluqları tapır.
Reverse PHP Shell Generator: Hədəf sistemlərə uzaqdan girişi təmin edəcək PHP tərs qabıq faylı yaradır.**

## Quraşdırılma: ##

**Repositori'yi klonlayın:**
_git clone https://github.com/DeebWep/Ankaaz-Panel.git_
_cd Ankaaz-Panel_

**Başladın:**
_python3 ankaaz-panel.py_

## İstifadəsi ##

### Ana Menu ###
**Alət işə salındıqda əsas menyu görünəcək:**
[1]  Admin Panel Finder
[2]  Directory Bruteforce
[3]  Reverse PHP Shell Generator
[4]  Çıxış

### Admin Panel Finder ###
**Bu funksiya hədəf saytlarda admin panelləri axtarmağa imkan verir.**

**1.Menyuda 1-ci variantı seçin.
2.Hədəf URL-ni daxil edin (məsələn: http://example.com).
3.İdarəetmə paneli axtarışı başlayacaq.**

### Directory Bruteforce ###
**Bu funksiya kataloq kobud güc tətbiq etməklə hədəf saytlarda mövcud ola biləcək kataloqları tapır.**

**1.Menyuda 2-ci variantı seçin.
2.Hədəf URL-ni daxil edin (məsələn: http://example.com).
3.Alət wordlists/directory-list-2.3-medium.txt siyahısındakı qovluqlara qarşı skan edəcək.**

### Reverse PHP Shell Generator ###
**Bu xüsusiyyət hədəf sistemlərə sızmaq üçün PHP tərs qabıq faylı yaradır.**

**1.Menyuda 3-cü variantı seçin.
2.İstədiyiniz IP ünvanını və port nömrəsini daxil edin.
3.Alət daxil edilmiş məlumatlardan istifadə edərək PHP qabıq faylı yaradacaq.**

## Dosya Yapısı ##
**ankaaz-panel.py: Əsas Python skripti.
söz siyahıları: alət tərəfindən istifadə edilən Wordlist faylları.
_admin-panel-directorylist.txt_: İdarəetmə panelinin kəşf aləti üçün istifadə olunan kataloq siyahısı.
_directory-list-2.3-medium.txt_: Kataloqun kobud güc əməliyyatı üçün istifadə edilən siyahı.
_reverse_shell_template.txt_: PHP tərs qabıq şablonunu ehtiva edir.**
