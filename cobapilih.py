import streamlit as st

# Meminta pengguna untuk memilih antara 'Satu' atau 'Dua'
pilihan = st.radio("Pilih satu:", ("Satu", "Dua"))

if pilihan == "Satu":
    # Menampilkan gambar jika 'Satu' dipilih
    st.image('https://github.com/atikadefs/streamlit-example/blob/master/Cone%20Nebula%20(NGC2264).jpeg', caption='Gambar yang ditampilkan')

elif pilihan == "Dua":
    # Menampilkan video jika 'Dua' dipilih
    st.video('https://github.com/atikadefs/streamlit-example/blob/master/Video%20tanpa%20judul%20%E2%80%90%20Dibuat%20dengan%20Clipchamp%20(1)%20(1).mp4', start_time=0)
