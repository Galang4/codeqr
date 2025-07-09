# app.py
import streamlit as st
import qrcode
from PIL import Image

st.set_page_config(page_title="QR Code Generator", layout="centered")
st.title("🔗 YouTube QR Code Generator")

link = st.text_input("Masukkan link YouTube:")

if link:
    qr = qrcode.QRCode(version=10, box_size=5, border=3)
    qr.add_data(link)
    qr.make()
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrcode.png")
    st.image(Image.open("qrcode.png"), caption="Scan me!", use_column_width=True)
