import random
import time
import sys

class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    RESET = "\033[0m"

class GuessNumberGame:
    def __init__(self, low=1, high=100):
        self.low = low
        self.high = high
        self.number = random.randint(low, high)
        self.attempts = 0
        self.start_time = None

    def start(self):
        print(Colors.BLUE + "Добро пожаловать в игру 'Угадай число'!" + Colors.RESET)
        print(f"Я загадал число от {self.low} до {self.high}. Попробуй угадать!\n")
        self.start_time = time.time()

        while True:
            guess = self.get_guess()
            self.attempts += 1

            if guess < self.number:
                print(Colors.YELLOW + "Больше!" + Colors.RESET)
            elif guess > self.number:
                print(Colors.YELLOW + "Меньше!" + Colors.RESET)
            else:
                self.win()
                break

    def get_guess(self):
        while True:
            try:
                value = int(input("Твоё предположение: "))
                if value < self.low or value > self.high:
                    print(Colors.RED + "Число вне диапазона!" + Colors.RESET)
                    continue
                return value
            except ValueError:
                print(Colors.RED + "Введите число!" + Colors.RESET)

    def win(self):
        elapsed = time.time() - self.start_time
        print(Colors.GREEN + f"\nПоздравляю! Ты угадал число {self.number}!" + Colors.RESET)
        print(f"Попыток: {self.attempts}")
        print(f"Время игры: {elapsed:.2f} секунд")

def main():
    while True:
        game = GuessNumberGame(1, 50)
        game.start()

        again = input("\nСыграть ещё раз? (y/n): ").strip().lower()
        if again != "y":
            print(Colors.BLUE + "Спасибо за игру! Пока!" + Colors.RESET)
            sys.exit()

if __name__ == "__main__":
    main()



print("It is 1st duplicate")
print("It is duplicate 2")
print("It is duplicate 3")
print("It is duplicate 4")
print("It is duplicate 5")
