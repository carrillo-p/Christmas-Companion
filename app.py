import streamlit as st
from pymongo import MongoClient
from screens.home import home_screen
from screens.profile import profile_screen
from screens.mesa import mesa_screen
from screens.ruleta import ruleta_screen
from screens.recetas import recetas_screen
from screens.recomendador import recomendador_screen
from screens.playlist import playlist_screen
from screens.tarjeta import tarjeta_screen

#MongoDB connection
client = MongoClient('localhost', 27017)
db = client["christmas_companion"]
users_collection = db["users"]

st.set_page_config(
    page_title = "Christmas Companion",
    page_icon="🎄"
    layout="wide",
)

if 'screen' not in st.session_state:
    st.session_state.screen = 'home'

def change_screen(screen):
    st.session_state.screen = screen

def login(username, password):
    user = users_collection.find_one({"username": username, "password": password})
    if user:
        st.session_state.logged_in = True
        st.session_state.username = username
        st.session_state.family_group = user["family_group"]
        return True
    return False

def logout():
    st.session_state.logged_in = False
    st.session_state.username = None
    st.session_state.family_group = None

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = None
    st.session_state.family_group = None

if not st.session_state.logged_in:
    st.sidebar.header('Login')
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        if login(username, password):
            st.sidebar.success("Logged in as {}".format(username))
        else:
            st.sidebar.error("Invalid username or password")

else:
# Menu de navegación
    st.sidebar.header('Menú')
    st.sidebar.markdown('---')
    if st.sidebar.button('Home'):
        change_screen('home')
    if st.sidebar.button('Perfil'):
        change_screen('profile')
    if st.sidebar.button('Mesa'):
        change_screen('mesa')
    if st.sidebar.button('Ruleta'):
        change_screen('ruleta')
    if st.sidebar.button('Chat'):
        change_screen('chat')
    if st.sidebar.button('Tarjeta'):
        change_screen('tarjeta')

# Cambio de pantalla
if st.session_state.logged_in:
    if st.session_state.screen == 'home':
        home_screen()
    elif st.session_state.screen == 'profile':
        profile_screen()
    elif st.session_state.screen == 'mesa':
        mesa_screen()
    elif st.session_state.screen == 'ruleta':
        ruleta_screen()
    elif st.session_state.screen == 'chat':
        chat_screen()
    elif st.session_state.screen == 'tarjeta':
        tarjeta_screen()
else:
    st.write("Por favor, inicia sesión para acceder a la aplicación.")
