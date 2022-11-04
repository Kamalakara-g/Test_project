s = "Hello world welcome to python programming"
def get_words(word):
	if word[0] in 'pw':
		return word
print(list(filter(get_words, s.split())))

l = [1,2,3,4,5]
print([i*i for i in l])