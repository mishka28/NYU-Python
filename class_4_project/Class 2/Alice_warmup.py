#! usr/bin/env python

def vowel(sentance):
	vowels = ('a', 'e', 'i', 'o', 'u', 'y')
	s1 = []
	for l in s:
		if l not in vowels:
			s1.append(l)
	return ''.join(s1)
if __name__ == "__main__":

	s='make a function that removes all vowels from a sentense.'
	print(vowel(s))