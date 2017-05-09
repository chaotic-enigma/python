def digit_sum(n):
    s = 0
    while n != 0:
        s = s + (n % 10)
        n = n / 10
    return s

print digit_sum(123)
print digit_sum(2345678)
print 

def digit_multiplication(n):
	s = 1;
	while n != 0:
		s = s * (n % 10)
		n = n / 10
	return s

print digit_multiplication(123234)
print 

def factorial(x):
	s = 1
	while x > 0:
		s = s * x
		x -= 1
	return s

#print factorial(12345)
print factorial(5)
print 

def is_prime(x):
	if x < 2:
		return False
	else:
		for any_number in range (2, x):
			if x % any_number == 0:
				return False
		return True

print is_prime(13)
print is_prime(232)
print 

def reverse_string(text):
	l = list(text)
	l_rv = l.reverse()
	l_jn = "".join(l)
	return l_jn

print reverse_string('wertygfd')
print 

def palindrome_string(text):
	if reverse_string(text) == text:
		return 'Plindrome'
	else:
		return False

print palindrome_string('sssssss')
print palindrome_string('sdrjvhfjh')
print

"""def anti_vowel(text):
    a = int(text.lower())
    l_text = list(text)
    for vowel in l_text:
        if text[vowel] == 'a' or text[vowel] == 'e' or text[vowel] == 'i' or text[vowel] == 'o' or text[vowel] == 'u':
            l_text.remove(text[vowel])
    return str("".join(l_text))

print anti_vowel('asnuhy')""" #my own code .... didn't work

def anti_vowel(text):
	anti_vowel_text = ''
	for vowel in text:
		if vowel not in 'AEIOUaeiou':
			anti_vowel_text += vowel
	return anti_vowel_text

print anti_vowel('airirowncjroe')
print anti_vowel('aeioujarvis')
print 

