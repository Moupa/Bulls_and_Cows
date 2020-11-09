import random
import time
import datetime


def main():
    greeting()
    attempts = 0
    random_num = random_number()
    print(random_num)
    start_time = time.time()
    while True:
        player_num = player_number()
        attempts += 1
        bulls, cows = bulls_cows_counts(random_num, player_num)
        if bulls == 4:
            total_time = time.time() - start_time
            print(f"Congratulations!!You won in {attempts} attemps. That's {evaluation(attempts)} result. ")
            add_result('statistics.txt', attempts, total_time)
            show_statistics('statistics.txt')
            break
        else:
            continue


def greeting():
    print("""
    Hi there!
    Let's play a bulls and cows game.
    I've generated a random 4 digit number for you.
    Your goal is to guess this number.
    Enter a 4 digit number, made from unique digits.
    (digits do not repeat in the number)
    If you guess correct digit:
    - in the correct position, it's "Bulls"
    - in the different position, it's "Cows"
    Let's begin!""")


def random_number():
    num = list(range(0,10))
    number = random.sample(num, k=4)
    return number


def player_number():
    while True:
        num = input('Enter a number: ')
        if len(num) != 4 or not num.isdigit():
            print('Please enter 4 digit number!')
            continue
        elif len(set(num)) != 4:
            print('Please enter a number with 4 unique digits')
            continue
        else:
            break
    number = [int(i) for i in str(num)]
    return number


def bulls_cows_counts(random_n, player_n):
    bulls = cows = 0
    for i, num in enumerate(player_n):
        if num in random_n:
            if num == random_n[i]:
                bulls += 1
            else:
                cows += 1
    print(f"{bulls} bulls, {cows} cows")
    return bulls, cows


def add_result(file, attempts, total_time):
    g_date, g_time = day_time_form()
    with open(file, "a", newline="\n") as new_result:
        new_result.write("|{0:^12}|{1:^10}|{2:^11}|{3:^15}|{4:^14,.3f}|\n"
                         .format(g_date, g_time, attempts, evaluation(attempts), total_time))


def show_statistics(file):
    choice = str(input('Do you want to see statistics of your games? y / n : '))
    while True:
        if choice == "y":
            with open(file, "r") as read_stat:
                print(read_stat.read())
            break
        if choice == "n":
            print("Thank you for your game.")
            break
        else:
            print("Please enter 'y' for yes and 'n' for no.")
            continue


def evaluation(count_attempts):
    if count_attempts < 3:
        return 'amazing'
    elif count_attempts < 6:
        return 'good'
    return 'not very good'


def day_time_form():
    day_time = datetime.datetime.now()
    game_date = str(day_time.date())
    game_time = (day_time.time()).strftime('%H:%M:%S')
    return game_date, game_time


main()
