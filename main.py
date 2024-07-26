import pygame
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("My Game")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))
        pygame.display.flip()

if __name__ == "__main__":
    main()

import os
from decouple import Config, RepositoryEnv
from logic import GuessTheNumberGame


config = Config(RepositoryEnv(os.path.join(os.path.dirname(__file__), 'settings.ini')))
range_start = config('range_start', cast=int)
range_end = config('range_end', cast=int)
attempts = config('attempts', cast=int)
initial_capital = config('initial_capital', cast=int)


game = GuessTheNumberGame(range_start, range_end, attempts, initial_capital)

print(f"Добро пожаловать в игру 'Угадай число'!")
print(f"У вас есть {attempts} попыток и {initial_capital} начального капитала.")
print(f"Диапазон чисел: от {range_start} до {range_end}.")


while not game.is_game_over():
    try:
        guess = int(input(f"Введите ваше число: "))
        bet = int(input(f"Введите вашу ставку: "))

        if bet > game.capital:
            print(f"Ваша ставка превышает ваш текущий капитал: {game.capital}")
            continue

        correct, capital = game.make_guess(guess, bet)
        if correct:
            print(f"Поздравляем! Вы угадали число и ваш капитал удвоен: {capital}")
            break
        else:
            print(f"Неправильно! Осталось попыток: {game.attempts - 1}, текущий капитал: {capital}")

        game.attempts -= 1

    except ValueError:
        print("Введите корректное число и ставку.")

if game.is_game_over():
    print(f"Игра окончена! Ваш окончательный капитал: {game.capital}")
else:
    print(f"Вы выиграли! Ваш окончательный капитал: {game.capital}")
