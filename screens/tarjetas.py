import streamlit as st
from utils.aux_functions import load_css, load_image
import openai
import requests
from io import BytesIO
import base64

def generate_image(prompt):
    try:
        response = openai.Image.create(
            prompt=f"Christmas card design with: {prompt}",
            n=1,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']
        return image_url
    except Exception as e:
        st.error(f"Error generating image: {str(e)}")
        return None

def tarjetas_screen():
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
            <h2>Generador de Tarjetas Navideñas</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Text input for card description
    card_description = st.text_area(
        "Describe cómo quieres que sea tu tarjeta navideña",
        placeholder="Por ejemplo: Una tarjeta con un reno alegre patinando sobre hielo con luces navideñas..."
    )

    if st.button("Generar Tarjeta"):
        if card_description:
            with st.spinner('Generando tu tarjeta navideña...'):
                image_url = generate_image(card_description)
                if image_url:
                    # Display generated image
                    st.markdown(
                        f"""
                        <div style="display: flex; justify-content: center; margin: 20px 0;">
                            <img src="{image_url}" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                    
                    # Download button
                    response = requests.get(image_url)
                    image_bytes = BytesIO(response.content)
                    st.download_button(
                        label="Descargar Tarjeta",
                        data=image_bytes,
                        file_name="tarjeta_navidad.png",
                        mime="image/png"
                    )
        else:
            st.warning("Por favor, describe cómo quieres que sea tu tarjeta.")
