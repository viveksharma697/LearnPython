# create a dictionary and take input from the user and return the meaning of the word from the dictionary

dic = {"cat":"rat", "bat":"hat", "gap":"pap"}
print(dic)
print("Word")
n1 = input()
print("Rhyme")
n2 = dic.get(n1)
print(n2)