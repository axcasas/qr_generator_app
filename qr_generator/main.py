import qrcode
import streamlit as st
from gui.sidebar import Sidebar
import time

def create_qr_code(link, output_file):
    """
    Generates a QR code image from the provided link and saves it to the specified output file.

    Parameters:
    link (str): The URL to encode in the QR code.
    output_file (str): The file path to save the generated QR code image.
    """
    # Get parameters from session state
    box_size = st.session_state.get('box_size', 10)
    border_size = st.session_state.get('border_size', 4)
    error_correction_level = st.session_state.get('error_correction', 'Low (L)')
    error_correction = Sidebar.ERROR_CORRECTION_OPTIONS[error_correction_level]

    time.sleep(3)

    # Create a QR code object
    qr = qrcode.QRCode(
        version=1,
        error_correction=error_correction,
        box_size=box_size,
        border=border_size,
    )

    # Add the link data to the QR code
    qr.add_data(link)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill='black', back_color='white')

    # Save the image to the specified file
    img.save(output_file)
