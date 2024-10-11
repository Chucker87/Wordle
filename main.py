import random
yellow = '\033[93m'
green = '\033[92m'
clear = '\033[0m'
fail = '\033[91m'
cyan = '\033[96m'
i = 0
x = 0
u = 0

file_path = r'YOUR_PATH\wordlist.txt'
streak_path = r'YOUR_PATH\streak.txt'
highscore_path = r'YOUR_PATH\highscore.txt'

with open(streak_path, 'r') as file:
    streak = file.read().strip()
streak = int(streak)

def get_random_word(file_path):
    with open(file_path, 'r') as file:
        words = [word for line in file for word in line.split()]
    return random.choice(words)

while True:
    o = 6
    random_word = get_random_word(file_path)
    low = random_word.lower()
    #print(low) uncomment this to see the word 
    word = list(low)

    hint = []
    hints = False
    h = 0
    for x in range(5):
        o = o - 1
        while True:
            print(cyan+"Type ok for a hint (-1 try)."+clear)
            guess = input("(" + str(o) + ")" + "Guess the word: ").strip()
            if guess == 'ok' and hints == False:
                h = h + 1
                if h == 2:
                    hints = True
                while True:
                    random_choice = random.randint(0, 4)
                    if random_choice not in hint:
                        hint.append(random_choice)
                        break
                for u in range(5):
                    if u in hint:
                        print(cyan + word[u] + clear, end=" ")
                    else:
                        print("x", end=" ")
                x = x + 1
                guess=str()
                break
                
            if guess.isalpha():
                guess = guess.lower()
                if len(guess) == 5:
                    break
                else:
                    if guess == 'ok':
                        print("You can´t use more than 2 hints per word.")
                    else:
                        print("Error: Please enter a word with 5 letters.")
            else:
                print("Error: Invalid input. Please use letters only.")

        arr = list(guess)
        for x in range(len(arr)):
            found = False
            for i in range(len(word)):
                if arr[x] == word[i]:
                    found = True
                    if x == i:
                        print(green + arr[x] + clear, end=" ")
                    else:
                        if arr[x] == word[x]:
                            print(green + arr[x] + clear, end=" ")
                        else:
                            print(yellow + arr[x] + clear, end=" ")
                    break
            if not found:
                print(arr[x], end=" ")
        print(" ")

        if arr == word:
            print(green + "Correct! You've guessed the word!")
            streak = streak+1
            print("Your streak: "+str(streak) + clear)
            with open(streak_path, 'w') as file:
                file.write(str(streak))
            with open(streak_path, 'r') as file:
                currentscore = file.read().strip()
            with open(highscore_path, 'r') as file:
                highscore = file.read().strip()
                if currentscore>highscore:
                    with open(highscore_path, 'w') as file:
                        file.write(str(currentscore))
            break

    if arr != word:
        print(fail + "You Lost!")
        result = ''.join(word)
        print("The Word was: " + result)
        print("You lost your "+str(streak)+" Winning streak" + clear)
        streak = 0
        with open(streak_path, 'w') as file:
            file.write(str(streak))

    user = input("Do you want to continue? y/n:")
    if user == ('n'):
        print("Saving score...")
        with open(streak_path, 'w') as file:
            file.write(str(streak))
        break
    print(" ")
