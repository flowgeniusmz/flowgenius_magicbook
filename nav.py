import streamlit as st


def create_pages():
    pages = []
    page_count = len(st.secrets.pages.paths)
    for i in range(page_count):
        page = st.Page(page=st.secrets.pages.paths[i], title=st.secrets.pages.titles[i], icon=st.secrets.pages.icons[i], url_path=st.secrets.pages.urls[i], default=bool(st.secrets.pages.defaults[i]))
        pages.append(page)
    return pages

def get_navigation():
    pages = create_pages()
    selected_page = st.navigation(pages=pages,)
    selected_page.run()