## unpam-elearning-absen-scraper

`unpam-elearning-absen-scraper` merupakan aplikasi scraper berbasis console untuk mendapatkan nama-nama mahasiswa yang aktif dalam suatu topik forum diskusi,, yang mudah-mudahan dapat membantu orang seperti author

## Dependensi
- Python 3
- ChromeDriver

## Penggunaan
1. Download ChromeDriver di `https://chromedriver.chromium.org/downloads`
2. Letakan `chromedriver.exe` di dalam direktori yang sama dengan file `login.py`
3. Buka terminal di dalam direktori yang terdapat file `requirements.txt` dan jalankan perintah `pip install -r requirements.txt`
4. Kemudian jalankan perintah `py main.py`

## Opsional
Jika anda tidak ingin selalu memasukan username dan password terus menerus, maka anda dapat membuat username dan password default dengan cara berikut:
1. Buat file dengan nama `.env` di dalam root direktori
2. Kemudian tuliskan teks berikut pada file `.env`
```
USER_NAME=xxxxxxx
PASSWORD=yyyyyyy
```
3. Ganti `xxxxxxx` dengan username dan `yyyyyyy` dengan password
