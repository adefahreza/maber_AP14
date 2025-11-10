from database.user import update_user
from database.config import player_name

def cek_tingkat(total_level):
    if 10 <= total_level < 20:
        tingkat = "Bronze"
    elif 20 <= total_level < 30:
        tingkat = "Silver"
    elif 30 <= total_level < 40:
        tingkat = "Gold"
    elif 40 <= total_level < 50:
        tingkat = "Diamond"
    elif 50 <= total_level < 60:
        tingkat = "Master"
    elif total_level == 60:
        tingkat = "Legendary"
    else:
        tingkat = "Belum memiliki tingkatan"
    
    
    return tingkat

def proses_level(kategori, level_dikerjakan, total_level):
    print(f"Kategori: {kategori}, Level ke-{level_dikerjakan} selesai.")
    print(f"Total level yang sudah dikerjakan: {total_level}")
    
    tingkat = cek_tingkat(total_level)
    update_user(player_name, level=total_level, title=tingkat)
    
    if total_level % 10 == 0:
        print(f"🎉 Selamat! Anda naik ke {tingkat}")
    elif 0 <= total_level >= 9:
        print(f"Anda belum memiliki tingkatan")
    else:
        print(f"Anda berada di tingkat {tingkat}.")