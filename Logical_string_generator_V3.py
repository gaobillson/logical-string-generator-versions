"""
Please refer to the Logical String Generator changelog
"""
import random


def initial():
    index = random.randint(0, 25)
    return alphabet[index]


def get_index_a():
    index = random.randint(0, 100)
    chances_a = (16, 31, 45, 55, 62, 67, 72, 76, 80, 84, 87, 90, 92,
                 94, 95, 96, 97, 98, 99, 100)
    letters_a = "nltrcsbmpdgeuivkfywzhxoqja"

    for a in range(20):
        if index <= chances_a[a]:
            return letters_a[a]


def get_index_b():
    index = round(random.uniform(0, 100), 2)
    chances_b = (18.18, 33.34, 48.49, 62.63, 74.75, 84.85, 92.93, 94.95,
                 95.96, 96.97, 97.98, 98.99, 100.0)
    letters_b = "leairoubsycdt"

    for b in range(13):
        if index <= chances_b[b]:
            return letters_b[b]


def get_index_c():
    index = round(random.uniform(0, 100), 2)
    chances_c = (21.21, 38.39, 52.53, 62.63, 69.7, 76.77, 82.83, 87.88,
                 91.92, 95.96, 98.99, 100.0)
    letters_c = "oaheirtulkyc"

    for c in range(12):
        if index <= chances_c[c]:
            return letters_c[c]


def get_index_d():
    index = round(random.uniform(0, 100), 2)
    chances_d = (28.84, 54.68, 66.01, 77.34, 84.55, 88.67, 91.76, 93.82,
                 95.88, 97.94, 98.97, 100.0)
    letters_d = "eioarulydngs"

    for d in range(12):
        if index <= chances_d[d]:
            return letters_d[d]


def get_index_e():
    index = round(random.uniform(0, 100), 2)
    chances_e = (21.21, 35.36, 46.47, 54.55, 61.62, 67.68, 72.73, 76.77,
                 80.81, 83.84, 86.87, 88.89, 90.91, 92.93, 93.94, 94.95,
                 95.96, 96.97, 97.98, 98.99, 100.0)
    letters_e = "rnsdltacmpxeouivfgbwy"

    for e in range(21):
        if index <= chances_e[e]:
            return letters_e[e]


def get_index_f():
    index = round(random.uniform(0, 100), 2)
    chances_f = (17.34, 34.72, 47.98, 60.22, 71.44, 81.64, 90.82, 95.92,
                 97.96, 100.0)
    letters_f = "oieluarfty"

    for f in range(10):
        if index <= chances_f[f]:
            return letters_f[f]


def get_index_g():
    index = round(random.uniform(0, 100), 2)
    chances_g = (17.82, 31.69, 44.56, 57.43, 67.33, 76.24, 82.18, 87.13,
                 91.09, 95.05, 98.02, 99.01, 100.0)
    letters_g = "earilounyhgms"

    for g in range(13):
        if index <= chances_g[g]:
            return letters_g[g]


def get_index_h():
    index = round(random.uniform(0, 100), 2)
    chances_h = (23.46, 40.84, 57.16, 72.46, 85.72, 88.78, 91.84, 94.9,
                 96.94, 97.96, 98.98, 100.0)
    letters_h = "eoiayurtlnmw"

    for h in range(12):
        if index <= chances_h[h]:
            return letters_h[h]


def get_index_i():
    index = random.randint(0, 100)
    chances_i = (20, 33, 44, 52, 60, 68, 73, 78, 81, 84, 87, 89, 91, 93,
                 95, 97, 98, 99, 100)
    letters_i = "ncstoadlmzvfprgebku"

    for i in range(19):
        if index <= chances_i[i]:
            return letters_i[i]


def get_index_j():
    index = round(random.uniform(0, 100), 2)
    chances_j = (28.28, 55.56, 75.76, 93.94, 100.0)
    letters_j = "uaoei"

    for j in range(5):
        if index <= chances_j[j]:
            return letters_j[j]


