import random
words = ["chicken", "individual", "laptop", "office", "telephone"]

def get_word():
    words = open("c:/Users/user/Documents/hangman/data/words.txt")
    my_Word= words.read().upper()
    wording = random.choice(my_Word.split())
    return wording
    

def display_word(wording):
    word_completion = "_" * len(wording)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    guesses = {}
    print("Let's play Hangman!")
    print(word_completion)
    print("\n")      
    while not guessed and tries > 0:
        guess = input("Please guess a letter: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in wording:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
                guesses[guess] = False
            else:
                print("YES", guess)
                guessed_letters.append(guess)
                guesses[guess] = True
                wording_as_list = list(word_completion)  
                indices = [i for i, letter in enumerate(wording) if letter == guess] 
                print(indices) 
                for index in indices:
                    wording_as_list[index] = guess
                word_completion = "".join(wording_as_list)  
                if "_" not in word_completion:
                    guessed = True  

        elif len(guess) == len(wording) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)  
            elif guess != wording:
                print(guess, "is not the word")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = wording    
        else:
            print("NO!")  
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
        print(guesses)  
    else:
        print("Sorry,you ran out of tries. The word was" +" " + wording + ". Maybe next time!")          
        
    
def main():
    wording = get_word()
    display_word(wording)        
    while input("Play again? (Y/%)").upper() == "Y":
        wording = get_word()
        display_word(wording)

    


        






    #for indexNumber, letter in enumerate(wording):
        #if letter in wording:
           #indexNumber = wording.index(letter)
           
        #print("YES {}".format(indexNumber))
        

   
        
        



















if __name__ == '__main__':
    main()