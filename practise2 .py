s = "Hello world welcome to python programming"
def get_words(word):
	if word[0] in 'pw':
		return word
print(list(filter(get_words, s.split())))