WIDTH = 60
from pyfiglet import Figlet


def line():
    print("=" * WIDTH)
    
def space():
    print("\n")

def header(title: str):
    line()
    print(title.center(WIDTH).capitalize())
    line()
    
def text_centered(text):
    print(text.center(WIDTH))

def text_left(text):
    print(text)
    
def main_menu():
    line()
    text_left("Menu Utama:")
    text_left("1. Mari Berhitung")
    text_left("2. Lihat Peringkat")
    text_left("3. Lihat Profil")
    text_left("4. Keluar Aplikasi")    
    line()
    
    choice = input("Pilih opsi (1-4): ")
    
def banner():
    banner = Figlet(font='small', justify='left')
    line()
    print(banner.renderText("MABER AP14"))
    line()
