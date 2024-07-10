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

main_container = st.container(border=False)
with main_container:
    cols = st.columns(spec=2, vertical_alignment="top")
    with cols[0]:
        form_container = st.container(border=True, height=400)
        submit_placeholder = st.empty()
        with submit_placeholder:
            if st.session_state.submitted:
                st.success("Submitted")
        with form_container:
            style_elements_form = st.form(key="story_elements", border = False)
            with style_elements_form:
                genre = st.text_input("Genre")
                setting = st.text_input("Setting")
                uploaded_image = st.file_uploader(label="Upload an Image", type=["png", "jpg", "jpeg", "gif"])
                submit = st.form_submit_button("Submit", type="primary", use_container_width=True)
                if submit:
                    # with submit_placeholder:
                    #     st.success("Submitted")
                    st.session_state.submitted = True
            
    with cols[1]:
        title_container = st.container(border=True, height=400)
        approve_placeholder = st.empty()
        with approve_placeholder:
            if st.session_state.approved:
                st.success("Approved")
        with title_container:
            title_summary_form = st.form(key="title_summary", border=False)
            with title_summary_form:
                title = st.text_input(label="Title", value=st.session_state.title)
                summary = st.text_area(label="Summary", value=st.session_state.summary)
                approve = st.form_submit_button(label="Approve", type="primary", use_container_width=True)
                if approve:
                    # with approve_placeholder:
                    #     st.success("Approved")
                    st.session_state.approved = True
    if st.session_state.approved and st.session_state.submitted:
        create_btn = st.button(label="Next: Create Your Story", type="primary", use_container_width=True)
        if create_btn:
            st.switch_page("app/create.py")

