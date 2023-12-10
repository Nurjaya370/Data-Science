import streamlit as st
import pandas as pd
import joblib

# Impor model Machine Learning
linear_regression_model = joblib.load('Linier_regresi_model.joblib')
decision_tree_model = joblib.load('dtree_model.joblib')

def main():
    st.title('Aplikasi Prediksi Harga Emas')
    st.write('Masukkan fitur-fitur yang diperlukan untuk melakukan prediksi harga saham.')

    # Tampilkan form untuk input fitur-fitur
    feature1 = st.number_input('Pembukaan')
    feature2 = st.number_input('Tertinggi')
    feature3 = st.number_input('Terendah')
    feature4 = st.number_input('Vol.')
    feature5 = st.number_input('Perubahan%')
    feature_date = st.date_input('Tanggal')
    # Tombol untuk melakukan prediksi
    if st.button('Proses'):
        # Memecah tanggal menjadi empat fitur terpisah
        day = feature_date.day if feature_date else None
        week = feature_date.isocalendar()[1] if feature_date else None
        month = feature_date.month if feature_date else None
        year = feature_date.year if feature_date else None

        # Buat dataframe dengan fitur-fitur yang diinput
        data = pd.DataFrame({
            'Pembukaan': [feature1],
            'Tertinggi': [feature2],
            'Terendah': [feature3],
            'Vol.': [feature4],
            'Perubahan%': [feature5],
            'day': [day],
            'week': [week],
            'month': [month],
            'year': [year]
        })

        # Prediksi menggunakan model regresi linear
        linear_regression_prediction = linear_regression_model.predict(data)

        # Prediksi menggunakan model decision tree
        decision_tree_prediction = decision_tree_model.predict(data)

        # Tampilkan hasil prediksi
        st.write('Prediksi menggunakan Regresi Linear:', linear_regression_prediction)
        st.write('Prediksi menggunakan Decision Tree:', decision_tree_prediction)

if __name__ == '__main__':
    main()
