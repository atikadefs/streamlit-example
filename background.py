import streamlit as st

def main():
    # Menggunakan HTML dan CSS kustom untuk mengatur gambar latar belakang
page_bg_img = '''
<style>
.stApp {
    background-image: url("https://github.com/atikadefs/streamlit-example/blob/master/Cone%20Nebula%20(NGC2264).jpeg");
    background-size: cover;
}
</style>
'''

    st.title('Aplikasi dengan Background Gambar')
    st.write('Ini adalah konten aplikasi dengan background gambar.')

if __name__ == "__main__":
    main()
