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
    input = "katakana sushi"
    print(input)
    print(translate(input))