import streamlit as st
from utils.aux_functions import load_css, load_image

def profile_screen():
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
            <h2>Perfil de Usuario</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    with st.form("profile_form"):
        nombre = st.text_input("Nombre")
        comida = st.text_input("Comidas Favoritas")
        intereses = st.text_input("Cosas que te Gustan")
        afinidad_politica = st.selectbox(
            "Afinidad Política",
            ["Prefiero no decir", "Extrema Izquierda", "Izquierda", "Centro", "Derecha", "Extrema Derecha"]
        )
        alergias = st.text_area("Alergias")
        musica = st.text_input("Gustos Musicales")
        
        submitted = st.form_submit_button("Guardar")
        if submitted:
            # Here you can add code to save to database
            st.success("Perfil actualizado con éxito!")
            user_data = {
                "nombre": nombre,
                "comida": comida,
                "intereses": intereses,
                "afinidad_politica": afinidad_politica,
                "alergias": alergias,
                "musica": musica
            }
            st.session_state.db.users.update_one(
                {"_id": st.session_state.user_id},
                {"$set": user_data},
                upsert=True
            )