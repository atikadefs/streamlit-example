import streamlit as st
#Menggunakan HTML dan CSS kustom untuk mengatur gambar latar belakang
page_bg_img = '''
<style>
.stApp {
    background-image: url("https://raw.githubusercontent.com/enjunaja/belajar-vektor/main/gambar/background.png");
    background-size: cover;
}
</style>
'''
def main():
    st.title('Aplikasi Menu Sederhana')

    # Membuat pilihan menu
    menu_options = ['Beranda', 'Profil', 'Pengaturan']

    # Menampilkan pilihan menu dalam bentuk dropdown
    selected_menu = st.sidebar.selectbox('Menu', menu_options)

    # Mengatur konten berdasarkan pilihan menu yang dipilih
    if selected_menu == 'Beranda':
        st.write('Selamat datang di halaman Beranda!')
        # Tambahkan konten atau fitur untuk halaman Beranda di sini
    elif selected_menu == 'Profil':
        st.write('Ini adalah halaman Profil!')
        # Tambahkan konten atau fitur untuk halaman Profil di sini
    elif selected_menu == 'Pengaturan':
        st.write('Halaman Pengaturan')
        # Tambahkan konten atau fitur untuk halaman Pengaturan di sini

if __name__ == "__main__":
    main()
