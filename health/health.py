import database.config as config
import database.user as user
import ui_utils as ui

data_user = user.get_user(config.player_name)

level_and_lives = {
    "Teka Teki Gambar": {
        "level": data_user[3],  
        "lives": data_user[4]   
    },
    "Aritmatika Dasar": {
        "level": data_user[1],  
        "lives": data_user[2]   
    },
    "Deret Angka": {
        "level": data_user[5],  
        "lives": data_user[6] 
    }
}

def reset_life(kategori):
    if kategori in level_and_lives:
        level_and_lives[kategori]["lives"] = 5  
        
        user.update_user(kategori, level_and_lives[kategori]["lives"], 
                         level_and_lives[kategori]["level"])

def lose_life(kategori):
    isLose = False

    if kategori in level_and_lives:
        level_and_lives[kategori]["lives"] -= 1
        ui.error(f"Nyawa berkurang! Sisa nyawa: {level_and_lives[kategori]['lives']}")
        
        if level_and_lives[kategori]["lives"] <= 0:
            print("Game Over! ☠")
            ui.info("Nyawa habis, ulangi dari level 1.")
            isLose = True
            reset_life(kategori)
            
        user.update_user(kategori, level_and_lives[kategori]["lives"], 
                         level_and_lives[kategori]["level"])

    return isLose

def get_lives(kategori):
    if kategori in level_and_lives:
        return level_and_lives[kategori]["lives"]
    return 0
