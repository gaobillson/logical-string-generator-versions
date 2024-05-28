"""
Please refer to the Logical String Generator changelog

"""
import random


def initial():
    index = random.randint(0, 25)
    return alphabet[index]


def get_index_a():
    index = random.randint(0, 100000)
    chances_a = (16210, 30778, 44973, 55149, 62061, 67232, 72296, 76491, 80514,
                 84239, 87291, 89899, 91932, 93778, 94976, 96017, 96955, 97650,
                 98225, 98751, 99169, 99584, 99751, 99896, 99954, 100000)
    letters_a = ("n", "l", "t", "r", "c", "s", "b", "m", "p", "d", "g", "e", "u",
                 "i", "v", "k", "f", "y", "w", "z", "h", "x", "o", "q", "j", "a")

    for a in range(26):
        if index <= chances_a[a]:
            return letters_a[a]


def get_index_b():
    index = random.randint(0, 100000)
    chances_b = (17794, 32854, 47536, 61116, 72630, 83098, 90798, 93125, 94522,
                 95505, 96245, 96962, 97627, 98094, 98516, 98837, 99136, 99345,
                 99550, 99711, 99845, 99939, 99961, 99983, 100000)
    letters_b = ("l", "e", "a", "i", "r", "o", "u", "b", "s", "y", "c", "d",
                 "t", "m", "p", "h", "j", "f", "v", "g", "n", "w", "k", "q",
                 "z")

    for b in range(26):
        if index <= chances_b[b]:
            return letters_b[b]


def get_index_c():
    index = random.randint(0, 100000)
    chances_c = (20811, 37540, 51874, 62090, 69138, 75837, 81718, 86906, 91157,
                 94685, 97797, 99207, 99628, 99822, 99872, 99915, 99953, 99967,
                 99980, 99987, 99995, 100000)
    letters_c = ("o", "a", "h", "e", "i", "r", "t", "u", "l", "k", "y", "c", "s",
                 "n", "q", "z", "m", "d", "w", "p", "b", "f")

    for c in range(22):
        if index <= chances_c[c]:
            return letters_c[c]


def get_index_d():
    index = random.randint(0, 100000)
    chances_d = (27744, 53105, 64486, 75493, 82642, 86914, 89643, 91998, 94019,
                 95673, 96665, 97388, 97839, 98275, 98683, 99011, 99215, 99391,
                 99546, 99685, 99818, 99923, 99963, 99991, 100000)
    letters_d = ("e", "i", "o", "a", "r", "u", "l", "y", "d", "n", "g", "s", "m",
                 "w", "h", "f", "b", "v", "t", "j", "p", "c", "k", "z", "q")

    for d in range(25):
        if index <= chances_d[d]:
            return letters_d[d]


def get_index_e():
    index = random.randint(0, 100000)
    chances_e = (21117, 34837, 45670, 54007, 60619, 66589, 71757, 76231, 79816,
                 82724, 85462, 87833, 90151, 92451, 93783, 94798, 95810, 96816,
                 97588, 98196, 98759, 99221, 99623, 99804, 99910, 100000)
    letters_e = ("r", "n", "s", "d", "l", "t", "a", "c", "m", "p", "x", "e", "o",
                 "u", "i", "v", "f", "g", "b", "w", "y", "q", "h", "k", "z", "j")

    for e in range(26):
        if index <= chances_e[e]:
            return letters_e[e]


def get_index_f():
    index = random.randint(0, 100000)
    chances_f = (17155, 33744, 47195, 59679, 70223, 80695, 90127, 95383, 97606,
                 99231, 99402, 99507, 99586, 99665, 99737, 99803, 99849, 99895,
                 99928, 99954, 99980, 99993, 100000)
    letters_f = ('o', 'i', 'e', 'l', 'u', 'a', 'r', 'f', 't', 'y', 's', 'n', 'w',
                 'h', 'm', 'd', 'c', 'b', 'g', 'j', 'p', 'k', 'v')

    for f in range(23):
        if index <= chances_f[f]:
            return letters_f[f]


