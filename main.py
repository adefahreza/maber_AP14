from login import login_screen
from utils import banner, header, line, main_menu, space


def main():
    isLoggedIn = login_screen()
    if isLoggedIn == True:
        banner()
        main_menu()

if __name__ == "__main__":
    main()