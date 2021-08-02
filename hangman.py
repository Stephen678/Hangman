import random
words = ["chicken", "individual", "laptop", "office", "telephone"]

def get_target_word():
    words = open("c:/Users/user/Documents/hangman/data/words.txt")
    my_Word= words.read().upper()
    target_word= random.choice(my_Word.split())
    return target_word
    
class Hangman:
    def __init__(self, target_word):
        self.target_word = target_word

    
    def display_word(self):
        word_completion = "_" * len(self.target_word)
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
                elif guess not in self.target_word:
                    print(guess, "is not in the word.")
                    tries -= 1
                    guessed_letters.append(guess)
                    guesses[guess] = False
                else:
                    print("YES", guess)
                    guessed_letters.append(guess)
                    guesses[guess] = True
                    wording_as_list = list(word_completion)  
                    indices = [i for i, letter in enumerate(self.target_word) if letter == guess] 
                    print(indices) 
                    for index in indices:
                        wording_as_list[index] = guess
                    word_completion = "".join(wording_as_list)  
                    if "_" not in word_completion:
                        guessed = True  

            elif len(guess) == len(self.target_word) and guess.isalpha():
                if guess in guessed_words:
                    print("You already guessed the word", guess)  
                elif guess != self.target_word:
                    print(guess, "is not the word")
                    tries -= 1
                    guessed_words.append(guess)
                else:
                    guessed = True
                    word_completion = self.target_word    
            else:
                print("NO!")  
            print(word_completion)
            print("\n")
        if guessed:
            print("Congrats, you guessed the word! You win!")
            print(guesses)  
        else:
            print("Sorry,you ran out of tries. The word was" + " " + self.target_word + ". Maybe next time!")          
            
        
    def run(self):
        self.display_word()        
        while input("Play again? (Y/%)").upper() == "Y":
            self.target_word = get_target_word()
            self.display_word()
target_word = get_target_word()
my_object = Hangman(target_word)
my_object.run()