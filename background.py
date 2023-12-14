import streamlit as st

def main():
    # Menambahkan CSS untuk mengatur gambar sebagai background
    st.markdown(
        """
        <style>
        body {
            background-image: url('https://github.com/atikadefs/streamlit-example/blob/master/Cone%20Nebula%20(NGC2264).jpeg/'); /* Ganti URL dengan URL gambar Anda */
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title('Aplikasi dengan Background Gambar')
    st.write('Ini adalah konten aplikasi dengan background gambar.')

if __name__ == "__main__":
    main()
