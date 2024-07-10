import streamlit as st
from classes import clsPageSetup as ps


# 0. App Config
# st.set_page_config(page_title=st.secrets.app.name, page_icon=st.secrets.app.icon, layout=st.secrets.app.layout, initial_sidebar_state=st.secrets.app.sidebar, menu_items={key: value for key, value in zip(st.secrets.app.menu_keys, st.secrets.app.menu_values)})
ps.PageUtilities.app_style()
ps.PageUtilities.app_logo()



# st.markdown("""
# <style>
#     body { background-color: #1E1E2E; }
#     .main-text { font-size: 48px; font-weight: bold; color: white; margin-bottom: 10px; }
#     .gradient-text { background: linear-gradient(90deg, #A78BFA, #EC4899); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
#     .subheader { font-size: 18px; color: #B0B0B0; margin-bottom: 20px; }
#     .custom-button { background-color: #8B5CF6; color: white; padding: 10px 20px; border-radius: 5px; border: none; cursor: pointer; font-size: 16px; text-decoration: none; display: inline-block; }
#     .custom-button:hover { background-color: #7C3AED; }
#     .footer { font-size: 16px; color: white; margin-top: 20px; }
#     .footer-highlight { color: #EC4899; }
# </style>

# <div style="text-align: center; padding: 20px; max-width: 800px; margin: 0 auto;">
#     <p class="main-text">Connect your stories <span class="gradient-text">to magic</span></p>
#     <p class="subheader">MagicBook AI creates custom storybooks in minutes through the power of AI. The output is cheaper and better than competitors.</p>
#     <a href="https://magicbookai.streamlit.app/start" class="custom-button">Get Started →</a>
#     <p class="footer">Check out our collaboration with <span class="footer-highlight">StoryAI</span></p>
# </div>
# """, unsafe_allow_html=True)

st.markdown("""
<style>
    body { background-color: #1E1E2E; }
    .main-text { font-size: 48px; font-weight: bold; color: white; margin-bottom: 10px; }
    .gradient-text { background: linear-gradient(90deg, #A78BFA, #EC4899); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .subheader { font-size: 18px; color: #B0B0B0; margin-bottom: 20px; }
    .stButton > button { 
        background-color: #8B5CF6; 
        color: white; 
        padding: 10px 20px; 
        border-radius: 5px; 
        border: none; 
        cursor: pointer; 
        font-size: 16px; 
    }
    .stButton > button:hover { background-color: #7C3AED; }
    .footer { font-size: 16px; color: white; margin-top: 20px; }
    .footer-highlight { color: #EC4899; }
</style>

<div style="text-align: center; padding: 20px; max-width: 800px; margin: 0 auto;">
    <p class="main-text">Connect your stories <span class="gradient-text">to magic</span></p>
    <p class="subheader">MagicBook AI creates custom storybooks in minutes through the power of AI. The output is cheaper and better than competitors.</p>
</div>
""", unsafe_allow_html=True)

if st.button("Get Started →"):
    # st.markdown("[Redirecting to Start Page](https://magicbookai.streamlit.app/start)")
    # st.markdown('<meta http-equiv="refresh" content="0; URL=https://magicbookai.streamlit.app/start">', unsafe_allow_html=True)
    st.switch_page()

# st.markdown("""
# <div style="text-align: center; padding: 20px; max-width: 800px; margin: 0 auto;">
#     <p class="footer">Check out our collaboration with <span class="footer-highlight">StoryAI</span></p>
# </div>
# """, unsafe_allow_html=True)

# st.markdown("""
# <style>
#     body { background-color: #1E1E2E; }
#     .main-text { font-size: 48px; font-weight: bold; color: white; margin-bottom: 10px; }
#     .gradient-text { background: linear-gradient(90deg, #A78BFA, #EC4899); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
#     .subheader { font-size: 18px; color: #B0B0B0; margin-bottom: 20px; }
#     .custom-button { background-color: #8B5CF6; color: white; padding: 10px 20px; border-radius: 5px; border: none; cursor: pointer; font-size: 16px; }
#     .custom-button:hover { background-color: #7C3AED; }
#     .footer { font-size: 16px; color: white; margin-top: 20px; }
#     .footer-highlight { color: #EC4899; }
# </style>

# <div style="text-align: center; padding: 20px; max-width: 800px; margin: 0 auto;">
#     <p class="main-text">Connect your stories <span class="gradient-text">to magic</span></p>
#     <p class="subheader">MagicBook AI creates custom storybooks in minutes through the power of AI. The output is cheaper and better than competitors.</p>
#     <button class="custom-button">Get Started →</button>
#     <p class="footer">Check out our collaboration with <span class="footer-highlight">StoryAI</span></p>
# </div>
# """, unsafe_allow_html=True)

# st.markdown("""
# <style>
#     .main-text { font-size: 48px; font-weight: bold; color: white; }
#     .gradient-text { background: linear-gradient(45deg, #8A2BE2, #FF69B4); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
#     .subheader { font-size: 18px; color: #B0B0B0; }
#     .custom-button { background-color: #8A2BE2; color: white; padding: 10px 20px; border-radius: 5px; border: none; cursor: pointer; }
#     .custom-button:hover { background-color: #9B30FF; }
#     .footer { font-size: 16px; color: #B0B0B0; }
# </style>

# <div style="text-align: center; padding: 20px;">
#     <p class="main-text">Connect your stories <span class="gradient-text">to magic</span></p>
#     <p class="subheader">MagicBook AI creates custom storybooks in minutes through the power of AI. The output is cheaper and better than competitors.</p>
#     <button class="custom-button">Get Started →</button>
#     <p class="footer">Check out our collaboration with StoryAI</p>
# </div>
# """, unsafe_allow_html=True)
