import random
from datetime import datetime

from translations import romaji


# Prints a chart of all translations
# print("\tH\tK")
# for item in romaji:
#     print(f"{item}:",end=" ")
#     print(f'\t{romaji[item]["hiragana"]}\t{romaji[item]["katakana"]}')

def translate(input):
    word = ""
    trial = ""
    index = 0
    output = ""
    while index < (len(input)):
        try: # Checks if it is three letter kana
            trial = input[index:index+3]
            romaji[trial]
        except KeyError:
            try: # Checks if it is two letter kana
                trial = input[index:index+2]
                romaji[trial]
            except KeyError:
                try: # Checks if it is one letter kana
                    trial = input[index:index+1]
                    romaji[trial]
                except KeyError:
                    word = trial
                else: # One letter kana
                    word = romaji[trial]["hiragana"]
            else: # Two letter kana
                word = romaji[trial]["hiragana"]
                index = index + 1
        else: # Three letter kana
            word = romaji[trial]["hiragana"]
            index = index + 2
        output = output + word
        index = index + 1
    return output

if __name__ == "__main__":    
    random.seed(datetime.now().timestamp())
    
    for i in range(3):
        item = random.choice(list(romaji.items())) # Picks a random item from the translation dictionary
        print(item[1]["hiragana"]) # Prints the hiragana of this item
        
        start = datetime.now().timestamp() # Timestamp for start of guessing
        maxAttempts = 5 # Number of incorrect guesses they can make before continuing on
        for i in range(maxAttempts): # Gets and checks answer from user
            answer = input("What is the romaji?: ")
            if answer.strip().lower() == item[0]:
                break
        end = datetime.now().timestamp()
        
        print(f"Total Time: {(end-start)}") # Prints the amount of time it took.
    