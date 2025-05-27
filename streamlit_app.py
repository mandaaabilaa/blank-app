import streamlit as st

st.title(" selamat datang di website mandaabilaa ")
st.write(
    "Let's start building!"
) 
st.image("0e00fdc34a6c8bb474a27e5e43c96744.jpg", width=200)


st.title("Aplikasi Sederhana ")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah angka:",value=0,step=1)

if (angka % 2 ) == 0:
  st.write(f"{angka} adalah Bilangan Genap")
else:
  st.write(f"{angka} adalah Bilangan Ganjil")