def get_index_g():
    index = random.randint(0, 100000)
    chances_g = (17649, 31615, 44278, 56814, 66539, 75059, 81541, 86173, 90300,
                 94110, 96786, 98200, 98759, 99088, 99318, 99544, 99680, 99803,
                 99910, 99943, 99968, 99988, 99996, 100000)
    letters_g = ('e', 'a', 'r', 'i', 'l', 'o', 'u', 'n', 'y', 'h', 'g', 'm', 's',
                 'w', 't', 'b', 'f', 'd', 'p', 'z', 'k', 'c', 'v', 'j')

    for g in range(24):
        if index <= chances_g[g]:
            return letters_g[g]


def get_index_h():
    index = random.randint(0, 100000)
    chances_h = (23123, 40255, 55828, 71228, 84525, 87989, 91012, 93525, 95305,
                 96765, 97774, 98311, 98715, 99065, 99354, 99520, 99629, 99738,
                 99833, 99898, 99952, 99972, 99986, 100000)
    letters_h = ('e', 'o', 'i', 'a', 'y', 'u', 'r', 't', 'l', 'n', 'm', 'w', 'b',
                 'f', 's', 'p', 'h', 'c', 'd', 'g', 'k', 'v', 'q', 'z')

    for h in range(24):
        if index <= chances_h[h]:
            return letters_h[h]


def get_index_i():
    index = random.randint(0, 100000)
    chances_i = (19675, 32735, 43917, 51988, 59773, 67289, 72658, 77605, 80610,
                 83128, 85629, 87936, 90166, 92293, 94261, 96226, 97557, 98471,
                 99348, 99548, 99741, 99838, 99905, 99942, 99974, 100000)
    letters_i = ('n', 'c', 's', 't', 'o', 'a', 'd', 'l', 'm', 'z', 'v', 'f', 'p',
                 'r', 'g', 'e', 'b', 'k', 'u', 'i', 'x', 'q', 'h', 'j', 'w', 'y')

    for i in range(26):
        if index <= chances_i[i]:
            return letters_i[i]


def get_index_j():
    index = random.randint(0, 100000)
    chances_j = (27992, 54979, 74937, 92678, 98870, 99163, 99372, 99539, 99665,
                 99749, 99833, 99875, 99916, 99958, 100000)
    letters_j = ('u', 'a', 'o', 'e', 'i', 'r', 'h', 'y', 'n', 'd', 'l', 'm', 'p',
                 'b', 't')

    for j in range(15):
        if index <= chances_j[j]:
            return letters_j[j]


def get_index_k():
    index = random.randint(0, 100000)
    chances_k = (34017, 52751, 65535, 71132, 76525, 81293, 84377, 87339, 89988,
                 92148, 93914, 94919, 95829, 96671, 97486, 98206, 98912, 99211,
                 99510, 99673, 99836, 99932, 99986, 100000)
    letters_k = ('e', 'i', 'a', 'o', 'l', 'n', 'u', 'y', 'h', 's', 'r', 'w', 'b',
                 't', 'f', 'k', 'm', 'd', 'p', 'j', 'c', 'g', 'v', 'z')

    for k in range(24):
        if index <= chances_k[k]:
            return letters_k[k]


def get_index_l():
    index = random.randint(0, 100000)
    chances_l = (20017, 38110, 52050, 64467, 75254, 85674, 89102, 91320, 92645,
                 93826, 94776, 95711, 96569, 97244, 97875, 98435, 98896, 99344,
                 99637, 99785, 99891, 99970, 99991, 99994, 99997, 100000)
    letters_l = ('e', 'i', 'a', 'y', 'l', 'o', 'u', 't', 'd', 'p', 'm', 'v', 'c',
                 's', 'n', 'f', 'k', 'g', 'b', 'w', 'h', 'r', 'z', 'x', 'j', 'q')

    for l in range(26):
        if index <= chances_l[l]:
            return letters_l[l]


def get_index_m():
    index = random.randint(0, 100000)
    chances_m = (22239, 42024, 61365, 76765, 82620, 87226, 91026, 94649, 97560,
                 98734, 99050, 99320, 99505, 99595, 99664, 99732, 99795, 99850,
                 99900, 99934, 99960, 99981, 99989, 99997, 100000)
    letters_m = ('a', 'e', 'i', 'o', 'p', 'u', 'y', 'b', 'm', 'n', 's', 'l', 'f',
                 'r', 'd', 'w', 'c', 't', 'h', 'v', 'k', 'g', 'j', 'z', 'q')

    for m in range(25):
        if index <= chances_m[m]:
            return letters_m[m]


