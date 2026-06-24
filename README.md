# Beijing Air Quality Dashboard ☁️

Ini adalah submission proyek akhir kelas **Belajar Fundamental Analisis Data** di Dicoding. Proyek ini menganalisis kualitas udara di wilayah Beijing menggunakan dataset _PRSA (Multi-site Air-Quality Data)_ dari tahun 2013 hingga 2017, serta menyediakan dashboard interaktif berbasis **Streamlit**.

## 🛠️ Setup Environment

### Menggunakan Anaconda

```bash
conda create --name air-quality-ds python=3.9
conda activate air-quality-ds
pip install -r requirements.txt
```

### Menggunakan Venv (Python Bawaan)

```bash
python -m venv venv
venv\Scripts\activate      # Untuk pengguna Windows
# source venv/bin/activate # Untuk pengguna Linux/Mac

pip install -r requirements.txt
```

## 🚀 Cara Menjalankan Dashboard

1. Pastikan semua _library_ (seperti `pandas`, `matplotlib`, `seaborn`, dan `streamlit`) sudah terinstal melalui `requirements.txt`.
2. Masuk ke dalam direktori `dashboard` tempat skrip aplikasi berada.
3. Jalankan perintah `streamlit run`.

```bash
cd dashboard
streamlit run dashboard.py
```

Setelah perintah berhasil dijalankan, Streamlit akan secara otomatis membuka jendela browser baru (umumnya di alamat `http://localhost:8501`) yang menampilkan dashboard secara langsung.
