import random

def generate_question_1():
    a = random.randint(1, 100)
    b = random.randint(1, 100)

    print(f"{a}+{b} = ")
    answer = a + b
    return answer

def generate_question_2():
    a = random.randint(1, 100)
    b = random.randint(1, 100)

    print(f"{a}-{b} = ")
    answer = a + b
    return answer

def generate_question_3():
    a = random.randint(1, 10)

    print(f"jika x = {a}, nilai dari 3x+1 = ")
    answer = 3*a + 1
    return answer

def generate_question_4():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1,10)

    print(f"({a}+{b}) x {c} = ")
    answer = (a+b)*c
    return answer