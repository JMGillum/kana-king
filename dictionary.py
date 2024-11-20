values = []
with open("translations.txt","r") as f:
    values = f.readlines()

h = values[0].split()
k = values[1].split()
r = values[2].split()

for i in range(len(h)):
    print(f"{r[i]}:  {h[i]}   {k[i]}")

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