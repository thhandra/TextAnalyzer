import string
import re
import sys

# file = sys.argv[-1]
file = open("mytext.txt", "r")  # open the file

data = file.read()  # read the data from the file

pctmarks = ['.', ',', '?', '!', ';', ':', '"', '`', '(', ')']
count = 0
words = data.split()  # split into list

# count the words (checks if every letter isalpha)
for word in words:
    ok = 1
    for letter in word:
        if letter not in pctmarks:
            if not letter.isalpha():
                ok = 0
    if ok == 1:
        count += 1
        # print(word)

print("Numarul de cuvinte este: ", count)


# counts the sentences
# considering they are separated by . ? or !
sentences = 0
sentences += data.count('.') + data.count('?') + data.count('!')

print("Numarul de propozitii este: ", sentences)

# create dict with all lowercase letters
d = dict.fromkeys(string.ascii_lowercase, 0)

# compute frequency of each letter
for word in words:
    for letter in word:
        for key, val in d.items():
            if letter.lower() == key:
                d[key] += 1


# print(d)

# compute percentage of each letter (key/sum(val))
def get_letter_percentage(dictionary, lttr):
    return dictionary[lttr] * 1.0 / sum(dictionary.values()) * 100.0


print("Numarul de aparitii si procentul fiecarei litere este:")

for key, val in d.items():
    if val != 0:
        print(key, " : ", val, " (", get_letter_percentage(d, key), "%)")
        # mysum += get_letter_percentage(d, key)

# regex for phone number
# considering any phone number starts with 07
r1 = re.compile(r"^07\d{8}$")

# get the matches into a list
phonenums = list(filter(r1.match, words))

# delete duplicates
for i in range(len(phonenums)-1):
    for j in range(i+1, len(phonenums)):
        if phonenums[i] == phonenums[j]:
            del phonenums[j]
print("Numere de telefon: ", len(phonenums), phonenums)


# regexes for CNPs

r2 = re.compile(r"^[12][0-9][0-9]0[469]0[1-9]0[1-9][0-9][0-9][0-9][0-9]$")  # lunile 4 6 9 zilele 01-09 judetele 01-09

r17 = re.compile(r"^[12][0-9][0-9]0[469]0[1-9][1234][0-9][0-9][0-9][0-9][0-9]$")  # lunile 4 6 9 zilele 01-09 judetele 10-49

r18 = re.compile(r"^[12][0-9][0-9]0[469]0[1-9]5[0-2][0-9][0-9][0-9][0-9]$")  # lunile 4 6 9 zilele 01-09 judetele 50-52

r3 = re.compile(r"^[12][0-9][0-9]0[469][12][0-9]0[1-9][0-9][0-9][0-9][0-9]$")  # lunile 4 6 9 zilele 10-29 judetele 01-09

r19 = re.compile(r"^[12][0-9][0-9]0[469][12][0-9][1234][0-9][0-9][0-9][0-9][0-9]$")  # lunile 4 6 9 zilele 10-29 judetele 10-49

r20 = re.compile(r"^[12][0-9][0-9]0[469][12][0-9]5[0-2][0-9][0-9][0-9][0-9]$")  # lunile 4 6 9 zilele 10-29 judetele 50-52

r4 = re.compile(r"^[12][0-9][0-9]0[469]300[1-9][0-9][0-9][0-9][0-9]$")  # lunile 4 6 9 ziua 30 judetele 01-09

r21 = re.compile(r"^[12][0-9][0-9]0[469]30[1234][0-9][0-9][0-9][0-9][0-9]$")  # lunile 4 6 9 ziua 30 judetele 10-49

r22 = re.compile(r"^[12][0-9][0-9]0[469]305[0-2][0-9][0-9][0-9][0-9]$")  # lunile 4 6 9 ziua 30 judetele 50-52

r5 = re.compile(r"^[12][0-9][0-9]110[1-9]0[1-9][0-9][0-9][0-9][0-9]$")  # luna 11 zilele 01-09 judetele 01-09

r23 = re.compile(r"^[12][0-9][0-9]110[1-9][1234][0-9][0-9][0-9][0-9][0-9]$")  # luna 11 zilele 01-09 judetele 10-49

r24 = re.compile(r"^[12][0-9][0-9]110[1-9]5[0-2][0-9][0-9][0-9][0-9]$")  # luna 11 zilele 01-09 judetele 50-52

r6 = re.compile(r"^[12][0-9][0-9]11[12][0-9]0[1-9][0-9][0-9][0-9][0-9]$")  # luna 11 zilele 10-29 judetele 01-09

