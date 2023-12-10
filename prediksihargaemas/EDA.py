import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

st.title ('Prediksi Harga Emas')
'---'
'### Dataset Harga Emas'
st.divider()
df=pd.read_csv('./dataset/clean_data1.csv')
df
df1=pd.read_csv('./dataset/clean_data.csv')
st.divider()

# Menginisialisasi plot
#fig, ax = plt.subplots(figsize=(12, 6))


# Inisialisasi variabel
#progress_bar = st.sidebar.progress(0)
#status_text = st.sidebar.empty()
#fig, ax = plt.subplots(figsize=(12, 6))
#chart = st.pyplot(fig)
#button = st.button("Re-run")

# Fungsi untuk mengupdate plot pada setiap iterasi
#def update(frame):
 #   ax.clear()
#    ax.plot(df1['Tanggal'][:frame], df1['Terakhir'][:frame])
#    ax.set_xlabel('Date')
#    ax.set_ylabel('Terakhir')
#    ax.set_title('Penutupan Harga Emas Dari Waktu ke Waktu')
#    chart.pyplot(fig)

# Animasi dengan FuncAnimation
#animation = FuncAnimation(fig, update, frames=len(df1['Tanggal']), repeat=False)

# Logika untuk button Re-run
#if button:
#    for i in range(1, 101):
#        update(int(i / 100 * len(df1['Tanggal'])))
#        progress_bar.progress(i)
#        status_text.text("%i%% Complete" % i)
#        time.sleep(0.0002)
#
#    progress_bar.empty()
#    status_text.empty()
#    st.button("Re-run")

# --- Menampilkan Grafik Harga Terakhir ---
st.header('Grafik Harga Terakhir')
progress_bar = st.progress(0)
status_text = st.empty()
dates = pd.to_datetime(df1['Tanggal'])  # Ubah kolom Tanggal ke format datetime
prices = df1['Terakhir'].values
chart = st.line_chart(prices)

for i in range(1, 101):
    new_prices = prices[-1] + np.random.randn(100)
    status_text.text("%i%% Complete" % i)
    chart.line_chart(new_prices[-50:])
    progress_bar.progress(i)
    prices = new_prices
    time.sleep(0.05)
progress_bar.empty()

st.button("Re-run")
st.divider()

df1.groupby('year')['Terakhir'].agg([len,min,max])
#visualisasi data harga saham 
plt.figure(figsize=(16,6))
Harga_Penutupan = pd.pivot_table(df1, values = "Terakhir", columns = "year", index = "month")
plt.savefig('./grafik/hargaemas.png')
Harga_Penutupan.plot()
plt.title('Harga Emas Pertahun')
plt.grid()
st.pyplot(plt)
('***')
# Plot regresi polinomial
fig2, ax2 = plt.subplots(figsize=(12, 6))
chart2 = st.pyplot(fig2)

# Data harga Emas
df1['Tanggal'] = pd.to_datetime(df1['Tanggal'])  # Mengonversi kolom 'Tanggal' ke tipe datetime

X = df1['Tanggal'].astype(np.int64) // 10**9  # Mengonversi tanggal ke unix timestamp (numerik)
y = df1['Terakhir'].values  # Harga Emas


# Menggunakan regresi polinomial dengan derajat 2
coefficients = np.polyfit(X, y, 2)
polynomial = np.poly1d(coefficients)
y_pred = polynomial(X)

# Plot data asli dan kurva regresi polinomial
ax2.scatter(df1['Tanggal'], y, label='Data Harga Emas')
ax2.plot(df1['Tanggal'], y_pred, color='red', label='Regresi Polinomial')
ax2.set_xlabel('Waktu')
ax2.set_ylabel('Harga Emas')
ax2.legend()

