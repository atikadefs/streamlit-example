import streamlit as st

# Menambahkan CSS untuk latar belakang
st.markdown(
    """
    <style>
    body {
        background-image: url('https://github.com/atikadefs/streamlit-example/blob/master/Cone%20Nebula%20(NGC2264).jpeg');
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Konten aplikasi Streamlit
st.title('Aplikasi dengan Latar Belakang')
st.write('Konten aplikasi Streamlit di sini...')
