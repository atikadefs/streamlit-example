import streamlit as st

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
    def main():
    # Menambahkan CSS untuk mengubah background
    st.markdown(
        """
        <style>
        body {
            background-color: #f0f0f0; /* Ganti dengan warna yang Anda inginkan */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title('Aplikasi dengan Background Baru')
    st.write('Ini adalah konten aplikasi dengan background baru.')

if __name__ == "__main__":
    main()

    elif selected_menu == 'Profil':
        st.write('Ini adalah halaman Profil!')
        # Tambahkan konten atau fitur untuk halaman Profil di sini
    elif selected_menu == 'Pengaturan':
        st.write('Halaman Pengaturan')
        # Tambahkan konten atau fitur untuk halaman Pengaturan di sini

if __name__ == "__main__":
    main()
