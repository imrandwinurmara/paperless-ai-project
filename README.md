# Paperless-AI Project (Basic)

Panduan instalasi Paperless-NGX (tested di Windows, Docker Desktop).

---

## Langkah Instalasi

1. **Clone repo ini dari CMD (run as administrator):**
    ```bash
    git clone https://github.com/imrandwinurmara/paperless-ai-project.git
    cd paperless-ai-project
    ```

2. **Install Docker Desktop**  
   Unduh dan install dari: https://www.docker.com/products/docker-desktop/

3. **Buat struktur folder berikut di dalam folder project:**
    ```
    paperless-ai-project/
    ├── paperless_ngx/
    │   ├── data/
    │   ├── media/
    │   ├── consume/
    │   ├── export/
    ├── docker-compose.yml
    └── README.md
    ```
    *Catatan: Pastikan nama folder sama dengan path di docker-compose.yml*

4. **Jalankan Paperless-NGX:**
    ```bash
    docker-compose up -d
    ```

5. **Akses Paperless-NGX di browser:**  
    Buka: http://localhost:8000  
    **Default login:**  
    Username: `admin`  
    Password: `admin`

6. **Selesai!**  
    Semua dokumen yang di-upload, database, dan file hasil scan otomatis masuk ke folder `paperless_ngx/`.  
    Jika ada error, cek panduan troubleshooting di folder `docs/`.

---

**Tips:**
- Untuk ganti lokasi penyimpanan data, edit path di `docker-compose.yml`.
- Untuk kolaborasi, cukup share repo ini ke tim.
- Pastikan `.gitignore` sudah mengabaikan folder data.

---

Selamat mencoba!  
Butuh bantuan? Silakan buat *issue* di repo GitHub ini 🚀
