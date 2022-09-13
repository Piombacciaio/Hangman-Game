import colorama, ctypes, re, requests, os
from colorama import Fore
from string import ascii_lowercase

LIFES_DICT = {
    "1": 4,
    "2": 2,
    "3": 0,
    "4": -2
}
LANGS_DICT = {
    "0": "en",
    "1": "it",
    "2": "de",
    "3": "es",
    "4": "zh"
}
VOWELS = "aeiouy"
PATTERN = r'^[0-4]$'


def new_game(difficulty, lang):

    word = requests.get(f"https://random-word-api.herokuapp.com/word?lang={LANGS_DICT[lang]}").json()
    word = str(word[0])
    lifes = int(len(word) + LIFES_DICT[difficulty])
    known_letters = []
    guessed_letters = []

    return word, lifes, known_letters, guessed_letters


def main():

    while True:

        print(f"""Please choose one of the following options:\n[{Fore.GREEN}1{Fore.RESET}] - Easy\n[{Fore.GREEN}2{Fore.RESET}] - Medium\n[{Fore.GREEN}3{Fore.RESET}] - Hard\n[{Fore.GREEN}4{Fore.RESET}] - Master\n[{Fore.GREEN}0{Fore.RESET}] - Exit the program""")
        difficulty = input(">> ")

        if re.match(PATTERN, difficulty):

            if difficulty == "0":

                quit(1)

            print(f"Please choose one of the following languages:\n[{Fore.GREEN}0{Fore.RESET}] - English\n[{Fore.GREEN}1{Fore.RESET}] - Italian\n[{Fore.GREEN}2{Fore.RESET}] - German\n[{Fore.GREEN}3{Fore.RESET}] - Spanish\n[{Fore.GREEN}4{Fore.RESET}] - Chinese")
            language = input(">> ")

            if re.match(PATTERN, language):

                word, lifes, known_letters, guessed_letters = new_game(difficulty, language)

                while True:

                    guessed_phrase = ""
                    for char in word:

                        if char not in known_letters:

                            if char in VOWELS and difficulty == "1":

                                guessed_phrase += "+ "

                            else:

                                guessed_phrase += "- "

                        else:

                            guessed_phrase += f"{char} "

                    if "-" not in guessed_phrase:

                        print(f"\n{Fore.GREEN}YOU WON!{Fore.RESET}\nThe word is {word}")
                        break

                    if lifes < 0:

                        print(f"{Fore.RED}DEFEAT{Fore.RESET}, the word was: {word}")
                        break

                    print(f"\n{guessed_phrase}, lifes remaining: {str(lifes)}")

                    guess = input("Guess a character (a-z) >> ").lower()

                    if guess in ascii_lowercase:

                        if guess in word:

                            known_letters.append(guess)

                        if guess not in guessed_letters and guess not in word:

                            lifes -= 1

                        if guess not in guessed_letters:

                            guessed_letters.append(guess)

                        else:

                            print(f"{Fore.YELLOW}Letter already guessed{Fore.RESET}")

                    else:

                        print(f"{Fore.YELLOW}Character must be a letter (a-z){Fore.RESET}")

                print(f"{Fore.YELLOW}Press ENTER to start a new game...{Fore.RESET}", end="")
                input()
                os.system("cls")

            else:

                print(f"{Fore.RED}Inavlid choice. Press ENTER to continue...{Fore.RESET}", end="")
                input()
                os.system("cls")

        else:

            print(f"{Fore.RED}Inavlid choice. Press ENTER to continue...{Fore.RESET}", end="")
            input()
            os.system("cls")


if __name__ == "__main__":

    ctypes.windll.kernel32.SetConsoleTitleW(f'Hangman Game | made by piombacciaio')
    colorama.init()
    main()