def get_index_k():
    index = round(random.uniform(0, 100), 2)
    chances_k = (33.66, 52.48, 65.35, 71.29, 76.24, 81.19, 84.16, 87.13,
                 90.1, 92.08, 94.06, 95.05, 96.04, 97.03, 98.02, 99.01,
                 100.0)
    letters_k = "eiaolnuyhsrwbtfkm"

    for k in range(17):
        if index <= chances_k[k]:
            return letters_k[k]


def get_index_l():
    index = round(random.uniform(0, 100), 2)
    chances_l = (20.4, 38.8, 53.08, 65.32, 76.54, 86.74, 89.8, 91.84,
                 92.86, 93.88, 94.9, 95.92, 96.94, 97.96, 98.98, 100.0)
    letters_l = "eiayloutdpmvcsnf"

    for l in range(16):
        if index <= chances_l[l]:
            return letters_l[l]


def get_index_m():
    index = round(random.uniform(0, 100), 2)
    chances_m = (22.22, 42.43, 61.62, 76.77, 82.83, 87.88, 91.92, 95.96,
                 98.99, 100.0)
    letters_m = "aeiopuybmn"

    for m in range(10):
        if index <= chances_m[m]:
            return letters_m[m]


def get_index_n():
    index = round(random.uniform(0, 100), 2)
    chances_n = (17.34, 30.64, 42.88, 54.1, 64.3, 73.48, 79.6, 85.72, 89.8,
                 91.84, 93.88, 94.9, 95.92, 96.94, 97.96, 98.98, 100.0)
    letters_n = "etoigadcsnuyfkvlp"

    for n in range(17):
        if index <= chances_n[n]:
            return letters_n[n]


def get_index_o():
    index = random.randint(0, 100)
    chances_o = (16, 27, 35, 43, 50, 57, 63, 69, 74, 79, 83, 87, 89, 91, 93,
                 95, 96, 97, 98, 99, 100)
    letters_o = "nrupsmltcgvdiobwafexk"

    for o in range(21):
        if index <= chances_o[o]:
            return letters_o[o]


def get_index_p():
    index = round(random.uniform(0, 100), 2)
    chances_p = (17.17, 32.33, 47.48, 59.6, 70.71, 77.78, 83.84, 87.88, 91.92,
                 94.95, 96.97, 98.99, 100.0)
    letters_p = "rehaoiltusypn"

    for p in range(13):
        if index <= chances_p[p]:
            return letters_p[p]


def get_index_q():
    return "u"


def get_index_r():
    index = round(random.uniform(0, 100), 2)
    chances_r = (17.17, 32.33, 47.48, 59.6, 63.64, 67.68, 71.72, 74.75, 77.78,
                 80.81, 83.84, 86.87, 88.89, 90.91, 92.93, 94.95, 95.96, 96.97,
                 97.98, 98.99, 100.0)
    letters_r = "eaiotymscdrunpbghlvkf"

    for r in range(21):
        if index <= chances_r[r]:
            return letters_r[r]


def get_index_s():
    index = round(random.uniform(0, 100), 2)
    chances_s = (19.19, 29.3, 39.4, 49.5, 57.58, 64.65, 70.71, 76.77, 82.83, 87.88,
                 91.92, 93.94, 95.96, 96.97, 97.98, 98.99, 100.0)
    letters_s = "tseiuchpaomlynkwq"

    for s in range(17):
        if index <= chances_s[s]:
            return letters_s[s]


def get_index_t():
    index = round(random.uniform(0, 100), 2)
    chances_t = (21.42, 42.88, 55.12, 66.34, 76.54, 86.74, 90.82, 93.88, 95.92, 96.94,
                 97.96, 98.98, 100.0)
    letters_t = "eiraohyutlcws"

    for t in range(13):
        if index <= chances_t[t]:
            return letters_t[t]


def get_index_u():
    index = round(random.uniform(0, 100), 2)
    chances_u = (37.74, 54.1, 63.28, 72.46, 78.58, 82.66, 85.72, 88.78, 90.82, 92.86,
                 94.9, 96.94, 97.96, 98.98, 100.0)
    letters_u = "nslrmtciapedgbo"

    for u in range(15):
        if index <= chances_u[u]:
            return letters_u[u]


