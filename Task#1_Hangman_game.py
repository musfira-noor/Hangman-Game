import random
from collections import Counter 

available_words = "apple banana mango pineapple grape cherry papaya melon watermelon orange peach pear apricot lychee "
words = available_words.split(" ")

word=random.choice(words) #ramdomly choose the secret word from available_words
if __name__ =='__main__':
    print("Guess the word!\nHINT: The word is a name of fruit.")
    for i in word:
        print("_",end="") #for printing the empty spaces for letters of the words, empty spaces == no of letters in a word 
        print()

    play=True
    letterGuessed=''
    chances=len(word)+3
    correct=0
    flag=0
    try:
        while(chances!=0) and flag==0:
            print("\nYou have",chances,"chances left")
            chances -= 1
            try:
                guess = str(input("Guess a letter: ").lower())
            except:
                print("Enter only a letter!")
                continue

#Validity of the guessed word:
            if not guess.isalpha():
                print("Enter only a letter---")
                continue
            elif len(guess)!=1:
                print('Enter only single letter please---')
                continue
            elif guess in letterGuessed:
                print('You already guessed this letter, try another one---')
                continue

#if letter is guessed correctly        
            if guess in word:
#here k will store the no of times the guessed letter in word
                 k = word.count(guess)
                 for _ in range(k):
                    letterGuessed += guess #the guesseed letter is added as many times as it occurs in word

            for char in word: #print the word 
                if char in letterGuessed and (Counter(letterGuessed)) != Counter(word):
                    print(char , end='') 
                    correct += 1  
                elif Counter(letterGuessed) == Counter(word):
                    print(f"You guessed the word {word} correctly!!")
                    flag = 1
                    print("Congradulatiion, You Won!")
                    break #break out of for loop
                else:
                    print("_", end='')

        if chances <= 0 and Counter(letterGuessed) != Counter(word):
            print("Game is Over, You lost!")
            print("The word was{}".format(word))
    except KeyboardInterrupt:
        print("\nGame is Over, You lost!")
        print("Bye Bye!, try Again---")
        exit()
