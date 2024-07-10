import streamlit as st
from classes import clsPageSetup as ps
from typing import Literal

# 0. App Config
ps.PageUtilities.app_style()
ps.PageUtilities.app_logo()

if "story_page_count" not in st.session_state:
    st.session_state.story_page_count = 10

if "create_step" not in st.session_state:
    st.session_state.create_step = 0

def callback_create_step(type: Literal["increment", "decrement"]):
    if type == "decrement":
        st.session_state.create_step -= 1
    elif type == "increment":
        st.session_state.create_step += 1


def get_start_button():
    start_button = st.button(label="Start", type="primary", use_container_width=False, on_click=callback_create_step, args=["increment"])
    return start_button

def get_next_button():
    next_button = st.button(label="Next", type="primary", use_container_width=False, on_click=callback_create_step, args=["increment"])
    return next_button

def get_previous_button():
    previous_button = st.button(label="Previous", type="primary", use_container_width=False, on_click=callback_create_step, args=["decrement"])
    return previous_button

def get_finish_button():
    finish_button = st.button(label="Finish", type="primary", use_container_width=False, on_click=callback_create_step, args=["increment"])
    return finish_button

# 1. Setup
header_container = st.container(height=100, border=False)
main_container = st.container(border=False)
with main_container:
    maincols = st.columns(spec=[2,20,2], vertical_alignment="center")
    with maincols[0]:
        left_btn_placeholder = st.empty()
    with maincols[1]:
        page_placeholder = st.empty()
    with maincols[2]:
        right_btn_placeholder = st.empty()
    
        
footer_container = st.container(height=100, border=False)

# 4 Fill
if st.session_state.create_step == 0:
    with right_btn_placeholder:
        rbutton = get_start_button()
    with page_placeholder:
        st.image(image="assets/images/book/frontbook.png")

elif st.session_state.create_step >= 0 and st.session_state.create_step < st.session_state.story_page_count:
    with left_btn_placeholder:
        lbutton = get_previous_button()
    with right_btn_placeholder:
        rbutton = get_next_button()
    with page_placeholder:
        st.image(image="assets/images/book/openbook.png")

elif st.session_state.create_step == st.session_state.story_page_count:
    with left_btn_placeholder:
        lbutton = get_previous_button()
    with right_btn_placeholder:
        rbutton = get_finish_button()
    with page_placeholder:
        st.image(image="assets/images/book/openbook.png")

elif st.session_state.create_step >= st.session_state.story_page_count:
    with page_placeholder:
        st.image(image="assets/images/book/backbook.png")
    with left_btn_placeholder:
        lbutton = get_previous_button()