r25 = re.compile(r"^[12][0-9][0-9]11[12][0-9][1234][0-9][0-9][0-9][0-9][0-9]$")  # luna 11 zilele 10-29 judetele 10-49

r26 = re.compile(r"^[12][0-9][0-9]11[12][0-9]5[0-2][0-9][0-9][0-9][0-9]$")  # luna 11 zilele 10-29 judetele 50-52

r7 = re.compile(r"^[12][0-9][0-9]11300[1-9][0-9][0-9][0-9][0-9]$")  # luna 11 ziua 30 judetele 01-09

r27 = re.compile(r"^[12][0-9][0-9]1130[1234][0-9][0-9][0-9][0-9][0-9]$")  # luna 11 ziua 30 judetele 10-49

r28 = re.compile(r"^[12][0-9][0-9]11305[0-2][0-9][0-9][0-9][0-9]$")  # luna 11 ziua 30 judetele 50-52

r8 = re.compile(r"^[12][0-9][0-9]020[1-9]0[1-9][0-9][0-9][0-9][0-9]$")  # luna 2 zilele 01-09 judetele 01-09

r29 = re.compile(r"^[12][0-9][0-9]020[1-9][1234][0-9][0-9][0-9][0-9][0-9]$")  # luna 2 zilele 01-09 judetele 10-49

r30 = re.compile(r"^[12][0-9][0-9]020[1-9]5[0-2][0-9][0-9][0-9][0-9]$")  # luna 2 zilele 01-09 judetele 50-52

r9 = re.compile(r"^[12][0-9][0-9]021[0-9]0[1-9][0-9][0-9][0-9][0-9]$")  # luna 2 zilele 10-19 judetele 01-09

r31 = re.compile(r"^[12][0-9][0-9]021[0-9][1234][0-9][0-9][0-9][0-9][0-9]$")  # luna 2 zilele 10-19 judetele 10-49

r32 = re.compile(r"^[12][0-9][0-9]021[0-9]5[0-2][0-9][0-9][0-9][0-9]$")  # luna 2 zilele 10-19 judetele 50-52

r10 = re.compile(r"^[12][0-9][0-9]022[0-8]0[1-9][0-9][0-9][0-9][0-9]$")  # luna 2 zilele 20-28 judetele 01-09

r33 = re.compile(r"^[12][0-9][0-9]022[0-8][1234][0-9][0-9][0-9][0-9][0-9]$")  # luna 2 zilele 20-28 judetele 10-49

r34 = re.compile(r"^[12][0-9][0-9]022[0-8]5[0-2][0-9][0-9][0-9][0-9]$")  # luna 2 zilele 20-28 judetele 50-52

r11 = re.compile(r"^[12][0-9][0-9]0[13578]0[1-9]0[1-9][0-9][0-9][0-9][0-9]$")  # lunile 1 3 5 7 8 zilele 01-09 judetele 01-09

r35 = re.compile(r"^[12][0-9][0-9]0[13578]0[1-9][1234][0-9][0-9][0-9][0-9][0-9]$")  # lunile 1 3 5 7 8 zilele 01-09 judetele 10-49

r36 = re.compile(r"^[12][0-9][0-9]0[13578]0[1-9]5[0-2][0-9][0-9][0-9][0-9]$")  # lunile 1 3 5 7 8 zilele 01-09 judetele 50-52

r12 = re.compile(r"^[12][0-9][0-9]0[13578][12][0-9]0[1-9][0-9][0-9][0-9][0-9]$")  # lunile 1 3 5 7 8 zilele 10-29 judetele 01-09

r37 = re.compile(r"^[12][0-9][0-9]0[13578][12][0-9][1234][0-9][0-9][0-9][0-9][0-9]$")  # lunile 1 3 5 7 8 zilele 10-29 judetele 10-49

r38 = re.compile(r"^[12][0-9][0-9]0[13578][12][0-9]5[0-2][0-9][0-9][0-9][0-9]$")  # lunile 1 3 5 7 8 zilele 10-29 judetele 50-52

r13 = re.compile(r"^[12][0-9][0-9]0[13578]3[01]0[1-9][0-9][0-9][0-9][0-9]$")  # lunile 1 3 5 7 8 zilele 30 31 judetele 01-09

r39 = re.compile(r"^[12][0-9][0-9]0[13578]3[01][1234][0-9][0-9][0-9][0-9][0-9]$")  # lunile 1 3 5 7 8 zilele 30 31 judetele 10-49

