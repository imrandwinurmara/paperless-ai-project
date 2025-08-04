# Paperless-AI Project (Basic)

Panduan install Paperless-NGX (tested Windows).

---

## 1. Clone repo ini dari CMD (admin mode)

```bash
git clone https://github.com/imrandwinurmara/paperless-ai-project.git
cd paperless-ai-project



2. installl Docker Desktop


3.Buat folder Paperless Ngx
	
 Sebelum menjalankan perintah docker-compose up -d, buat dulu struktur folder yang dibutuhkan supaya data, dokumen, dan database bisa tersimpan dengan benar.

 Buka lokasi project-mu (misal, D:\paperless-ai-project)

 Buat folder baru dengan nama:

	paperless-ai-project/
	├─paperless_ngx
	  ├─ data/
	  ├─ media/
	  ├─ consume/
	  ├─ export/
	├─ docker-compose.yml 
	└─ README.md
 Note: Pastikan nama folder persis sama seperti di file docker-compose.yml


4. Jalankan Docker Compose

 Pastikan Docker Desktop sudah terinstall.

 Buka kembali Command Prompt (admin mode), lalu ketik:

	docker-compose up -d

	

5. Akses Paperless-NGX di Browser 

 Ketik alamat: http://localhost:8000

 Default login:

	Username: admin

	Password: admin

6. Selesai!

 Semua dokumen yang di-upload, database, dan file hasil scan otomatis masuk ke folder paperless_ngx/.
 Kalau ada error atau masalah, cek panduan lengkap/troubleshooting di folder docs/



Tips:
 Kalau mau ganti lokasi penyimpanan data, cukup edit path di docker-compose.yml.
 Untuk kolaborasi, share repo ini ke tim.  
 Selalu pastikan .gitignore sudah mengabaikan folder data.


Selamat mencoba!   
Kalau butuh bantuan, tinggal mention lewat issue di GitHub.


