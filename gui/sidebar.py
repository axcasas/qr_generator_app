import streamlit as st
import qrcode

class Sidebar:

    # QR Code parameter constants
    BOX_SIZE_DEFAULT = 10
    BORDER_SIZE_DEFAULT = 4
    ERROR_CORRECTION_OPTIONS = {
        'Low (L)': qrcode.constants.ERROR_CORRECT_L,
        'Medium (M)': qrcode.constants.ERROR_CORRECT_M,
        'Quartile (Q)': qrcode.constants.ERROR_CORRECT_Q,
        'High (H)': qrcode.constants.ERROR_CORRECT_H,
    }
    ERROR_CORRECTION_DEFAULT = 'Low (L)'

    @staticmethod
    def about():
        about = st.sidebar.expander("About The Author")
        sections = [
            "#### App created with [Qrcode](https://pypi.org/project/qrcode/) and [Streamlit](https://github.com/streamlit/streamlit) ⚡",
            "#### Link to the code: [github.com/axcasas](https://github.com/axcasas)",
            "#### Follow me on [LinkedIn](https://www.linkedin.com/in/axel-casas/)",
            "#### Read my articles on [Medium](https://medium.com/@axel.em.casas)"
        ]

        for section in sections:
            about.write(section)

    @staticmethod
    def generate_qr_button():
        if st.button("Generate New QR Code"):
            st.session_state["generate_qr"] = True
        st.session_state.setdefault("generate_qr", False)

    @staticmethod
    def qr_code_options():
        with st.sidebar.expander("QR Code Options", expanded=True):
            st.session_state['box_size'] = st.slider("Box Size", min_value=1, max_value=20, value=Sidebar.BOX_SIZE_DEFAULT)
            st.session_state['border_size'] = st.slider("Border Size", min_value=1, max_value=10, value=Sidebar.BORDER_SIZE_DEFAULT)
            st.session_state['error_correction'] = st.selectbox("Error Correction Level", options=list(Sidebar.ERROR_CORRECTION_OPTIONS.keys()), index=0)

    def show_options(self):
        with st.sidebar.expander("🛠️ Tools", expanded=True):
            self.generate_qr_button()
            self.qr_code_options()