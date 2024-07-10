import streamlit as st


class StoryElements:
    def __init__(self):
        self.initialize_attributes()
        
    def initialize_attributes(self):
        self.story_elements = dict(st.secrets.storyelements)
        for key, value in self.story_elements:
            setattr(self, key, value)