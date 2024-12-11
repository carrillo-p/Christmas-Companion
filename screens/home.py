import streamlit as st
from utils.aux_functions import load_css, load_image

def home_screen():
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
            <h2>Nuestros Servicios</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="service-box">
        <h3>Planificación de Eventos</h3>
        <p>Ofrecemos un servicio completo de planificación de eventos navideños. Desde la organización de la cena hasta la decoración del hogar, nuestra app te ayudará a crear una experiencia inolvidable para ti y tus seres queridos.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="service-box">
        <h3>Recetas Navideñas</h3>
        <p>Descubre una amplia variedad de recetas navideñas para sorprender a tus invitados. Nuestra app te proporciona instrucciones detalladas y listas de ingredientes para que puedas preparar deliciosos platillos navideños.</p>
        </div>
        """, unsafe_allow_html=True)

    col3, col4 = st.columns(2)

    with col3:
        st.markdown("""
        <div class="service-box">
        <h3>Distribución de Asientos</h3>
        <p>¿Preocupado por la organización de la mesa? Nuestro planificador inteligente te ayuda a crear la disposición perfecta de asientos, considerando las dinámicas familiares y preferencias de tus invitados para una cena armoniosa.</p>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
        <div class="service-box">
        <h3>Playlists Personalizadas</h3>
        <p>Crea el ambiente perfecto con nuestro recomendador de música. Desde villancicos tradicionales hasta música moderna navideña, te ayudamos a encontrar la combinación perfecta para mantener el espíritu festivo.</p>
        </div>
        """, unsafe_allow_html=True)


    st.markdown(
        """
        <div style="text-align: center;">
            <h4>Estos servicios están diseñados para ofrecerte una experiencia navideña completa y sin estrés. Con nuestra tecnología avanzada, puedes asegurarte de que cada detalle de tus celebraciones sea perfecto.<h4>
            <h4>Juntos, hagamos de esta Navidad una celebración inolvidable para todos.<h4>
        </div>
        """,
        unsafe_allow_html=True
    )