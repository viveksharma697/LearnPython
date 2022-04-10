# create a function in python that accepts one parameter: a string that's a sentence. This function should return True if any word in that sentence contains duplicate letters and False if not


def duplicate_letters(text):
	word_list = text.split()
	for n in word_list:
		if len(n) > len(set(n)):
			return True
	return False

a = "thiss is a pen"
print(a)
print("Is there any duplicate letter within a word ? ", duplicate_letters(a))
