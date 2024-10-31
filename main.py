from translations import romaji

print("   H   K")
for item in romaji:
    print(f"{item}:",end=" ")
    print(f'{romaji[item]["hiragana"]}  {romaji[item]["katakana"]}')
    