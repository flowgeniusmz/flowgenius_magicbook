import streamlit as st
from typing import Literal
import base64

class PageUtilities:
   
    @staticmethod
    def app_style():
        with open(file=st.secrets.app.style, mode='r') as file:
            st.markdown(f'<style>{file.read()}</style>', unsafe_allow_html=True)

    @staticmethod
    def app_logo():
        st.logo(image=st.secrets.app.logo, link=None, icon_image=st.secrets.app.icon)

    @staticmethod
    def page_header(page_number: int):
        title = "MagicBook: "
        subtitle = st.secrets.pages.titles[page_number]
        description = st.secrets.pages.descriptions[page_number]
        template = '<style>body {{ background-color: #1E1E2E; }}.main-text {{ font-size: 48px; font-weight: bold; color: white; margin-bottom: 10px; }}.gradient-text {{ background: linear-gradient(90deg, #A78BFA, #EC4899); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}.subheader {{ font-size: 18px; color: #B0B0B0; margin-bottom: 20px; }}.stButton > button {{ background-color: #8B5CF6; color: white; padding: 10px 20px; border-radius: 5px; border: none; cursor: pointer; font-size: 16px; }}.stButton > button:hover {{ background-color: #7C3AED; }}.footer {{ font-size: 16px; color: white; margin-top: 20px; }}.footer-highlight {{ color: #EC4899; }}</style><div style="text-align: center; padding: 20px; max-width: 800px; margin: 0 auto;"><p class="main-text">{title} <span class="gradient-text">{subtitle}</span></p><p class="subheader">{description}</p></div>'
        st.markdown(template.format(title=title, subtitle=subtitle, description=description), unsafe_allow_html=True)

    @staticmethod
    def book_background(type: Literal["front", "open", "back"]):
        #style_template = '<style>.stApp {{background: linear-gradient(rgb(66, 44, 86, 0.7) 0%, rgb(146, 117, 133, 0.7) 100%), url("data:image/png;base64,{0}"); background-attachment: fixed; background-clip: border-box; background-color: rgba(0, 0, 0, 0); background-origin: padding-box; background-position: center; background-repeat: no-repeat; background-size: contain; width: 100vw; height: 100vh;}}</style>'
        style_template = '<style>.book-background {{background-image: url("data:image/png;base64,{0}"); background-position: center; background-repeat: no-repeat; background-size: contain; width: 100%; height: 80vh; margin-top: 20px;}}</style><div class="book-background"></div>'
        if type == "front":
            path = st.secrets.imagepaths.frontbook1
        elif type == "back":
            path = st.secrets.imagepaths.backbook1
        elif type == "open":
            path = st.secrets.imagepaths.openbook1
        with open(file=path, mode="rb") as file:
            encoded_file = base64.b64encode(s=file.read()).decode()
        background = style_template.format(encoded_file)
        st.markdown(body=background, unsafe_allow_html=True)


# background_page2 = '<style>.stApp {{background-image: linear-gradient(rgb(66, 44, 86) 0%, rgb(146, 117, 133) 100%), url("data:image/png;base64,{0}"); background-attachment: fixed; background-clip: border-box; background-color: rgba(0, 0, 0, 0); background-origin: padding-box; background-position: center; background-repeat: no-repeat; background-size: cover; width: 100vw; height: 100vh;}}</style>'
# background_page = '<style>.stApp {{background: linear-gradient(rgb(66, 44, 86, 0.7) 0%, rgb(146, 117, 133, 0.7) 100%), url("data:image/png;base64,{0}"); background-attachment: fixed; background-clip: border-box; background-color: rgba(0, 0, 0, 0); background-origin: padding-box; background-position: center; background-repeat: no-repeat; background-size: cover; width: 100vw; height: 100vh;}}</style>'
# background_page1 = '<style>.stApp {{background: url("data:image/png;base64,{0}"), rgba(255, 255, 255, 0.5); background-size: cover; background-blend-mode: lighten; background-position: center; background-repeat: no-repeat;}}</style>'
# styling_page = '<style>{0}</style>'