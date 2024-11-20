from translations import romaji

# Prints a chart of all translations
# print("\tH\tK")
# for item in romaji:
#     print(f"{item}:",end=" ")
#     print(f'\t{romaji[item]["hiragana"]}\t{romaji[item]["katakana"]}')

input = "katakana sushi"
print(input)
word = ""
trial = ""
index = 0
while index < (len(input)):
    try:
        trial = input[index:index+3]
        test = romaji[trial]
    except KeyError:
        try:
            trial = input[index:index+2]
            test = romaji[trial]
        except KeyError:
            try:
                trial = input[index:index+1]
                test = romaji[trial]
            except KeyError:
                word = trial
            else:
                word = romaji[trial]["hiragana"]
        else:
            word = romaji[trial]["hiragana"]
            index = index + 1
    else:
        word = romaji[trial]["hiragana"]
        index = index + 2
    print(word,end="")
    index = index + 1

print()