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


# regex for cnp
r2 = re.compile("^[12]\\d{2}(0?[1-9]|1[012])(0?[1-9]|[12][0-9]|3[01])(0?[1-9]|[123][0-9]|4[0-6]|5[12])[0-9][0-9]["
                "0-9][0-9]$")

# get matches into list
cnps = list(filter(r2.match, words))

cnps = list(dict.fromkeys(cnps))  # remove duplicates

print("CNP-uri: ", len(cnps), cnps)













