📊 Sales Dashboard (Streamlit)

Dashboard interaktif untuk menganalisis data penjualan menggunakan Python, Streamlit, Pandas, dan Plotly.
Project ini menampilkan tren penjualan, performa berdasarkan region, dan visualisasi lainnya secara real-time.


🚀 Fitur

Filter data berdasarkan Region dan Tanggal

Grafik penjualan harian (line chart)

Perbandingan penjualan antar region (bar chart)

Ringkasan statistik total penjualan


Struktur Project

├── app.py              # Main dashboard Streamlit
├── sales_data.csv      # Contoh dataset penjualan
├── requirements.txt    # Dependency project
└── README.md           # Dokumentasi project


Buat virtual environment (opsional tapi disarankan):

python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Mac/Linux


Install dependencies:

pip install -r requirements.txt


Jalankan aplikasi Streamlit:

streamlit run app.py atau python -m streamlit run app.py


📊 Contoh Dataset (sales_data.csv)

Date,Region,Sales
2024-01-01,North,1200
2024-01-02,South,800
2024-01-03,East,950
2024-01-04,West,1100
2024-01-05,North,1400


🔮 Pengembangan Lanjutan

Menambahkan prediksi penjualan dengan Machine Learning
Integrasi database (MySQL/PostgreSQL)
Deploy ke Streamlit Cloud / Heroku