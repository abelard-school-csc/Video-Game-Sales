import os
import time
import random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def level_one():
    paddle = 5
    ball_pos = 5
    ball_dir = 1
    for _ in range(20):
        clear()
        print("|" + " " * paddle + "-" + " " * (10 - paddle) + "|")
        print("|" + " " * ball_pos + "o" + " " * (10 - ball_pos) + "|")
        ball_pos += ball_dir
        if ball_pos == 0 or ball_pos == 10:
            ball_dir *= -1
        time.sleep(0.2)

def level_two():
    pacman = 0
    ghosts = [random.randint(5, 10) for _ in range(3)]
    for _ in range(20):
        clear()
        row = [" "] * 11
        row[pacman] = "C"
        for ghost in ghosts:
            row[ghost] = "G"
        print("|" + "".join(row) + "|")
        pacman = (pacman + 1) % 11
        ghosts = [(ghost - 1 if ghost > 0 else 10) for ghost in ghosts]
        time.sleep(0.2)

def level_three():
    track = [" "] * 20
    player_pos = 10
    for _ in range(20):
        clear()
        row = [" "] * 21
        row[player_pos] = "A"
        print("|" + "".join(row) + "|")
        obstacles = [random.randint(0, 20) for _ in range(5)]
        for obstacle in obstacles:
            row[obstacle] = "X"
        time.sleep(0.2)
        if player_pos in obstacles:
            break

def trivia():
    questions = [
        ("What year was Tennis for Two created?", "1958"),
        ("What company saved the gaming industry in 1985?", "Nintendo"),
        ("Which genre leads global sales?", "Action")
    ]
    for question, answer in questions:
        clear()
        print(question)
        user_input = input("Your answer: ")
        if user_input.lower() != answer.lower():
            return False
    return True

def game():
    clear()
    print("Welcome to the Timeline of Gaming!")
    time.sleep(2)
    level_one()
    level_two()
    level_three()
    if trivia():
        print("Congratulations, you completed the game!")
    else:
        print("Game Over. Try Again!")

game()
