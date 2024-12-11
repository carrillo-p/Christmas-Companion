import streamlit as st
import base64
import os

def get_project_root():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(current_dir)

def load_image(image_name):
    project_root = get_project_root()
    image_path = os.path.join(project_root, 'assets', image_name)
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

def load_css(file_name):
    project_root = get_project_root()
    css_path = os.path.join(project_root, 'styles', file_name)
    with open(css_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)