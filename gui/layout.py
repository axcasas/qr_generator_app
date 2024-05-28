import streamlit as st

class Layout:

    def show_header(self):
        
        st.markdown(
            """
            <h1 style='text-align: center;'>Free QR Code Generator 📷</h1>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """

            Create QR images for free in just 5 steps:
            1. Paste your URL
            2. Select whether you want it in PNG or JPG format
            3. Edit the QR parameters as you wish 
            4. Click on generate QR
            5. Download your QR
            """
        )

    def show_bottom(self):
        
        st.markdown(
            """
            <h3 style='text-align: center;'><a href="https://www.paypal.com/donate/?hosted_button_id=ZK2XTGUNXAKLQ" target="_blank">Support this free website by buying me a coffee ☕️</a></h3>
            """,
            unsafe_allow_html=True,
        )