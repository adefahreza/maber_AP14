import random
from fractions import Fraction

## Salwa
def soal_1():
    a = random.randint(1, 100)
    b = random.randint(1, 100)

    print(f"{a}+{b} = ")
    answer = a + b
    return answer

def soal_2():
    a = random.randint(1, 100)
    b = random.randint(1, 100)

    print(f"{a}-{b} = ")
    answer = a - b
    return answer

def soal_3():
    a = random.randint(1, 10)

    print(f"jika x = {a}, nilai dari 3x+1 = ")
    answer = 3*a + 1
    return answer

def soal_4():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1,10)

    print(f"({a}+{b}) x {c} = ")
    answer = (a+b)*c
    return answer

## Ade
def soal_5():
    #pola soal : (a - b) x (c + d)

    a = random.randint(1, 20)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    d = random.randint(1, 10)

    soal = f"({a} - {b}) x ({c} + {d}) = ..."
    jawaban = int((a - b) * (c + d))

    print (soal)
    return jawaban

def soal_6():
    #pola soal : (a + b) x c(d + e)

    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(2, 5)  # Menghindari perkalian dengan 0 atau 1
    d = random.randint(1, 10)
    e = random.randint(1, 10)
    
    soal = f"({a} + {b}) x {c}({d} + {e}) = ..."
    jawaban = (a + b) * c * (d + e)

    print (soal)
    return jawaban

def soal_7():
    #pola soal : x^2 - y^2

    # 'x' lebih besar dari 'y' supaya hasilnya positif
    x = random.randint(2, 12) 
    y = random.randint(1, x - 1) 
    
    soal = f"Jika x={x} dan y={y}, nilai dari (x² - y²) adalah ..."
    jawaban = (x**2) - (y**2)

    print (soal)
    return jawaban

def soal_8():
    #pola soal : a / b * c
    a = random.randint(10, 100)
    b = random.randint(1, 10)  # Menghindari pembagian dengan 0
    c = random.randint(1, 10)

    soal = f"{a} / {b} * {c} = ..."
    jawaban = (a / b) * c

    print (soal)
    return jawaban

## Aqila
def soal_9():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    d = random.randint(1, 10)
    
    while c - d == 0:
        c = random.randint(1, 10)
        d = random.randint(1, 10)
    
    print(f"Selesaikan soal berikut: ({a}+{b})/({c}-{d})")
    answer = (a + b) / (c - d)
    return answer

def soal_10():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)

    print(f"Jika a={a}, b={b}, c={c}, tentukan nilai dari a² + b x c!")
    answer = a**2 + b*c
    return answer

def soal_11():
    a = random.randint(2, 10)
    b = random.randint(1, a - 1)

    while a - b == 0:
        b = random.randint(1, a - 1)

    print(f"Selesaikan soal berikut: ({a}² - {b}²)/({a} - {b})")
    answer = (a**2 - b**2) / (a - b) 
    return answer

def soal_12():
    a = random.randint(1, 5)   
    b = random.randint(1, 5)  
    while a == b:             
        b = random.randint(1, 5)

    c = random.randint(1, 10) 
    d = random.randint(1, 10)  

    print(f"Selesaikan persamaan berikut: {a}x + {c} = {b}x - {d}")
    answer = (c + d) / (b - a)
    return answer

## Aura
def soal_13():
    a = random.randint(5, 25)
    b = random.randint(5, 25)
    c = random.randint(5, 25)
    
    print(f"\nBerapa hasil dari ({a}+{b})x{c}^2 = ")
    answer = (a+b) * (c**2)
    return answer

def soal_14():
    a = random.randint(5, 25)
    b = random.randint(5, 25)
    c = random.randint(5, 25)
    d = random.randint(5, 25)
    
    print(f"\nBerapa hasil dari ({a}+{b})x({c}-{d}) = ")
    answer = (a-b) * (c-d)
    return answer

def soal_15():
    a = random.randint(5, 30)
    b = random.randint(5, 30)
    c = random.randint(5, 30)
  
    print(f"({a}+{b})^2 + {c}^2 = ")
    answer = (a+b)**2 + (c**2)
    return answer

def soal_16():
    a = random.randint(5, 30)
    b = random.randint(5, 30)
    c = random.randint(5, 30)
    hasil = a + b * c
    pembagi = [i for i in range(2, 30) if hasil % i == 0]
    if not pembagi:
        return soal_16()
    d = random.choice(pembagi)
    answer = hasil // d
    print(f"\nBerapa hasil dari ({a}+{b}x{c})/{d} ?")
    return answer

## Rendy
def level_17():
    total_mhs = random.randint(10, 25) * 6
    ikut_esport = total_mhs // 2
    ikut_psm = total_mhs // 3
    ikut_keduanya = random.randint(1, min(ikut_esport, ikut_psm) // 3)

    answer = ikut_esport + ikut_psm - ikut_keduanya
    print(f"17. Kelas Sintara memiliki {total_mhs} mahasiswa. Setengahnya ikut UKM E-Sport,\n"
          f"    sepertiganya ikut UKM PSM, dan {ikut_keduanya} orang ikut keduanya.\n"
          f"    Berapa total mahasiswa yang ikut paling sedikit salah satu UKM?")
    return answer

def level_18():
    harga_buku_asli = random.randint(3, 8) * 1000
    harga_pensil_asli = random.randint(2, 6) * 500
    jml_buku = random.randint(2, 5)
    jml_pensil = random.randint(2, 6)
    total_harga = (jml_buku * harga_buku_asli) + (jml_pensil * harga_pensil_asli)
    total_str = f"{total_harga:,}".replace(",", ".")
    buku_str = f"{harga_buku_asli:,}".replace(",", ".")

    answer = (total_harga - (jml_buku * harga_buku_asli)) / jml_pensil
    answer = f"{int(answer):,}".replace(",", ".")
    print(f"18. Sebuah toko menjual {jml_buku} buku tulis dan {jml_pensil} pensil dengan harga total Rp{total_str}.\n"
          f"    Jika harga sebuah buku tulis Rp{buku_str}, berapakah harga satu pensil?")
    return answer

def level_19():
    x = random.randint(3, 9)
    a = random.randint(2, 4)
    b = random.randint(1, 9)
    op_str = random.choice(["+", "-"])
    
    if op_str == "+":
        y = (a * x) + b
    else:
        y = (a * x) - b

    answer = (x + y) * (x - y)
    print(f"19. Jika x={x} dan y={a}x {op_str} {b}, hitung nilai dari (x+y) * (x-y).")
    return answer

def level_20():
    wa = random.choice([8, 12, 24])
    wb = random.choice([6, 8, 12])
    w_buka = random.randint(2, 4)

    laju_a = Fraction(1, wa)
    laju_b = Fraction(1, wb)
    laju_gabungan = laju_a + laju_b

    answer = laju_gabungan * w_buka
    print(f"20. Tangki air terisi penuh dalam {wa} jam oleh kran A, dan {wb} jam oleh kran B.\n"
          f"    Jika dibuka bersama selama {w_buka} jam, berapa bagian tangki yang terisi?")
    return answer