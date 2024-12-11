import streamlit as st
from utils.aux_functions import load_css, load_image
from pymongo import MongoClient

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["christmas_companion"]
users_collection = db["users"]

def check_unique_username(username):
    return users_collection.find_one({"username": username}) is None

def check_unique_family(family_name):
    return users_collection.find_one({"family_group": family_name}) is None

def signup_screen():
    load_css('style.css')
    image = load_image('logo 2.png')
    
    st.markdown(
    f"""
    <div style="display: flex; justify-content: center;">
        <img src="data:image/png;base64,{image}" width="150">
    </div>
    """,
    unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="text-align: center;">
            <h2>Registro de Usuario</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    with st.form("signup_form"):
        username = st.text_input("Nombre de Usuario")
        password = st.text_input("Contraseña", type="password")
        confirm_password = st.text_input("Confirmar Contraseña", type="password")
        family_name = st.text_input("Nombre de tu Familia")
        
        submitted = st.form_submit_button("Registrarse")
        
        if submitted:
            if not username or not password or not family_name:
                st.error("Por favor, rellena todos los campos")
            elif password != confirm_password:
                st.error("Las contraseñas no coinciden")
            elif not check_unique_username(username):
                st.error("Este nombre de usuario ya está en uso")
            elif not check_unique_family(family_name):
                st.error("Este nombre de familia ya está en uso")
            else:
                user_data = {
                    "username": username,
                    "password": password,  # Storing password as plaintext for trial
                    "family_group": family_name,
                    "is_admin": True  # First user in family is admin
                }
                
                users_collection.insert_one(user_data)
                st.success("¡Registro exitoso! Por favor, inicia sesión.")
                st.session_state.screen = 'login'