def get_index_n():
    index = random.randint(0, 100000)
    chances_n = (17225, 30184, 42426, 53740, 63995, 73093, 79378, 84969, 88575,
                 90592, 92616, 93688, 94686, 95637, 96275, 96896, 97407, 97896,
                 98294, 98691, 99023, 99339, 99581, 99811, 99938, 100000)
    letters_n = ('e', 't', 'o', 'i', 'g', 'a', 'd', 'c', 's', 'n', 'u', 'y', 'f',
                 'k', 'v', 'l', 'p', 'r', 'm', 'z', 'h', 'b', 'j', 'w', 'q', 'x')

    for n in range(26):
        if index <= chances_n[n]:
            return letters_n[n]


def get_index_o():
    index = random.randint(0, 100000)
    chances_o = (15524, 26631, 34337, 41950, 48791, 55614, 62009, 68019, 73363,
                 78028, 81739, 85269, 87736, 90059, 92180, 93937, 95204, 96269,
                 97223, 98091, 98820, 99208, 99510, 99794, 99928, 100000)
    letters_o = ('n', 'r', 'u', 'p', 's', 'm', 'l', 't', 'c', 'g', 'v', 'd', 'i',
                 'o', 'b', 'w', 'a', 'f', 'e', 'x', 'k', 'h', 'y', 'z', 'q', 'j')

    for o in range(26):
        if index <= chances_o[o]:
            return letters_o[o]


def get_index_p():
    index = random.randint(0, 100000)
    chances_p = (16661, 32152, 47367, 59825, 71201, 78366, 84814, 88403, 91931,
                 95083, 97091, 98992, 99582, 99699, 99778, 99853, 99897, 99937,
                 99968, 99986, 99994, 99996, 99998, 100000)
    letters_p = ('r', 'e', 'h', 'a', 'o', 'i', 'l', 't', 'u', 's', 'y', 'p', 'n',
                 'm', 'w', 'f', 'b', 'c', 'k', 'g', 'd', 'j', 'v', 'q')

    for p in range(24):
        if index <= chances_p[p]:
            return letters_p[p]


def get_index_q():
    index = random.randint(0, 100000)
    chances_q = (99636, 99727, 99817, 99863, 99909, 99955, 100000)
    letters_q = ('u', 'e', 'o', 'a', 'r', 'q', 'i')

    for q in range(7):
        if index <= chances_q[q]:
            return letters_q[q]


def get_index_r():
    index = random.randint(0, 100000)
    chances_r = (17368, 32281, 47083, 59514, 63736, 67619, 71457, 74520, 77527,
                 80506, 83462, 86118, 88352, 90497, 92107, 93634, 95032, 96353,
                 97427, 98429, 99249, 99743, 99843, 99934, 99993, 100000)
    letters_r = ('e', 'a', 'i', 'o', 't', 'y', 'm', 's', 'c', 'd', 'r', 'u', 'n',
                 'p', 'b', 'g', 'h', 'l', 'v', 'k', 'f', 'w', 'j', 'q', 'z', 'x')

    for r in range(26):
        if index <= chances_r[r]:
            return letters_r[r]


def get_index_s():
    index = random.randint(0, 100000)
    chances_s = (19285, 29434, 39067, 48643, 56287, 62828, 69194, 75145, 81066,
                 86129, 90310, 92498, 94456, 95904, 97001, 97985, 98786, 99094,
                 99324, 99508, 99687, 99846, 99940, 99989, 100000)
    letters_s = ('t', 's', 'e', 'i', 'u', 'c', 'h', 'p', 'a', 'o', 'm', 'l', 'y',
                 'n', 'k', 'w', 'q', 'f', 'b', 'r', 'g', 'd', 'v', 'j', 'z')

    for s in range(25):
        if index <= chances_s[s]:
            return letters_s[s]


