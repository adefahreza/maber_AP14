
player_lives = 5

def lose_life():
    global player_lives
    if player_lives > 0:
        player_lives -= 1
        print(f"Nyawa berkurang! Sisa nyawa: {player_lives}")
    else:
        print("Game Over!")

def lose():
    print(f"Mulai game dengan {player_lives} nyawa.")
    lose_life()