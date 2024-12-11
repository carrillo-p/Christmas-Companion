import streamlit as st
from utils.aux_functions import load_css, load_image
from datetime import datetime

def profile_screen():
    if st.session_state.logged_in:
        try:
            # Cargar estilos e imagen
            load_css('style.css')
            image = load_image('logo 2.png')
            if image:
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

            # Obtener información actual del usuario
            user = st.session_state.users_collection.find_one({"username": st.session_state.username})

            with st.form("profile_form"):
                # Mostrar campos con valores existentes si están disponibles
                nombre = st.text_input("Nombre", value=user.get('nombre', '')) if user else st.text_input("Nombre")
                comida = st.text_input("Comidas Favoritas", value=user.get('comida', '')) if user else st.text_input("Comidas Favoritas")
                intereses = st.text_input("Cosas que te Gustan", value=user.get('intereses', '')) if user else st.text_input("Cosas que te Gustan")
                afinidad_politica = st.selectbox(
                    "Afinidad Política",
                    ["Prefiero no decir", "Extrema Izquierda", "Izquierda", "Centro", "Derecha", "Extrema Derecha"],
                    index=["Prefiero no decir", "Extrema Izquierda", "Izquierda", "Centro", "Derecha", "Extrema Derecha"].index(user.get('afinidad_politica', 'Prefiero no decir')) if user and user.get('afinidad_politica') else 0
                )
                alergias = st.text_area("Alergias", value=user.get('alergias', '')) if user else st.text_area("Alergias")
                musica = st.text_input("Gustos Musicales", value=user.get('musica', '')) if user else st.text_input("Gustos Musicales")

                submitted = st.form_submit_button("Guardar")
                if submitted:
                    try:
                        # Preparar datos del usuario
                        user_data = {
                            "nombre": nombre,
                            "comida": comida,
                            "intereses": intereses,
                            "afinidad_politica": afinidad_politica,
                            "alergias": alergias,
                            "musica": musica,
                            "updated_at": datetime.now()
                        }

                        # Actualizar en la base de datos
                        st.session_state.users_collection.update_one(
                            {"username": st.session_state.username},
                            {"$set": user_data},
                            upsert=True
                        )
                        st.success("¡Perfil actualizado con éxito!")
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error al actualizar el perfil: {e}")

        except Exception as e:
            st.error(f"Error al cargar el perfil: {e}")
    else:
        st.warning("Por favor, inicia sesión para ver tu perfil.")

    # Agregar algo de espacio al final
    st.markdown("<br><br>", unsafe_allow_html=True)