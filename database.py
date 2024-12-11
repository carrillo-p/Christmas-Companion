from pymongo import MongoClient
from datetime import datetime
import streamlit as st

class ChristmasDatabase:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['Christmas']
        self.wish = self.db['wish']

    # Métodos de usuarios usando la colección wish
    def create_user(self, user_data):
        user_data['created_at'] = datetime.now()
        return self.wish.insert_one(user_data)

    def get_user(self, username):
        return self.wish.find_one({"username": username})

    def validate_login(self, username):
        return self.wish.find_one({"username": username})

    def update_user(self, username, new_data):
        return self.wish.update_one(
            {"username": username},
            {"$set": new_data}
        )

    def get_family_tables(self, family_group):
        return list(self.wish.find({"family_group": family_group, "type": "table"}))

    def update_table(self, table_id, new_data):
        return self.wish.update_one(
            {"_id": table_id, "type": "table"},
            {"$set": new_data}
        )

    def add_recipe(self, recipe_data):
        recipe_data['created_at'] = datetime.now()
        recipe_data['type'] = "recipe"
        return self.wish.insert_one(recipe_data)

    def get_recipes(self, family_group=None):
        if family_group:
            return list(self.wish.find({"family_group": family_group, "type": "recipe"}))
        return list(self.wish.find({"type": "recipe"}))

    def create_playlist(self, playlist_data):
        playlist_data['created_at'] = datetime.now()
        playlist_data['type'] = "playlist"
        return self.wish.insert_one(playlist_data)

    def get_family_playlists(self, family_group):
        return list(self.wish.find({"family_group": family_group, "type": "playlist"}))

    def create_card(self, card_data):
        card_data['created_at'] = datetime.now()
        card_data['type'] = "card"
        return self.wish.insert_one(card_data)

    def get_family_cards(self, family_group):
        return list(self.wish.find({"family_group": family_group, "type": "card"}))

    def save_roulette_result(self, result_data):
        result_data['created_at'] = datetime.now()
        result_data['type'] = "roulette"
        return self.wish.insert_one(result_data)

    def get_roulette_history(self, family_group):
        return list(self.wish.find({"family_group": family_group, "type": "roulette"}))

    def close(self):
        self.client.close()