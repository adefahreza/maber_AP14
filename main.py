from login.login import login_screen
from ui_utils import banner
from utils import main_menu


def main():
    isLoggedIn = login_screen()
    if isLoggedIn == True:
        banner()
        main_menu()

if __name__ == "__main__":
    main()