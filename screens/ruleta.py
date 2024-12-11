import streamlit as st
from utils.aux_functions import load_css, load_image
import random
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["christmas_companion"]
users_collection = db["users"]

def assign_secret_santa(family_group):
    users = list(users_collection.find({"family_group": family_group}))
    if not users:
        st.error("No users found in the family group.")
        return

    random.shuffle(users)
    assignments = {}
    for i in range(len(users)):
        santa = users[i]
        recipient = users[(i + 1) % len(users)]
        assignments[santa["username"]] = recipient["username"]

    for santa, recipient in assignments.items():
        users_collection.update_one(
            {"username": santa},
            {"$set": {"secret_santa": recipient}}
        )  

def check_secret_santa_assigned(family_group):
    users = list(users_collection.find({"family_group": family_group}))
    for user in users:
        if "secret_santa" not in user:
            return False
    return True


def ruleta_screen():
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
            <h2>Ruleta del amigo invisible</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    family_group = st.session_state.family_group

    if check_secret_santa_assigned(family_group):
        st.write("Amigo invisible ya asignado")
    else:
        if st.button("Asignar Amigo Invisible"):
            assign_secret_santa(family_group)
            st.success("Amigo invisible asignado")

        st.markdown(
            """
            <div style="text-align: center;">
                <h2>Ruleta del amigo invisible</h2>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div style="display: flex; justify-content: center;">
                <img src="https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif" width="150">
            </div>
            """,
            unsafe_allow_html=True
        )