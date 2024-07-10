import streamlit as st
from classes import clsPageSetup as ps
from PIL import Image
import io

# 0. App Config
ps.PageUtilities.app_style()
ps.PageUtilities.app_logo()







st.markdown("""
<style>
    body { background-color: #f0f2f6; font-family: Arial, sans-serif; }
    .stApp { background-color: #f0f2f6; }
    .container { display: flex; justify-content: space-between; }
    .column { width: 48%; }
    h2 { color: #333; margin-bottom: 20px; }
    .stTextInput>div>div>input { background-color: #4B0082; color: white; }
    .stSelectbox>div>div>div { background-color: #4B0082; color: white; }
    .stTextArea>div>div>textarea { background-color: #4B0082; color: white; }
    .stButton>button { background-color: #9146FF; color: white; }
    .stButton>button:hover { background-color: #7D3CFF; }
    .output-text { color: #4B0082; font-weight: bold; }
    .stFileUploader>div>div>button { background-color: #4B0082; color: white; }
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("<h2>Story Elements</h2>", unsafe_allow_html=True)
    
    title = st.text_input("", placeholder="Enter title")
    summary = st.text_area("", placeholder="Enter summary", height=100)
    main_character = st.text_input("", placeholder="Enter main character")
    genre = st.selectbox("", ["Select genre", "Fantasy", "Science Fiction", "Mystery", "Romance"])
    theme = st.text_area("", placeholder="Enter theme", height=100)
    
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
    
    if st.button("Generate Story"):
        # Here you would typically call your story generation function
        generated_title = "Generated Title"
        generated_summary = "This is where your generated story summary would appear."

with col2:
    st.markdown("<h2>Generated Story</h2>", unsafe_allow_html=True)
    
    st.markdown("<p class='output-text'>Title</p>", unsafe_allow_html=True)
    if 'generated_title' in locals():
        st.write(generated_title)
    else:
        st.write("Your generated title will appear here.")
    
    st.markdown("<p class='output-text'>Summary</p>", unsafe_allow_html=True)
    if 'generated_summary' in locals():
        st.write(generated_summary)
    else:
        st.write("Your generated story summary will appear here.")