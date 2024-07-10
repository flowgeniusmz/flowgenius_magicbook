import streamlit as st
from classes import clsPageSetup as ps


# 0. App Config
page = 3
ps.PageUtilities.app_style()
ps.PageUtilities.app_logo()
ps.PageUtilities.page_header(page_number=page)