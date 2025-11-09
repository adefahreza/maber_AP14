def tutorial_hitung_campuran():
    print("=" * 80)
    print("  TUTORIAL: Aritmatika Dasar")
    print("=" * 80)
    print("\nDalam operasi hitung campuran, urutan pengerjaan sangat penting.")
    print("Aturan yang harus diikuti adalah 'KuKaBaTaKu':")
    print("\n1. KURUNG ()")
    print("   - Kerjakan semua operasi di dalam tanda kurung terlebih dahulu.")
    print("   - Contoh: 10 + (5 - 2) -> Kerjakan (5 - 2) dulu jadi 3.")
    
    print("\n2. KALI (x) dan BAGI (:)")
    print("   - Setelah kurung, kerjakan perkalian dan pembagian.")
    print("   - Keduanya sama kuat, kerjakan dari yang paling kiri.")
    print("   - Contoh: 10 + 4 x 2 -> Kerjakan 4 x 2 dulu jadi 8.")
    print("   - Contoh: 12 : 2 x 3 -> Kerjakan 12 : 2 dulu jadi 6, baru 6 x 3 = 18.")

    print("\n3. TAMBAH (+) dan KURANG (-)")
    print("   - Terakhir, kerjakan pertambahan dan pengurangan.")
    print("   - Keduanya sama kuat, kerjakan dari yang paling kiri.")
    
    print("\n--- CONTOH LENGKAP ---")
    print("Soal: 5 + ( 10 - 2 ) x 3 : 4 - 1")
    print("1. Kurung: 5 + (8) x 3 : 4 - 1")
    print("2. Kali/Bagi (dari kiri):")
    print("   - Kali: 5 + 24 : 4 - 1")
    print("   - Bagi: 5 + 6 - 1")
    print("3. Tambah/Kurang (dari kiri):")
    print("   - Tambah: 11 - 1")
    print("   - Kurang: 10")
    print("\nHasil Akhir: 10")
    print("\n========================================")

def tutorial_tekateki_gambar():
    print("=" * 80)
    print("   TUTORIAL: Teka-Teki Gambar dan Operasi")
    print("=" * 80)
    print("\nJenis soal ini menantang Anda untuk menemukan nilai setiap bentuk")
    print("berdasarkan pola operasi matematika yang diberikan ( + , - , × , ÷ ).")
    print("Setiap bentuk (misalnya ◼, ▲, ●, ◆, ○) mewakili nilai angka tertentu.")
    
    print("\nCara Mengerjakan:")
    print("1. Perhatikan Bentuk dan Operasi")
    print("   - Tiap soal menggunakan simbol-simbol acak seperti ◼, ▲, ●, ◆, ○.")
    print("   - Setiap simbol punya nilai berbeda.")
    print("   - Soal ditulis seperti:  ◼ + ▲ = ?  atau  ● × ◼ ÷ ▲ = ?")

    print("\n2. Gunakan Petunjuk (Hint) untuk Menemukan Nilai Simbol")
    print("   - Tiap hint menunjukkan hubungan antar bentuk dengan hasil hitungan.")
    print("   - Contoh hint:  ◼ + ◼ + ◼ = 9  → berarti nilai ◼ = 3.")
    print("   - Gunakan semua hint yang tersedia untuk menentukan nilai setiap bentuk.")

    print("\n3. Substitusi Nilai ke Dalam Soal Utama")
    print("   - Setelah tahu nilai tiap bentuk, gantikan simbol pada soal.")
    print("   - Lakukan operasi matematika sesuai urutan (ingat urutan operasi: ×/÷ lebih dulu).")

    print("\n4. Hasilkan Jawaban Akhir")
    print("   - Hitung hasil akhir setelah semua simbol diganti nilainya.")
    print("   - Beberapa soal mungkin melibatkan operasi campuran ( + , - , × , ÷ ).")

    print("\n--- CONTOH ---")
    print("Soal:   ◼ + ▲ = ?")
    print("Petunjuk:")
    print("  ◼ + ◼ + ◼ = 9")
    print("  ▲ + ▲ + ▲ = 6")
    print("Analisis:")
    print("  Dari hint pertama → ◼ = 3")
    print("  Dari hint kedua   → ▲ = 2")
    print("Substitusi ke soal utama → 3 + 2 = 5")
    print("Jawaban: 5")

    print("\n--- CATATAN TAMBAHAN ---")
    print("• Pada level lebih tinggi, operasi bisa lebih rumit (campuran +, -, ×, ÷).")
    print("• Beberapa hint menunjukkan pola kombinasi, bukan nilai langsung.")
    print("• Fokuslah pada hubungan antar bentuk, bukan pada angka di hint saja.")
    print("• Gunakan logika dan perhatikan urutan operasi.")

    print("\nSelamat berpikir dan temukan pola tersembunyi di balik simbol-simbol tersebut!")
    print("=" * 80)
    
    continuePlay = input("Ingin memulai permainan Teka-Teki Gambar? (y): ")
    if continuePlay.lower() == 'y':
        return True
    else:
        return False


def tutorial_barisan_deret():
    print("=" * 80)
    print("    TUTORIAL: Matematika Barisan & Deret")
    print("=" * 80)
    print("\nBarisan adalah urutan bilangan dengan pola tertentu.")
    print("Deret adalah jumlah dari suku-suku barisan tersebut.")

    print("\n--- 1. BARISAN ARITMETIKA ---")
    print("Pola: Beda (selisih) antar suku selalu SAMA (konstan).")
    print("Contoh: 4, 7, 10, 13, ... (Bedanya selalu +3)")
    print(" - Suku pertama (a) = 4")
    print(" - Beda (b) = 3")
    print("\nRumus Suku ke-n (Un):")
    print("   Un = a + (n - 1) * b")
    print("   Contoh: Suku ke-10 (U10) = 4 + (10 - 1) * 3 = 4 + 9 * 3 = 4 + 27 = 31")
    
    print("\nRumus Jumlah n Suku (Sn) / Deret Aritmetika:")
    print("   Sn = n/2 * (a + Un)   ATAU   Sn = n/2 * (2a + (n - 1) * b)")
    print("   Contoh: Jumlah 10 suku pertama (S10) = 10/2 * (4 + 31) = 5 * 35 = 175")

    print("\n--- 2. BARISAN GEOMETRI ---")
    print("Pola: Rasio (perbandingan) antar suku selalu SAMA (konstan).")
    print("Contoh: 2, 6, 18, 54, ... (Rasionya selalu x3)")
    print(" - Suku pertama (a) = 2")
    print(" - Rasio (r) = 3")
    
    print("\nRumus Suku ke-n (Un):")
    print("   Un = a * r^(n-1)   (r pangkat n-1)")
    print("   Contoh: Suku ke-5 (U5) = 2 * 3^(5-1) = 2 * 3^4 = 2 * 81 = 162")

    print("\nRumus Jumlah n Suku (Sn) / Deret Geometri:")
    print("   Sn = a * (r^n - 1) / (r - 1)   (jika r > 1)")
    print("   Contoh: Jumlah 5 suku (S5) = 2 * (3^5 - 1) / (3 - 1) = 2 * (243 - 1) / 2 = 242")
    print("\n========================================")-13