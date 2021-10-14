import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

word_dict = {row.letter: row.code for (index, row) in data.iterrows()}

def nato():
    answer = input("Give a String: ").upper()
    try:
        word_list = [word_dict[letter] for letter in answer]
    except KeyError:
        print("Please choose from the words in dictionary.")
        nato()
    else:
        print(word_list)


nato()
