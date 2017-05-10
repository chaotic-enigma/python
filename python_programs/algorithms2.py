score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

def scrabble_score(word):
    total = 0
    for letter in word:
        total += score[letter.lower()]
    return total

print (scrabble_score('pie'))
print ("\n")

def censor(text, word):
	if word in text:
		text = text.replace(word, "*" * len(word))
	return text

print (censor('what the fuck', 'fuck'))
print ("\n")

def count(sequence, item):
	item_count = 0
	for i in sequence:
		if i == item:
			item_count += 1
	return item_count

print (count([1,2,2,2,2,1,2,], 2))
print ("\n")

def purify_even(sequence):
	is_even = []
	for i in sequence:
		if i % 2 == 0:
			is_even.append(i)
	return is_even

print (purify_even([1,2,3,4,5,6,7,8,9,10]))
print ("\n")

def purify_odd(sequence):
	is_odd = []
	for i in sequence:
		if i % 2 != 0:
			is_odd.append(i)
	return is_odd

print (purify_odd([1,2,3,4,5,6,7,8,9,10]))
print ("\n")

def product(sequence):
	product_item = 1
	for item in sequence:
		product_item *= item
	return product_item

print (product([1,2,3,4,5,6,7,8,9,10]))
print ("\n")

def remove_duplicates(sequence):
	original = []
	for element in sequence:
		if element not in original:
			original.append(element)
	return original

print (remove_duplicates([1,2,3,1,1,4,5,6,7,7,8,9,9,1,10,10,10]))

def median(sequence):
    temp_list = sorted(sequence)
    if len(temp_list) % 2 > 0:
        return temp_list[len(temp_list) / 2]
    else:
        return (temp_list[len(temp_list) / 2] + temp_list[(len(temp_list) / 2) - 1]) / 2.0
        
print (median([1,2,3,4,5,6]))
        
