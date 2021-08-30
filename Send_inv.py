#TODO: Create a letter using starting_letter.txt 


names = open("./Input/Names/invited_names.txt", "r")
n = names.read().split("\n")
print(n)

text = open("./Input/Letters/starting_letter.txt", "r")
t = text.read()

for i in range(0, 8):
    new_n = n[i]
    b = open(f"./Output/ReadyToSend/{new_n}.txt", "w")
    for x in t.replace("[name]", new_n):
        b.write(x)




