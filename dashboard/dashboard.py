import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

# Helper functions
def create_monthly_pm25_df(df):
    df['year_month'] = df['datetime'].dt.to_period('M')
    monthly_pm25 = df.groupby('year_month')['PM2.5'].mean().reset_index()
    monthly_pm25['year_month'] = monthly_pm25['year_month'].astype(str)
    return monthly_pm25

# Load data
@st.cache_data
def load_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'main_data.csv')
    df = pd.read_csv(file_path)
    df['datetime'] = pd.to_datetime(df['datetime'])
    return df

all_df = load_data()

# Sidebar
with st.sidebar:
    st.title('Air Quality Dashboard')
    st.image('https://cdn-icons-png.flaticon.com/512/3208/3208903.png', width=100)
    
    # Pilihan stasiun
    stations = all_df['station'].unique().tolist()
    stations.insert(0, 'Semua Stasiun')
    selected_station = st.selectbox('Pilih Stasiun Pengamatan:', stations)

# Filter data
if selected_station == 'Semua Stasiun':
    main_df = all_df
else:
    main_df = all_df[all_df['station'] == selected_station]

# Dashboard Layout
st.header('Beijing Air Quality Dashboard ☁️')
st.markdown('Dashboard ini menyajikan analisis interaktif untuk kualitas udara (Air Quality) di wilayah Beijing dari tahun 2013 hingga awal 2017.')

# 1. Pertanyaan Bisnis 1: Tren PM2.5
st.subheader('1. Tren Rata-rata Konsentrasi PM2.5 Bulanan')
monthly_pm25_df = create_monthly_pm25_df(main_df)

fig, ax = plt.subplots(figsize=(16, 6))
ax.plot(
    monthly_pm25_df['year_month'],
    monthly_pm25_df['PM2.5'],
    marker='o',
    linewidth=2,
    color='#90CAF9'
)
ax.set_title('Tren Konsentrasi PM2.5', loc="center", fontsize=20)
ax.set_ylabel('Konsentrasi PM2.5 (µg/m³)')
ax.set_xlabel('Bulan')
plt.xticks(rotation=45)
ax.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(fig)

st.caption('Insight: Tingkat polusi cenderung melonjak drastis pada akhir tahun menuju musim dingin.')

# 2. Pertanyaan Bisnis 2: Korelasi TEMP vs O3
st.subheader('2. Korelasi antara Temperatur Udara (TEMP) dan Ozon (O3)')

# Untuk mempercepat rendering scatter plot, ambil sampel
sample_df = main_df.sample(n=min(5000, len(main_df)), random_state=42)

fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.regplot(x='TEMP', y='O3', data=sample_df, scatter_kws={'alpha':0.3, 'color':'teal'}, line_kws={'color':'red'}, ax=ax2)
ax2.set_title('Korelasi Temperatur dan Ozon', fontsize=16)
ax2.set_xlabel('Temperatur (°C)')
ax2.set_ylabel('Konsentrasi Ozon (µg/m³)')
ax2.grid(True, linestyle='--', alpha=0.6)
st.pyplot(fig2)

st.caption('Insight: Terdapat korelasi positif yang cukup kuat, di mana suhu tinggi sejalan dengan peningkatan konsentrasi Ozon.')

# 3. Analisis Lanjutan: Binning
st.subheader('3. Kategori Indeks Kualitas Udara Berdasarkan PM2.5 (Binning)')

category_counts = main_df['PM2.5_Category'].value_counts().reindex(['Good', 'Moderate', 'Unhealthy for Sensitive', 'Unhealthy', 'Very Unhealthy', 'Hazardous'])

fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.barplot(x=category_counts.index, y=category_counts.values, palette='viridis', ax=ax3)
ax3.set_title('Distribusi Kategori Kualitas Udara (PM2.5)', fontsize=16)
ax3.set_xlabel('Kategori')
ax3.set_ylabel('Jumlah Jam')
plt.xticks(rotation=45)
st.pyplot(fig3)

st.caption('Insight: Meskipun sebagian besar waktu udara dalam kondisi Good-Moderate, proporsi waktu dalam status Unhealthy hingga Hazardous tidak dapat diabaikan.')

st.markdown('---')
st.markdown('**Dibuat oleh Adyanto Wahyudhi Nugroho - Dicoding Submission**')
