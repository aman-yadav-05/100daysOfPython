import random
import hangman_art
import hangman_words


print(hangman_art.logo)
word_list=hangman_words.word_list
lives=6

chosen_word=random.choice(word_list)
word_length=len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')
display=[]

#blank space for display list
for i in range(0,word_length):
    display.append("_")

end_of_game=False
while not end_of_game:

    guess=input("guess a letter: ").lower()
    # print(guess)

    if guess in display:
        print("You've already guessed this letter.")
    #check for the guess word in chosen_word
    for i in range(0,word_length):
        if(guess==chosen_word[i]):
            display[i]=guess

    #if guesed word not in chosen_word reduce life by 1
    if guess not in chosen_word:
        print("The letter you entered is not in word.You lose a life!")
        lives -=1
        if lives == 0:
           end_of_game=True
           print("You lose.")

    #pring hangman status
    print(hangman_art.stages[lives])
    print(display)

    #if all the spaces are identified then you win.
    if "_" not in display:
        end_of_game=True
        print("you win")