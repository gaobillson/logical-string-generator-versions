raw = []
letters = "nth sch scr shr spl spr squ str thr"

temp = [sum(raw[:i + 1]) for i in range(len(raw))]
# if temp[-1] != 100:
# edited = True
# previous_total = temp[-1]
# factor = ((100 - temp[-1]) / 100)
# scaling = factor + 1
# touch_up = factor * (100 - temp[-1])
# chances = [raw[i] * scaling for i in range(len(raw))]
# chances[1] = chances[1] + touch_up
chances = [sum(raw[:i + 1]) for i in range(len(raw))]
# chances = [round(i, 2) for i in chances]
# else:
# edited = False
# chances = temp
# previous_total = ""

str_chances = str(chances)
str_chances = str_chances[1:len(str_chances) - 1]

letters = tuple(letters.split())

"""
def remove_sub(string, integer):
    return string[:integer] + "" + string[integer + 1:]


def duplicate_checker():
    for i in range(len(letters) - 1):
        if letters[i] in remove_sub(letters, i):
            print(f"{letters[i]} is duplicated")
"""

# if edited:
# print("Previous total: " + str(previous_total))
print(str_chances)
print("Length: " + str(len(chances)))
print()
print(letters)
print("Length: " + str(len(letters)))
# duplicate_checker()