def get_index_t():
    index = random.randint(0, 100000)
    chances_t = (21499, 42849, 54921, 65446, 75712, 85319, 88895, 92305, 94707,
                 96071, 96918, 97617, 98267, 98604, 98938, 99230, 99466, 99610,
                 99718, 99820, 99890, 99928, 99960, 99988, 100000)
    letters_t = ('e', 'i', 'r', 'a', 'o', 'h', 'y', 'u', 't', 'l', 'c', 'w', 's',
                 'm', 'f', 'n', 'b', 'p', 'g', 'z', 'd', 'k', 'v', 'j', 'q')

    for t in range(25):
        if index <= chances_t[t]:
            return letters_t[t]


def get_index_u():
    index = random.randint(0, 100000)
    chances_u = (37203, 52739, 62098, 71355, 77218, 81656, 84472, 87016, 89411,
                 91640, 93740, 95364, 96731, 97994, 98592, 98971, 99270, 99494,
                 99711, 99791, 99857, 99895, 99933, 99960, 99984, 100000)
    letters_u = ('n', 's', 'l', 'r', 'm', 't', 'c', 'i', 'a', 'p', 'e', 'd', 'g',
                 'b', 'o', 'f', 'v', 'k', 'x', 'z', 'y', 'j', 'h', 'q', 'u', 'w')

    for u in range(26):
        if index <= chances_u[u]:
            return letters_u[u]


def get_index_v():
    index = random.randint(0, 100000)
    chances_v = (45838, 70449, 88556, 97643, 99387, 99689, 99812, 99878, 99916,
                 99944, 99963, 99982, 99991, 100000)
    letters_v = ('e', 'i', 'a', 'o', 'u', 'y', 'r', 'v', 'l', 's', 'c', 'k', 'n',
                 'g')

    for v in range(14):
        if index <= chances_v[v]:
            return letters_v[v]


def get_index_w():
    index = random.randint(0, 100000)
    chances_w = (23647, 40426, 56838, 71284, 81231, 85447, 89426, 91510, 92955,
                 94104, 94957, 95774, 96579, 97242, 97846, 98414, 98876, 99219,
                 99562, 99799, 99953, 99976, 99988, 100000)
    letters_w = ('a', 'i', 'o', 'e', 'h', 'r', 'n', 'l', 's', 'd', 'k', 'y', 'b',
                 't', 'u', 'm', 'f', 'w', 'p', 'c', 'g', 'q', 'v', 'z')

    for w in range(24):
        if index <= chances_w[w]:
            return letters_w[w]


def get_index_x():
    index = random.randint(0, 100000)
    chances_x = (29700, 47794, 59844, 69781, 79495, 88727, 91471, 93696, 95809,
                 96662, 97329, 97848, 98293, 98738, 99146, 99368, 99516, 99664,
                 99813, 99925, 99963, 100000)
    letters_x = ('i', 'a', 'e', 'y', 'o', 't', 'u', 'c', 'p', 'l', 'b', 'h', 'w',
                 'f', 'm', 's', 'd', 'g', 'n', 'q', 'r', 'k')

    for x in range(22):
        if index <= chances_x[x]:
            return letters_x[x]


def get_index_y():
    index = random.randint(0, 100000)
    chances_y = (15983, 26078, 34997, 43019, 50742, 57981, 64116, 70210, 75252,
                 79985, 84213, 87915, 90421, 92896, 94360, 95793, 96865, 97814,
                 98711, 99268, 99742, 99897, 99938, 99969, 100000)
    letters_y = ('l', 's', 't', 'a', 'c', 'p', 'm', 'o', 'n', 'e', 'r', 'i', 'g',
                 'd', 'w', 'b', 'h', 'u', 'f', 'z', 'x', 'k', 'q', 'y', 'v')

    for y in range(25):
        if index <= chances_y[y]:
            return letters_y[y]


def get_index_z():
    index = random.randint(0, 100000)
    chances_z = (41064, 60050, 77512, 86584, 92382, 96475, 97635, 98681, 98886,
                 99091, 99205, 99319, 99433, 99524, 99615, 99706, 99774, 99819,
                 99864, 99909, 99954, 99977, 100000)
    letters_z = ('e', 'a', 'o', 'i', 'y', 'z', 'u', 'l', 'w', 'd', 'r', 'm', 'c',
                 'h', 'k', 's', 'n', 'g', 't', 'p', 'b', 'f', 'v')

    for z in range(23):
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


alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

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

