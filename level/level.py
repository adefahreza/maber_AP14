import database.config as config
import database.user as user
import health.health as health
import play.category.arithmetic.soal as arithmetic_level
import play.category.riddle.level as riddle_level
import play.category.sequence.sequence as sequence_level
import reward.reward as reward
import ui_utils as ui


def progres_level(kategori):
    user_data = user.get_user(config.player_name)
    total_level = user_data[0]
    
    current_level = user_data[3] if kategori == "Teka Teki Gambar" else user_data[1] if kategori == "Aritmatika Dasar" else user_data[5]

    health.reset_life(kategori)
    nyawa = health.get_lives(kategori)

    print(f"\nKategori: {kategori}")
    print("Soal terdiri dari level 1-20. Jika jawaban salah, nyawa berkurang 1.")
    print("Dan jika nyawa habis, kamu harus mengulang dari level 1.")

    while True:
        print(f"Total nyawa: {nyawa}\n")
        if kategori == "Teka Teki Gambar":
            if current_level <= 20:
                level = riddle_level.generate_question(current_level + 1)
                jawaban = level
            else :
                print("🎉Selamat! Kamu telah menyelesaikan semua level di kategori teka-teki gambar.🎉\n")
        elif kategori == "Aritmatika Dasar":
            if current_level <= 20:
                level = arithmetic_level.show_question(current_level + 1)
                jawaban = level
        else:
            if current_level <= 20:
                level = sequence_level.show_question(current_level + 1)
                jawaban = level[0]
            else:
                print("🎉Selamat! Kamu telah menyelesaikan semua level di kategori deret angka.🎉\n")
                
        jawaban_user = input("\nJawaban Anda: ")

        if jawaban_user.strip() == str(jawaban):
            print("Benar! Next ke level berikutnya.\n")
            current_level += 1
            reward.proses_level(kategori, nyawa, current_level)
            if kategori == "Teka Teki Gambar":
                current_riddle_level = current_level
            elif kategori == "Aritmatika Dasar":
                current_arithmetic_level = current_level
            else :
                solusi = level[1]
                print(f"Solusi: {solusi}\n")
                current_sequence_level = current_level
            lanjut = input("Lanjut ke level berikutnya? (y/n): ")
            if lanjut.lower() != 'y':
                break
        else:
            repeat = health.lose_life(kategori)
            if repeat == True:
                current_level = 0
                reward.proses_level(kategori, current_level, current_level)
                