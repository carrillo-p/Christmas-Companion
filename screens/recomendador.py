import streamlit as st
from utils.aux_functions import load_css, load_image
from pymongo import MongoClient
import requests

client = MongoClient("mongodb://localhost:27017/")
db = client["christmas_companion"]
users_collection = db["users"]

def get_ai_recommendations(recipient_data):
    # Simulated AI API call - replace with actual AI model
    prompt = f"""
    Suggest 5 Christmas gifts based on:
    - Interests: {recipient_data.get('intereses', 'Not specified')}
    - Food preferences: {recipient_data.get('comida', 'Not specified')}
    - Music taste: {recipient_data.get('musica', 'Not specified')}
    """
    
    # Simulate API response
    recommendations = [
        {"gift": "Wireless Headphones", "reason": "Based on their music interests"},
        {"gift": "Cooking Class", "reason": "Given their food preferences"},
        {"gift": "Concert Tickets", "reason": "Matches their musical taste"},
        {"gift": "Hobby Kit", "reason": "Aligns with their interests"},
        {"gift": "Gift Card", "reason": "For flexibility in choice"}
    ]
    return recommendations

def recomendador_screen():
    load_css('style.css')
    image = load_image('logo 2.png')
    
    # Custom CSS
    st.markdown("""
        <style>
        .gift-card {
            background-color: #2d2d44;
            padding: 20px;
            border-radius: 10px;
            border: 2px solid #ff2a6d;
            margin: 10px 0;
        }
        .gift-title {
            color: #05d9e8;
            font-size: 20px;
            margin-bottom: 10px;
        }
        .gift-reason {
            color: #d1d7e0;
            font-style: italic;
        }
        .recipient-card {
            background-color: #1a1a2e;
            padding: 20px;
            border-radius: 10px;
            border: 2px solid #ffb703;
            margin: 20px 0;
            text-align: center;
        }
        </style>
    """, unsafe_allow_html=True)

    # Display logo
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center;">
            <img src="data:image/png;base64,{image}" width="150">
        </div>
        """,
        unsafe_allow_html=True
    )

    # Get current user's secret santa assignment
    current_user = users_collection.find_one({"username": st.session_state.username})
    if current_user and "secret_santa" in current_user:
        recipient = users_collection.find_one({"username": current_user["secret_santa"]})
        
        if recipient:
            # Display recipient info
            st.markdown(
                f"""
                <div class="recipient-card">
                    <h2>🎁 Tu amigo invisible es:</h2>
                    <h1 style="color: #ffb703;">{recipient.get('nombre', recipient['username'])}</h1>
                </div>
                """,
                unsafe_allow_html=True
            )

            # Get and display AI recommendations
            recommendations = get_ai_recommendations(recipient)
            
            st.markdown("<h2 style='text-align: center; color: #05d9e8;'>Recomendaciones de Regalo</h2>", unsafe_allow_html=True)
            
            for rec in recommendations:
                st.markdown(
                    f"""
                    <div class="gift-card">
                        <div class="gift-title">🎄 {rec['gift']}</div>
                        <div class="gift-reason">💡 {rec['reason']}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            # Additional recipient info
            with st.expander("Ver más información sobre tu amigo invisible"):
                st.write("Gustos e Intereses:")
                st.write(f"🍽️ Comidas Favoritas: {recipient.get('comida', 'No especificado')}")
                st.write(f"🎵 Música: {recipient.get('musica', 'No especificado')}")
                st.write(f"⭐ Intereses: {recipient.get('intereses', 'No especificado')}")
                st.write(f"⚠️ Alergias: {recipient.get('alergias', 'No especificado')}")

        else:
            st.error("No se pudo encontrar la información del amigo invisible")
    else:
        st.warning("Todavía no se ha realizado el sorteo del amigo invisible")
