from database.user import logout
from login import login
from ui_utils import error, goodbye_banner, info, line, space, text_left


def main_menu():
    while True:
        line()
        space()
        text_left("Menu Utama:")
        text_left("1. Mulai Permainan ⚔️")
        text_left("2. Lihat Peringkat 🏆")
        text_left("3. Ganti Akun 🔄️")
        text_left("4. Keluar Aplikasi 🚪")
        space()
        choice = input("Pilih opsi (1-4): ")
        line()
        if choice == "1":
            from play.menu import chooseCategory
            chooseCategory()
        elif choice == "2":
            # Leaderboard
            from rank.leaderboard import Show_LeaderBoard
            Show_LeaderBoard()
        elif choice == "3":
            logout()
            while True:
                result = login.login_user()
                if result == True:
                    info("Akun telah berhasil diganti")
                    break
                else:
                    continue
        elif choice == "4":
            goodbye_banner()
            break
            