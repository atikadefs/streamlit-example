import streamlit as st

# Meminta pengguna untuk memilih antara 'Satu' atau 'Dua'
pilihan = st.radio("Pilih satu:", ("Satu", "Dua"))

if pilihan == "Satu":
    # Menampilkan gambar jika 'Satu' dipilih
    st.image('link_gambar_di_sini', caption='Gambar yang ditampilkan')

elif pilihan == "Dua":
    # Menampilkan video jika 'Dua' dipilih
    st.video('link_video_di_sini', start_time=0)
