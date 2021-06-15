import random
import hangman_words
from hangman_art import stages, logo
from replit import clear


print(logo)
word_list = hangman_words.word_list
correct_word = random.choice(word_list)
display = []


lives = 6

for x in range(len(correct_word)):  # used "_" because it is not needed in this for expression
    display += "_"
print(display)
end_of_game = True

while end_of_game:
    user_word = input("Guess a letter : ")
    user_word = user_word.lower()
    clear()

    if user_word in display:
        print(f"You have already guessed the letter {user_word}...try something new")

    for position in range(len(correct_word)):  # Range starts from zero to 1 less than the given number
        letter = correct_word[position]
        if letter == user_word:
            display[position] = letter
    print(display)

    if user_word not in correct_word:
        lives= lives-1
        lives_left = ['0','1','2','3','4','5']
        print("Incorrect letter choice, you loose a life")
        print(f"Your choice {user_word} is not in the word, try another letter")
        print(stages[lives])
        print(f"Number of lives left : {lives_left[lives]}")
        print(f"Current scenario {display}")
        if lives == 0:
            end_of_game = False
            print("You loose....try again???")
            print(f"The correct word was => {correct_word}")

    if '_' not in display:
        end_of_game = False
        print("Well Done....You Win!!!")
