def list_of_names(file):
    all_names =[]
    with open(file,'r') as f_names:
        f_names_contents = f_names.readlines()
        for name in f_names_contents:
            all_names.append(name.strip())

    return all_names


all_names = list_of_names('Input/Names/invited_names.txt')
print(all_names)
for name in all_names:
    with open('Input/Letters/starting_letter.txt','r') as f:

        f_contents = f.readlines()
        with open("Output/ReadyToSend/"+name + ".txt", 'w') as w_file:
            for line in f_contents:
                if line.startswith("Dear"):
                    word = line[5:-2]
                    w_file.write(line.replace(word,name))
                    continue
                w_file.write(line)

