import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

word_dict = {row.letter: row.code for (index, row) in data.iterrows()}
answer = input("Give a String: ").upper()

word_list = [word_dict[letter] for letter in answer]
print(word_list)
