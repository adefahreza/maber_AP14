import json
import os

import bcrypt

import database.config as config
from database.getjson import JSON as JSON_PATH
from database.getjson import get_json
from ui_utils import error, success


def check_user(username, password):
    data = get_json()

    if username in data:
        stored_hashed = data[username].get("password")
        if stored_hashed and bcrypt.checkpw(password.encode('utf-8'), stored_hashed.encode('utf-8')):
            config.player_name = username
            config.current_level = data[username].get("total_level", 0)
            success("Login berhasil!")
            return True
        else:
            error("Password salah!")
            return False
    else:
        error("Pengguna tidak ditemukan!")
        return False

def create_user(username, password):
    data = get_json()

    if username not in data:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        data[username] = {
            "username": username,
            "password": hashed_password.decode('utf-8'),
            "total_level": 0,
            "current_riddle_level": 0,
            "current_riddle_lives": 0,
            "current_arithmetic_level": 0,
            "current_arithmetic_lives": 0,
            "current_sequence_level": 0,
            "current_sequence_lives": 0  ,
            "title": "Belum memiliki tingkatan"
        }
        with open(JSON_PATH, "w") as json_file:
            json.dump(data, json_file, indent=4)
        return True
    else:
        error("Pengguna sudah ada!")
        return False
        
def update_user(kategori=None, lives=None, level=None, title=None):
    data = get_json()
    username = config.player_name
    
    if username in data:
        user = data[username]
        
        if kategori == "Teka Teki Gambar" and level is not None and lives is not None:
            user["current_riddle_level"] = level
            user["current_riddle_lives"] = lives
        elif kategori == "Aritmatika Dasar" and level is not None and lives is not None:
            user["current_arithmetic_level"] = level
            user["current_arithmetic_lives"] = lives
        elif kategori == "Deret Angka" and level is not None and lives is not None:
            user["current_sequence_level"] = level
            user["current_sequence_lives"] = lives
        
        user["total_level"] = sum([
            user.get("current_riddle_level", 0),
            user.get("current_arithmetic_level", 0),
            user.get("current_sequence_level", 0)
        ])
        
        if title is not None:
            user["title"] = title
        
        with open(JSON_PATH, "w") as json_file:
            json.dump(data, json_file, indent=4)
    else:
        error("Pengguna tidak ditemukan!")
        return False

    
def logout():
    config.player_name = ""
    
def get_user(username):
    data = get_json()
    
    if username in data:
        user = data[username]
        total_level = user['total_level']
        current_riddle_level = user['current_riddle_level']
        current_riddle_lives = user['current_riddle_lives']
        current_sequence_level = user['current_sequence_level']
        current_sequence_lives = user['current_sequence_lives']
        current_arithmetic_level = user['current_arithmetic_level']
        current_arithmetic_lives = user['current_arithmetic_lives']
        title = user["title"]
            
        return (total_level, current_arithmetic_level, current_arithmetic_lives, current_riddle_level, current_riddle_lives, current_sequence_level, current_sequence_lives, title)
    else:
        return None