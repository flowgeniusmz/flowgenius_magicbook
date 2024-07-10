import streamlit as st
from classes import clsPageSetup as ps
from PIL import Image
import io

# 0. App Config
page = 4
ps.PageUtilities.app_style()
ps.PageUtilities.app_logo()
ps.PageUtilities.page_header(page_number=page)