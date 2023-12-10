import streamlit as st
import plotly_express as px
import pandas as pd

# Konfigurasi
st.set_option('deprecation.showfileUploaderEncoding', False)

# Judul Form
st.title('Visualisasi Data')

# Membuat Sidebar
st.sidebar.subheader("Setting Visualisasi")

# Menggunakan komponen file uploader
upload_file = st.sidebar.file_uploader(label='Upload Data CSV/Excel', type=['csv', 'xlsx'])

# Inisialisasi DataFrame
df = None
numeric_columns = []

if upload_file is not None:
    try:
        df = pd.read_csv(upload_file)
    except Exception as e:
        print(e)
        df = pd.read_excel(upload_file)

if df is not None:
    st.write(df)
    # Inisialisasi kolom numerik
    numeric_columns = list(df.select_dtypes(['float64', 'int64']).columns)

# Memasukkan widget ke dalam sidebar
chart_select = st.sidebar.selectbox(
    label='Pilih Tipe Grafik',
    options=['Scatterplots', 'Lineplots', 'Histogram', 'Boxplot']
)

if chart_select == 'Scatterplots':
    st.sidebar.subheader('Scatterplot Settings')

    if numeric_columns:
        x_values = st.sidebar.selectbox('Sumbu X', options=numeric_columns)
        y_values = st.sidebar.selectbox('Sumbu Y', options=numeric_columns)
        plot = px.scatter(data_frame=df, x=x_values, y=y_values)
        # Menampilkan grafik
        st.plotly_chart(plot)
    else:
        st.sidebar.text("Tidak ada kolom numerik untuk ditampilkan.")

elif chart_select == 'Lineplots':
    st.sidebar.subheader('Lineplot Settings')

    if numeric_columns:
        x_values = st.sidebar.selectbox('Sumbu X', options=numeric_columns)
        y_values = st.sidebar.selectbox('Sumbu Y', options=numeric_columns)
        plot = px.line(data_frame=df, x=x_values, y=y_values)
        # Menampilkan grafik
        st.plotly_chart(plot)
    else:
        st.sidebar.text("Tidak ada kolom numerik untuk ditampilkan.")

elif chart_select == 'Histogram':
    st.sidebar.subheader('Histogram Settings')

    if numeric_columns:
        x_values = st.sidebar.selectbox('Pilih Kolom untuk Histogram', options=numeric_columns)
        plot = px.histogram(data_frame=df, x=x_values)
        # Menampilkan grafik
        st.plotly_chart(plot)
    else:
        st.sidebar.text("Tidak ada kolom numerik untuk ditampilkan.")

elif chart_select == 'Boxplot':
    st.sidebar.subheader('Boxplot Settings')

    if numeric_columns:
        y_values = st.sidebar.selectbox('Pilih Kolom untuk Boxplot', options=numeric_columns)
        plot = px.box(data_frame=df, y=y_values)
        # Menampilkan grafik
        st.plotly_chart(plot)
    else:
        st.sidebar.text("Tidak ada kolom numerik untuk ditampilkan.")
