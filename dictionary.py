# EXAMPLE OF TRANSLATIONS FILE. EACH ITEM IS SEPARATED BY SPACE
# あ い う え お か き く け こ さ し す せ そ た ち つ て と な に ぬ ね の は ひ ふ へ ほ ま み む め も や ゆ よ ら り る れ ろ わ を ん
# ア イ ウ エ オ カ キ ク ケ コ サ シ ス セ ソ タ チ ツ テ ト ナ ニ ヌ ネ ノ ハ ヒ フ ヘ ホ マ ミ ム メ モ ヤ ユ ヨ ラ リ ル レ ロ ワ ヲ ン
# a i u e o ka ki ku ke ko sa shi su se so ta chi tsu te to na ni nu ne no ha hi fu he ho ma mi mu me mo ya yu yo ra ri ru re ro wa wo n


values = []
with open("translations.txt","r") as f: # Reads values to a list
    values = f.readlines()

h = values[0].split() # Hiragana is first line
k = values[1].split() # Katakana is second line
r = values[2].split() # Romaji is third line

# Writes dictionary to an output file
output = "translations.py"
with open(output,"w") as f:
    f.write("romaji = {\n")
    for i in range(len(h)):
        f.write(f'\t"{r[i]}":')
        f.write("{\n")
        f.write(f'\t\t"hiragana":"{h[i]}",\n\t\t"katakana":"{k[i]}"\n')
        f.write("\t}")
        if i < (len(h)-1):
            f.write(",")
        f.write("\n")
    f.write("}\n")