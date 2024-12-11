import streamlit as st
from utils.aux_functions import load_css, load_image
from pymongo import MongoClient
import random

client = MongoClient("mongodb://localhost:27017/")
db = client["christmas_companion"]
users_collection = db["users"]

def assign_table_seats(family_group, chairs_per_side):
    users = list(users_collection.find({"family_group": family_group}))
    if not users:
        st.error("No users found in the family group.")
        return
    
    total_seats = chairs_per_side * 2
    if len(users) > total_seats:
        st.error(f"Too many users ({len(users)}) for available seats ({total_seats})")
        return
    
    random.shuffle(users)
    side1 = users[:chairs_per_side]
    side2 = users[chairs_per_side:chairs_per_side*2]
    
    return side1, side2

def mesa_screen():
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
        <style>
        .table-container {
            margin: 20px auto;
            max-width: 800px;
        }
        .table-row {
            display: flex;
            justify-content: center;
            margin: 10px 0;
        }
        .seat {
            background-color: #2d2d44;
            color: #d1d7e0;
            border: 2px solid #ff2a6d;
            padding: 10px 20px;
            margin: 0 5px;
            border-radius: 8px;
            min-width: 120px;
            text-align: center;
        }
        .table-center {
            height: 20px;
            background-color: #05d9e8;
            margin: 10px 0;
            border-radius: 4px;
        }
        </style>
        """, 
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="text-align: center;">
            <h2>Asignación de Mesa</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    chairs_per_side = st.number_input(
        "Número de sillas por lado", 
        min_value=1, 
        max_value=10, 
        value=4
    )

    if st.button("Asignar espacios en mesa"):
        side1, side2 = assign_table_seats(st.session_state.family_group, chairs_per_side)
        
        st.markdown('<div class="table-container">', unsafe_allow_html=True)
        
        # Row 1
        st.markdown('<div class="table-row">', unsafe_allow_html=True)
        for user in side1:
            st.markdown(
                f'<div class="seat">{user.get("username", "Vacío")}</div>',
                unsafe_allow_html=True
            )
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Table center
        st.markdown('<div class="table-center"></div>', unsafe_allow_html=True)
        
        # Row 2
        st.markdown('<div class="table-row">', unsafe_allow_html=True)
        for user in side2:
            st.markdown(
                f'<div class="seat">{user.get("username", "Vacío")}</div>',
                unsafe_allow_html=True
            )
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)