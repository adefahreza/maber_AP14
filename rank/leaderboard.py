import os
import sys

from ui_utils import space, text_centered

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from database.getjson import get_json


def Show_LeaderBoard():
    text_centered("--- 🏆 Papan Peringkat 🏆 ---")
    space()
    datap_user = get_json()

    if not datap_user:
        text_centered("Belum ada data pemain.")
        text_centered("-" * 80)
        return
    
    list_user = list(datap_user.values())

    leaderboard_sorted = sorted(list_user, key=lambda user: user["total_level"], reverse=True)

    for index, user in enumerate(leaderboard_sorted, start=1):
        # 'start=1' membuat 'enumerate' memulai hitungan dari 1 (untuk peringkat)
        username = user.get("username", "N/A")
        level = user.get("total_level", 0)
        title = user.get("title", "-")
        
        print(f"#{index:<3} | {username:<15} | Total Level: {level:<5} | Title: {title}")
    
    print("-" * 80)
