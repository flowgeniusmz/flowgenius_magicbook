import streamlit as st
from classes import clsPageSetup as ps
from PIL import Image
import io

# 0. App Config
page = 1
ps.PageUtilities.app_style()
ps.PageUtilities.app_logo()
ps.PageUtilities.page_header(page_number=page)

# 1. Session State
if "elements_initialized" not in st.session_state:
    st.session_state.elements_initialized = True
    st.session_state.title = None
    st.session_state.summary = None
    st.session_state.outline = None
    st.session_state.narrative = None
    st.session_state.character_desc = None
    st.session_state.character_image = None
    st.session_state.genre = None
    st.session_state.setting = None
    st.session_state.uploaded_image = None
    st.session_state.uploaded_image_type = None
    st.session_state.submitted = False
    st.session_state.approved = False
    st.session_state.current_step = 1

main_container = st.container()
with main_container:
    cols = st.columns(2)
    with cols[0]:
        form_container = st.container()
        with form_container:
            if st.session_state.current_step == 1:
                st.markdown("### Welcome to the storybook creator")
                st.markdown("Upload the image of your loved one:")
                uploaded_image = st.file_uploader(label="Upload an Image", type=["png", "jpg", "jpeg", "gif"])
                if uploaded_image is not None:
                    st.session_state.uploaded_image = uploaded_image
                    st.image(uploaded_image, caption='Uploaded Image', use_column_width=True)
                    st.markdown("Great Image! If you're satisfied by this upload, let's continue with selecting some story elements. Hit 'Next' to continue.")
                
                next_btn = st.button("Next")
                if next_btn:
                    st.session_state.current_step = 2

            elif st.session_state.current_step == 2:
                genre = st.text_input("Genre", value=st.session_state.genre)
                setting = st.text_input("Setting", value=st.session_state.setting)
                prev_btn = st.button("Previous")
                submit = st.button("Submit")
                if submit:
                    st.session_state.genre = genre
                    st.session_state.setting = setting
                    st.session_state.submitted = True
                if prev_btn:
                    st.session_state.current_step = 1
            
    with cols[1]:
        title_container = st.container()
        with title_container:
            title_summary_form = st.form(key="title_summary")
            with title_summary_form:
                title = st.text_input(label="Title", value=st.session_state.title)
                summary = st.text_area(label="Summary", value=st.session_state.summary)
                approve = st.form_submit_button(label="Approve")
                if approve:
                    st.session_state.title = title
                    st.session_state.summary = summary
                    st.session_state.approved = True
        
    if st.session_state.approved and st.session_state.submitted:
        create_btn = st.button(label="Next: Create Your Story")
        if create_btn:
            st.switch_page("app/create.py")
