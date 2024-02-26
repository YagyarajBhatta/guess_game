print("Welcome to the Game 🔮")
score=0
L=0
words=['Hi','hii','no','nn']
def func(level):
    global L, word
    L += 1
    word = words[level]
while L < len(words):
    func(L)
    attempts = 3
    while True:
        while attempts > 0:
            guess = input("Guess the word: ").lower()

            if guess == word.lower():
                print()
                print("Congratulations!💥 You won.")
                score+=50
                print(f"Your score is {score}")
                print(f"You passed Level {L}")

                break
            elif guess == "hint":
                print(f" 💡The first letter of the word is: {word[0]}")
            else:
                attempts -= 1
                if attempts == 0:
                    print("Game Over. You're out of attempts.")
                else:
                    print(f"🤏Incorrect guess. Attempts remaining: {attempts}")
                

        restart = input("Do you want to play again? (yes/no): ").lower()
        if restart != "yes":
            print("Thank you for playing!🤌🏽")
            break
        else:
            attempts = 3
            func(L)