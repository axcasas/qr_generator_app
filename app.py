import streamlit as st
from PIL import Image
import io
import time

from qr_generator.main import create_qr_code  # Ensure this is your updated function with the delay
from gui.sidebar import Sidebar
from gui.layout import Layout

if __name__ == '__main__':

    st.set_page_config(layout='wide', page_icon='📸', page_title='Free QR Image Generator')
    
    layout, sidebar = Layout(), Sidebar()
    
    layout.show_header()
    
    # Input URL from user
    url = st.text_input("### Enter the URL to generate a QR code:")
    
    # Select format
    format_option = st.selectbox("Select image format:", ["PNG", "JPG"])

    if st.button("Generate QR Code"):
        st.session_state["generate_qr"] = True

    if st.session_state.get("generate_qr") and url:
        with st.spinner('Generating QR code... Please wait...'):

            # Delay added here to simulate processing time
            time.sleep(3)
            
            # Set output file path
            output_file = f"qr_code.{format_option.lower()}"
            
            # Generate QR code
            create_qr_code(url, output_file)
            st.balloons()
            
            # Read the generated QR code image
            with open(output_file, "rb") as image_file:
                img_bytes = image_file.read()
            
            # Display the QR code image
            st.image(output_file, caption="Generated QR Code", use_column_width=True)
            
            # Download button
            st.download_button(
                label="Download QR Code",
                data=img_bytes,
                file_name=f"qr_code.{format_option.lower()}",
                mime=f"image/{format_option.lower()}"
            )

            # Show bottom
            layout.show_bottom()
            
            # Reset the flag after generating the QR code
            st.session_state["generate_qr"] = False

    elif st.session_state.get("generate_qr"):
        st.error("Please enter a valid URL.")
    
    sidebar.show_options()
    sidebar.about()
