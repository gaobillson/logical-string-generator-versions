"""
Please refer to the Logical String Generator changelog

"""
import random


def get_index(letter):
    indexes = len(letter) - 1
    index = random.randint(0, indexes)
    return index


alphabet = "abcdefghijklmnopqrstuvwxyz"

a = "nltrcsbmpdgeuivkfywzhxoqja"
b = "leairoubsycdtmphjfvgnwkqz"
c = "oaheirtulkyc"
d = "eioarulydngs"
e = "rsdltacmpxeouivfgbwy"
f = "oieluarfty"
g = "earilounyhgms"
h = "eoiayurtlnmw"
i = "ncstoadlmzvfprgebku"
j = "uaoei"
k = "eiaolnuyhsrwbtfkm"
l = "eiayloutdpmvcsnf"
m = "aeiopuybmn"
n = "etoigadcsnuyfkvlp"
o = "nrulptsmcgdovwibafkex"
p = "rehaoiltusypn"
q = "uia"
r = "eaiotymscdrunpbghlvkf"
s = "tseiuchpaomlynkwq"
t = "eiraohyutlcws"
u = "nslrmtciapedgbo"
v = "eiaou"
w = "aioehrnlsdkybtum"
x = "iaeyotucplbh"
y = "lstacpmonerigdwbhufz"
z = "eaoiyzul"

while True:
    try:
        length_of_text = int(input("Enter the length of the text to be generated: "))
        num_of_texts = int(input("Enter the number of texts to be generated: "))
        if length_of_text < 1:
            raise ValueError
        elif num_of_texts < 1:
            raise ValueError
        break
    except:
        print("Enter an integer greater than 0.")

print()
while True:
    for words in range(num_of_texts):
        word = ""
        current = alphabet[get_index(alphabet)]
        for character in range(length_of_text):
            word += current
            if current == "a":
                current = a[get_index(a)]
            elif current == "b":
                current = b[get_index(b)]
            elif current == "c":
                current = c[get_index(c)]
            elif current == "d":
                current = d[get_index(d)]
            elif current == "e":
                current = e[get_index(e)]
            elif current == "f":
                current = f[get_index(f)]
            elif current == "g":
                current = g[get_index(g)]
            elif current == "h":
                current = h[get_index(h)]
            elif current == "i":
                current = i[get_index(i)]
            elif current == "j":
                current = j[get_index(j)]
            elif current == "k":
                current = k[get_index(k)]
            elif current == "l":
                current = l[get_index(l)]
            elif current == "m":
                current = m[get_index(m)]
            elif current == "n":
                current = n[get_index(n)]
            elif current == "o":
                current = o[get_index(o)]
            elif current == "p":
                current = p[get_index(p)]
            elif current == "q":
                current = q[get_index(q)]
            elif current == "r":
                current = r[get_index(r)]
            elif current == "s":
                current = s[get_index(s)]
            elif current == "t":
                current = t[get_index(t)]
            elif current == "u":
                current = u[get_index(u)]
            elif current == "v":
                current = v[get_index(v)]
            elif current == "w":
                current = w[get_index(w)]
            elif current == "x":
                current = x[get_index(x)]
            elif current == "y":
                current = y[get_index(y)]
            elif current == "z":
                current = z[get_index(z)]
        print(f"Word #{words + 1}:\t{word}")

    print()

    while True:
        try:
            temp_length = length_of_text
            temp_num = num_of_texts
            length_of_text = input("Press 'Enter' to repeat with the same settings, "
                                   "type 'e' to exit, "
                                   "or type the new length of the string text: ")
            num_of_texts = input("Press 'Enter to repeat with the same settings, "
                                 "type 'e' to exit, "
                                 "or type the new number of texts: ")

            if length_of_text == "e" and num_of_texts == "e":
                break

            if length_of_text == "":
                length_of_text = temp_length
            if num_of_texts == "":
                num_of_texts = temp_num

            length_of_text = int(length_of_text)
            num_of_texts = int(num_of_texts)

            if length_of_text < 1:
                raise ValueError
            elif num_of_texts < 1:
                raise ValueError

            break
        except:
            print("Enter an integer greater than 0.")
            length_of_text = temp_length
            num_of_texts = temp_num

    if length_of_text == "e" and num_of_texts == "e":
        break

    print()
