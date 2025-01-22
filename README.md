

## Job Portal (Django)
Sebuah Aplikasi / Platform digital yang memafasilitasi sebuah perusaahan yang ingin mempunya sebuah portal rekrutmen tenaga kerja sendiri yang di kelola sendiri.

## Installation
Download atau clonning repositori ini.
```bash
git clone https://github.com/SamsuSidqy/JobPortal.git
```

## Buat Enviroment
**Windows**
```bash
python -m pip venv env
```

**Linux**
```bash
python3 -m pip venv env
```

## Aktifkan Virtual Enviroment & Install Enviroment

**Linux**
```bash
source env/bin/activate
```

**Windows**
```bash
env/Scripts/activate
```

## Install Requirements
```bash
pip install -r req.txt
```


## ⚠️ Persyaratan Konfigurasi Aplikasi

- Pertama Apikasi Ini Memerlukan Konfigurasi **SMTP** untuk melakukan Pengiriman Email Kepada Pengguna
  
  **SMTP Gmail**
  - Masuk Ke Akun Google Anda
  - Pilih Menu **Kelola Akun Google Anda**
  - Cari / Search Menu **Sandi Aplikasi**
  - Buat Dan Simpan Password Tersebut Ketampat Yang Aman

- Jika Sudah Melakukan Setup SMTP gmail, selanjutnya melakukan konfigurasi **SMTP** ke App Django Ini
  
  `core/settings.py`
  ```python
  ...
  EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
  EMAIL_HOST = 'smtp.gmail.com'
  EMAIL_USE_TLS = True
  EMAIL_PORT = 587
  EMAIL_HOST_USER = // Email SMTP Gmail Anda Yang Tadi Di Buat
  EMAIL_HOST_PASSWORD = // Password Yang Anda Simpan Tadi
  ...
  ```
## 🥽 Melakukan Migrations
Di documentation ini kita menggunakan database **sqlite**, jika kalian ingin mengganti ke database yang lain bisa cari di google

- Lakukan Makemigrations
```bash
python manage.py makemigrations
```
- Lakukan Migrate
```bash
python manage.py migrate
```

## 🔧 Buat Permissions Untuk Role User
Tujuan nya agar, nanti setiap user memiliki permissioon / authentikasi yang berbeda yaitu **admin** dan **pengguna**

- Lakukan Permission Untuk Admin
```bash
python manage.py create-groups-admin
```
- Lakukan Permission Untuk Pengguna
```bash
python manage.py create-groups-users
```


## 📌 Membuat Account
Untuk Membuat Account **admin** dan **pengguna**, itu berbeda.

- Pembuatan Akun **Admin**
  
  untuk membuat akun admin, anda harus melakukanya melewati terminal / bash. nanti anda akan di minta beberapa inputan seperti `email`,`no-telp`,`password`
```bash
python manage.py createsuperuser
```
- Pembuatan Akun **Pengguna**

  untuk membuat akun pengguna, hanya bisa di lakukan lewat Front-end atau di halaman registrasi yang sudah ada.


## 🧑🏻‍💻 Running App
Setelah semua konfigurasi telah dilakukan jalankan aplikasi.

```bash
python manage.py runserver
```
`http://127.0.0.1:8000`

```bash
python manage.py runserver 0.0.0.0:8000
```
`http://0.0.0.0:8000`

`http://<your-ip-address>:8000`