def get_index_v():
    index = random.randint(0, 100)
    chances_v = (46, 71, 89, 98, 100)
    letters_v = "eiaou"

    for v in range(5):
        if index <= chances_v[v]:
            return letters_v[v]


def get_index_w():
    index = round(random.uniform(0, 100), 2)
    chances_w = (24.24, 41.42, 57.58, 71.72, 81.82, 85.86, 89.9, 91.92, 92.93, 93.94,
                 94.95, 95.96, 96.97, 97.98, 98.99, 100.0)
    letters_w = "aioehrnlsdkybtum"

    for w in range(16):
        if index <= chances_w[w]:
            return letters_w[w]


def get_index_x():
    index = round(random.uniform(0, 100), 2)
    chances_x = (30.3, 48.49, 60.61, 70.71, 80.81, 89.9, 92.93, 94.95, 96.97, 97.98,
                 98.99, 100.0)
    letters_x = "iaeyotucplbh"

    for x in range(12):
        if index <= chances_x[x]:
            return letters_x[x]


def get_index_y():
    index = round(random.uniform(0, 100), 2)
    chances_y = (16.16, 26.27, 35.36, 43.44, 51.52, 58.59, 64.65, 70.71, 75.76, 80.81,
                 84.85, 88.89, 91.92, 93.94, 94.95, 95.96, 96.97, 97.98, 98.99, 100.0)
    letters_y = "lstacpmonerigdwbhufz"

    for y in range(20):
        if index <= chances_y[y]:
            return letters_y[y]


def get_index_z():
    index = round(random.uniform(0, 100), 2)
    chances_z = (41.82, 61.24, 78.58, 87.76, 93.88, 97.96, 98.98, 100.0)
    letters_z = "eaoiyzul"

    for z in range(8):
        if index <= chances_z[z]:
            return letters_z[z]


def function_iterator():
    global current
    global string
    functions = (get_index_a(), get_index_b(), get_index_c(), get_index_d(), get_index_e(),
                 get_index_f(), get_index_g(), get_index_h(), get_index_i(), get_index_j(),
                 get_index_k(), get_index_l(), get_index_m(), get_index_n(), get_index_o(),
                 get_index_p(), get_index_q(), get_index_r(), get_index_s(), get_index_t(),
                 get_index_u(), get_index_v(), get_index_w(), get_index_x(), get_index_y(),
                 get_index_z())

    for i in range(26):
        if current == alphabet[i]:
            current = functions[i]
            string += current
            break


alphabet = "abcdefghijklmnopqrstuvwxyz"

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
    for texts in range(num_of_texts):
        current = initial()
        string = current
        for length in range(length_of_text - 1):
            function_iterator()
        print(f"Word #{texts + 1}:\t{string}")

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

"""
Estimated letters:
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
"""

"""
Alternate letter selector:
def function_chooser():
    global new
    if current == "a":
        new = get_index_a()
    elif current == "b":
        new = get_index_b()
    elif current == "c":
        new = get_index_c()
    elif current == "d":
        new = get_index_d()
    elif current == "e":
        new = get_index_e()
    elif current == "f":
        new = get_index_f()
    elif current == "g":
        new = get_index_g()
    elif current == "h":
        new = get_index_h()
    elif current == "i":
        new = get_index_i()
    elif current == "j":
        new = get_index_j()
    elif current == "k":
        new = get_index_k()
    elif current == "l":
        new = get_index_l()
    elif current == "m":
        new = get_index_m()
    elif current == "n":
        new = get_index_n()
    elif current == "o":
        new = get_index_o()
    elif current == "p":
        new = get_index_p()
    elif current == "q":
        new = get_index_q()
    elif current == "r":
        new = get_index_r()
    elif current == "s":
        new = get_index_s()
    elif current == "t":
        new = get_index_t()
    elif current == "u":
        new = get_index_u()
    elif current == "v":
        new = get_index_v()
    elif current == "w":
        new = get_index_w()
    elif current == "x":
        new = get_index_x()
    elif current == "y":
        new = get_index_y()
    elif current == "z":
        new = get_index_z()

    return new
"""
