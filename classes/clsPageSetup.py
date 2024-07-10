import streamlit as st


class PageUtilities:
   
    @staticmethod
    def app_style():
        with open(file=st.secrets.app.style, mode='r') as file:
            st.markdown(f'<style>{file.read()}</style>', unsafe_allow_html=True)

    @staticmethod
    def app_logo():
        st.logo(image=st.secrets.app.logo, link=None, icon_image=st.secrets.app.icon)

    