# Menampilkan grafik harga Emas dan regresi polinomial
chart2.pyplot(fig2)
('***')
'### Korelasi antara variabel VS Harga Penutupan'
correlation = df.corr()['Terakhir']
print(correlation)
# Plot korelasi
plt.figure(figsize=(10, 6))
correlation.drop('Terakhir').plot(kind='bar')
plt.xlabel('Variabel')
plt.ylabel('korelasi')
plt.title('korelasi dengan Harga Penutupan')
plt.savefig('./grafik/korelasi.png')
plt.grid()
plt.show()
st.pyplot(plt)
st.divider()
'## Distribusi Data'
options1 = ['Harga Pembukaan', 'Harga Tertinggi', 'Harga Terendah', 'Volume', 'Perubahan']

# Dropdown untuk pemilihan grafik
selected_option1 = st.selectbox('Pilih Jenis Grafik', options1)

# Plot grafik berdasarkan pilihan pengguna
plt.figure(figsize=(12, 6))

if selected_option1 == 'Harga Pembukaan':
    plt.hist(df1['Pembukaan'], bins=20, edgecolor='k')
    plt.title('Distribusi Harga Pembukaan Emas')
    plt.xlabel('Harga Pembukaan')
    plt.ylabel('Frekuensi')

elif selected_option1 == 'Harga Tertinggi':
    plt.hist(df1['Tertinggi'], bins=20, edgecolor='k')
    plt.title('Distribusi Harga Tertinggi Emas')
    plt.xlabel('Harga Tertinggi')
    plt.ylabel('Frekuensi')

elif selected_option1 == 'Harga Terendah':
    plt.hist(df1['Terendah'], bins=20, edgecolor='k')
    plt.title('Distribusi Harga Terendah Emas')
    plt.xlabel('Harga Terendah')
    plt.ylabel('Frekuensi')

elif selected_option1 == 'Volume':
    #visualisasi data harga emas
    plt.figure(figsize=(16,6))
    harga = pd.pivot_table(df1, values = "Vol.", columns = "year", index = "month")
    harga.plot()
    plt.title('Vol. Penjualan Emas Pertahun')
    plt.grid()

elif selected_option1 == 'Perubahan':
        #visualisasi data harga emas
    plt.figure(figsize=(16,6))
    harga = pd.pivot_table(df1, values = "Perubahan%", columns = "year", index = "month")
    harga.plot()
    plt.title('Perubahan Harga Emas Pertahun')
    plt.grid()

# Menampilkan grafik
st.pyplot(plt)
('###')
st.divider()
'## Distribusi Data'
options = ['Harga Pembukaan', 'Harga Tertinggi', 'Harga Terendah', 'Volume', 'Perubahan']

# Dropdown untuk pemilihan grafik
selected_option = st.selectbox('Pilih Jenis Grafik', options, key='selectbox_option')

# Plot grafik berdasarkan pilihan pengguna
plt.figure(figsize=(12, 6))

if selected_option == 'Harga Pembukaan':
    plt.scatter(df1['Pembukaan'], df1['Terakhir'])
    plt.xlabel('Harga Pembukaan')
    plt.ylabel('Harga Terakhir')
    plt.title('Distribusi Harga Pembukaan terhadap Harga Terakhir')

elif selected_option == 'Harga Tertinggi':
    plt.scatter(df1['Tertinggi'], df1['Terakhir'])
    plt.xlabel('Harga Tertinggi')
    plt.ylabel('Harga Terakhir')
    plt.title('Distribusi Harga Tertinggi terhadap Harga Terakhir')

elif selected_option == 'Harga Terendah':
    plt.scatter(df1['Terendah'], df1['Terakhir'])
    plt.xlabel('Harga Terendah')
    plt.ylabel('Harga Terakhir')
    plt.title('Distribusi Harga Terendah terhadap Harga Terakhir')

elif selected_option == 'Volume':
    plt.scatter(df1['Vol.'], df1['Terakhir'])
    plt.xlabel('Volume')
    plt.ylabel('Harga Terakhir')
    plt.title('Distribusi Volume terhadap Harga Terakhir')

elif selected_option == 'Perubahan':
    plt.scatter(df1['Perubahan%'], df1['Terakhir'])
    plt.xlabel('Perubahan')
    plt.ylabel('Harga Terakhir')
    plt.title('Distribusi Perubahan terhadap Harga Terakhir')

# Menampilkan grafik
st.pyplot(plt)
('###')
