import streamlit as st
from pymongo import MongoClient
from screens.home import home_screen
from screens.profile import profile_screen
from screens.mesa import mesa_screen
from screens.ruleta import ruleta_screen
from screens.chat import chat_screen
from screens.recomendador import recomendador_screen
from dotenv import load_dotenv
load_dotenv()

#MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client["Christmas"]
users_collection = db["wish"]

st.set_page_config(
    page_title = "Christmas Companion",
    page_icon="🎄",
    layout="wide",
)

if 'screen' not in st.session_state:
    st.session_state.screen = 'home'

def change_screen(screen):
    st.session_state.screen = screen

def login(username):
    user = users_collection.find_one({"username": username})
    if user:
        st.session_state.logged_in = True
        st.session_state.username = username
        st.session_state.family_group = user.get("family_group")
        if username == "admin":
            st.session_state.admin = True
        else:
            st.session_state.admin = False
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
    if st.sidebar.button("Login"):
        if login(username):
            st.sidebar.success("Logged in as {}".format(username))
        else:
            st.sidebar.error("Invalid username")


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
    if st.sidebar.button('Recomendador'):
        change_screen('recomendador')

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
    elif st.session_state.screen == 'recomendador':
        recomendador_screen()
else:
    st.write("Por favor, inicia sesión para acceder a la aplicación.")
