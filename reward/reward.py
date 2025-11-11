from database.config import player_name
from database.user import get_user, update_user

# comment 1. Panggil >> showing_rank << dengan variable nama_player dan point_player untuk menampilkan rank player di main menu atau laman lainnya

class Warna:
    RESET = '\033[0m'
    LEGENDARY = '\033[95m'  # Magenta Cerah
    MASTER = '\033[91m'     # Merah Cerah
    DIAMOND = '\033[96m'    # Cyan Cerah
    GOLD = '\033[93m'       # Kuning Cerah
    SILVER = '\033[37m'     # Putih
    BRONZE = '\033[33m'     # Oranye/Coklat muda

def cek_tingkat(total_level):
    if 10 <= total_level < 20:
        tingkat = "🥉Bronze"
        return Warna.BRONZE + "Bronze" + Warna.RESET
    elif 20 <= total_level < 30:
        tingkat = "🥈Silver"
        return Warna.SILVER + "Silver" + Warna.RESET
    elif 30 <= total_level < 40:
        tingkat = "🥇Gold"
        return Warna.GOLD + "Gold" + Warna.RESET
    elif 40 <= total_level < 50:
        tingkat = "💎Diamond"
        return Warna.DIAMOND + "Diamond" + Warna.RESET
    elif 50 <= total_level < 60:
        tingkat = "🧠Master"
        return Warna.MASTER + "Master" + Warna.RESET
    elif total_level == 60:
        tingkat = "🏆Legendary"
        return Warna.LEGENDARY + "Legendary" + Warna.RESET
    else:
        tingkat = "Belum memiliki tingkatan"
    
    return tingkat

def proses_level(kategori, nyawa, level_dikerjakan):
    user_data = get_user(player_name)
    total_level = user_data[0]
    tingkat = cek_tingkat(total_level)
    update_user(kategori, nyawa, level_dikerjakan, tingkat)
    
    print(f"Kategori: {kategori}, Level ke-{level_dikerjakan} selesai.")
    print(f"Total level yang sudah dikerjakan dari semua kategori soal: {total_level}")
    
    if total_level % 10 == 0 and total_level != 0:
        print(f"🎉 Selamat! Anda naik ke tingkat {tingkat}")
