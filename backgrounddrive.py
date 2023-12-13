import streamlit as st

def main():
    # URL gambar dari Google Drive yang dapat diakses publik
    url_gambar = 'https://drive.google.com/file/d/1gc9W5DlQmEegj9RkJi_l44V1TJ8ezQUd/view?usp=sharing'  # Ganti dengan URL gambar Anda

    # Menambahkan CSS untuk mengatur gambar sebagai background
    st.markdown(
        f"""
        <style>
        body {{
            background-image: url('{url_gambar}');
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title('Aplikasi dengan Background Gambar dari Google Drive')
    st.write('Ini adalah konten aplikasi dengan background gambar dari Google Drive.')

if __name__ == "__main__":
    main()
