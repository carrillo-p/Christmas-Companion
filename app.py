import streamlit as st

# Debe ser la primera llamada a Streamlit
st.set_page_config(
    page_title = "Christmas Companion",
    page_icon="🎄",
    layout="wide",
)

from pymongo import MongoClient
from screens.home import home_screen
from screens.profile import profile_screen
from screens.mesa import mesa_screen
from screens.ruleta import ruleta_screen
from screens.chat import chat_screen
from screens.recomendador import recomendador_screen
from screens.signup import signup_screen
from screens.tarjetas import tarjetas_screen

# Inicialización del session_state
if 'screen' not in st.session_state:
    st.session_state.screen = 'home'

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = None
    st.session_state.family_group = None

# MongoDB connection con manejo de errores
if 'db' not in st.session_state:
    try:
        client = MongoClient('mongodb://localhost:27017/')
        st.session_state.client = client
        st.session_state.db = client["Crhistmas"]
        st.session_state.users_collection = st.session_state.db["wish"]
        # Verificar conexión
        client.admin.command('ping')
        st.sidebar.success("✅ Conectado a MongoDB")
    except Exception as e:
        st.sidebar.error(f"❌ Error de conexión a MongoDB: {e}")

def change_screen(screen):
    st.session_state.screen = screen

def login(username, password):
    try:
        # Verificar si es admin
        if username == "admin" and password == "admin":
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.family_group = "admin"
            return True

        # Verificar en la base de datos
        user = st.session_state.users_collection.find_one({"username": username, "password": password})
        if user:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.family_group = user.get("family_group", "default")
            return True
        return False
    except Exception as e:
        st.error(f"Error en login: {e}")
        return False

def logout():
    st.session_state.logged_in = False
    st.session_state.username = None
    st.session_state.family_group = None

# Interfaz de login
if not st.session_state.logged_in:
    st.sidebar.header('Login')
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    col1, col2 = st.sidebar.columns(2)

    with col1:
        if st.button("Login"):
            if login(username, password):
                st.sidebar.success(f"Bienvenido {username}!")
                st.rerun()
            else:
                st.sidebar.error("Usuario o contraseña inválidos")

    with col2:
        if st.button("Registrarse"):
            change_screen('signup')

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
    if st.sidebar.button('Tarjetas'):
        change_screen('tarjetas')
    if st.sidebar.button('Sign Up'):
        signup_screen()
    if st.sidebar.button('Logout'):
        logout()
        st.rerun()

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
    elif st.session_state.screen == 'tarjetas':
        tarjetas_screen()
    elif st.session_state.screen == 'signup':
        signup_screen()
else:
    st.write("Por favor, inicia sesión para acceder a la aplicación.")