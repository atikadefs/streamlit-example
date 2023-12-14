import streamlit as st

# Mengimpor gambar dari lokal
from PIL import Image

# Menampilkan gambar dari URL
from io import BytesIO
import requests

# Menambahkan gambar dari URL
url = 'https://github.com/atikadefs/streamlit-example/blob/master/Cone%20Nebula%20(NGC2264).jpeg'
response = requests.get(url)
img = Image.open(BytesIO(response.content))

# Menampilkan gambar dari lokal
local_image = Image.open('nama_file_gambar_lokal.jpg')

# Menampilkan gambar di aplikasi Streamlit
st.image(img, caption='Gambar dari URL', use_column_width=True)
st.image(local_image, caption='Gambar dari lokal', use_column_width=True)
