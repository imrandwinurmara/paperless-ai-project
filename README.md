Paperless-AI Project (Basic)

Cara Install Paperless-NGX

1.Clone repo ini dari cmd

	git clone https://github.com/imrandwinurmara/paperless-ai-project.git

	cd paperless-ai-project

2.Buat folder Paperless Ngx
	
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

3. Jalankan Docker Compose

	A. Pastikan kamu sudah install Docker Desktop

	Docker adalah aplikasi wajib yang harus terpasang di komputer untuk menjalankan project ini.


	B. Buka kembali Command Prompt (atau tetap di jendela tadi), lalu ketik:

	docker-compose up -d

4. Akses Paperless-NGX di Browser 

	Ketik alamat: http://localhost:8000

	(jika membutuhkan)

	Default login:

		Username: admin

		Password: admin