r40 = re.compile(r"^[12][0-9][0-9]0[13578]3[01]5[0-2][0-9][0-9][0-9][0-9]$")  # lunile 1 3 5 7 8 zilele 30 31 judetele 50-52

r14 = re.compile(r"^[12][0-9][0-9]1[02]0[1-9]0[1-9][0-9][0-9][0-9][0-9]$")  # lunile 10 12 zilele 01-09 judetele 01-09

r41 = re.compile(r"^[12][0-9][0-9]1[02]0[1-9][1234][0-9][0-9][0-9][0-9][0-9]$")  # lunile 10 12 zilele 01-09 judetele 10-49

r42 = re.compile(r"^[12][0-9][0-9]1[02]0[1-9]5[0-2][0-9][0-9][0-9][0-9]$")  # lunile 10 12 zilele 01-09 judetele 50-52

r15 = re.compile(r"^[12][0-9][0-9]1[02][12][0-9]0[1-9][0-9][0-9][0-9][0-9]$")  # lunile 10 12 zilele 10-29 judetele 01-09

r43 = re.compile(r"^[12][0-9][0-9]1[02][12][0-9][1234][0-9][0-9][0-9][0-9][0-9]$")  # lunile 10 12 zilele 10-29 judetele 10-49

r44 = re.compile(r"^[12][0-9][0-9]1[02][12][0-9]5[0-2][0-9][0-9][0-9][0-9]$")  # lunile 10 12 zilele 10-29 judetele 50-52

r16 = re.compile(r"^[12][0-9][0-9]1[02]3[01]0[1-9][0-9][0-9][0-9][0-9]$")  # lunile 10 12 zilele 30 31 judetele 01-09

r45 = re.compile(r"^[12][0-9][0-9]1[02]3[01][1234][0-9][0-9][0-9][0-9][0-9]$")  # lunile 10 12 zilele 30 31 judetele 10-49

r46 = re.compile(r"^[12][0-9][0-9]1[02]3[01]5[0-2][0-9][0-9][0-9][0-9]$")  # lunile 10 12 zilele 30 31 judetele 50-52

# get them into a list of lists
cnps = list(filter(r2.match, words))


cnps.append(list(filter(r3.match, words)))
cnps.append(list(filter(r4.match, words)))
cnps.append(list(filter(r5.match, words)))
cnps.append(list(filter(r6.match, words)))
cnps.append(list(filter(r7.match, words)))
cnps.append(list(filter(r8.match, words)))
cnps.append(list(filter(r9.match, words)))
cnps.append(list(filter(r10.match, words)))
cnps.append(list(filter(r11.match, words)))
cnps.append(list(filter(r12.match, words)))
cnps.append(list(filter(r13.match, words)))
cnps.append(list(filter(r14.match, words)))
cnps.append(list(filter(r15.match, words)))
cnps.append(list(filter(r16.match, words)))
cnps.append(list(filter(r17.match, words)))
cnps.append(list(filter(r18.match, words)))
cnps.append(list(filter(r19.match, words)))
cnps.append(list(filter(r20.match, words)))
cnps.append(list(filter(r21.match, words)))
cnps.append(list(filter(r22.match, words)))
cnps.append(list(filter(r23.match, words)))
cnps.append(list(filter(r24.match, words)))
cnps.append(list(filter(r25.match, words)))
cnps.append(list(filter(r26.match, words)))
cnps.append(list(filter(r27.match, words)))
cnps.append(list(filter(r28.match, words)))
cnps.append(list(filter(r29.match, words)))
cnps.append(list(filter(r30.match, words)))
cnps.append(list(filter(r31.match, words)))
cnps.append(list(filter(r32.match, words)))
cnps.append(list(filter(r33.match, words)))
cnps.append(list(filter(r34.match, words)))
cnps.append(list(filter(r35.match, words)))
cnps.append(list(filter(r36.match, words)))
cnps.append(list(filter(r37.match, words)))
cnps.append(list(filter(r38.match, words)))
cnps.append(list(filter(r39.match, words)))
cnps.append(list(filter(r40.match, words)))
cnps.append(list(filter(r41.match, words)))
cnps.append(list(filter(r42.match, words)))
cnps.append(list(filter(r43.match, words)))
cnps.append(list(filter(r44.match, words)))
cnps.append(list(filter(r45.match, words)))
cnps.append(list(filter(r46.match, words)))

# print(cnps)

# make a flat list only with non null values
flat_list = []
for sublist in cnps:
    for item in sublist:
        flat_list.append(item)

# print(flat_list)

flat_list = list(dict.fromkeys(flat_list))  # remove duplicates


print("CNP-uri: ", len(flat_list), flat_list)














