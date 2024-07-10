import streamlit as st
from classes import clsPageSetup as ps
from PIL import Image
from streamlit_extras.stylable_container import stylable_container as sc
import io

# 0. App Config
page = 4
ps.PageUtilities.app_style()
ps.PageUtilities.app_logo()
ps.PageUtilities.page_header(page_number=page)


styles = dict(st.secrets.styles)
for key, value in styles.items():
    st.markdown(key)
    outer = sc(key=f"outer_{key}", css_styles=value)
    with outer:
        inner = st.container(height=100, border=False)
    st.divider()
