# sum of all elements in a given range
def summ_all(arr):
	total_sum = 0
	maximum = max(arr[0],arr[1])
	minimum = min(arr[0],arr[1])
	while (minimum <= maximum):
		total_sum += minimum
		minimum += 1
	return total_sum
print(summ_all([1,10]))
print

# poping out diff elements from two diff arrays
def diff_array(arr1,arr2):
	i = 0
	while (i <= len(arr1 + arr2)):
		for k in arr1:
			if k not in arr2:
				arr1.remove(k)
		for l in arr2:
			if l not in arr1:
				arr2.remove(l)
		i += 1
	return sorted(list(set(arr1))),sorted(list(set(arr2))) # removes duplicates
print(diff_array([1,2,3,6,4,5,3,2,6,6,0,0,7,7,5,-1,3],[1,2,3,7,8,4,5,5,5,5,4,4,4,-1,7,7]))
print

# conversion decimals into romans
def roman_convertor(num):
	decimal_numerals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
	roman_numerals = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
	romans = ''
	i = 0
	while (i < len(decimal_numerals)):
		while (decimal_numerals[i] <= num):
			romans += roman_numerals[i]
			num -= decimal_numerals[i]
		i += 1
	return romans
print(roman_convertor(36))
print

# replacing with a particular word in place of another word
def replace_swap(str,before,after):
	if before.lower() in str:
		return str.replace(before,after.lower()).title()
	else:
		pass
print(replace_swap('i want to earn billions working in redhat','redhat','google'))
print

# playing with the words
def vowel(char):
	return char.lower() in 'aeiou'
print vowel('sadf')
def vowel_target(str):
	count = 0
	i = 0
	while i < len(str):
		if vowel(str[i]):
			count = 1
			break
		i += 1
	if count == 1:
		return i
print vowel_target('ssssa')
def translate_piglatin(str):
	pig = ''
	if vowel(str[0]):
		pig = str + 'way'
	else:
		pig = str[vowel_target(str):] + str[:vowel_target(str)] + 'ay'
	return pig
#print(list('sgsgsg'))
print(translate_piglatin('i want to earn billions'.lower()))
print(translate_piglatin('google'))
print(translate_piglatin('glove'))
print

# dna pairing
def dna_pairing(str):
	dna = []
	for i in str:
		if i == 'A':
			dna.append(['A','T'])
		elif i == 'T':
			dna.append(['T','A'])
		elif i == 'C':
			dna.append(['C','G'])
		elif i == 'G':
			dna.append(['G','C'])
		else:
			pass
	return dna
print(dna_pairing('ATCG'))
print

# html entities
def html_entities(str):
 	if '&' in str:
 		return str.replace('&','&amp;')
 	elif '<' in str:
 		return str.replace('<','&lt;')
 	elif '>'in str:
 		return str.replace('>','&gt;')
 	elif '"' in str:
 		return str.replace('"','&quot;')
 	elif "'" in str:
 		return str.replace("'",'&apos;')
 	else:
 		pass
print(html_entities("Dolce & Gabbana")) 
print(html_entities('jdhfesy < jjdu'))
print(html_entities('& < > "'))
print

# important
import string
print(string.ascii_lowercase)
print(string.letters)
print(string.hexdigits)
print(string.octdigits)
print(string.digits)
print(string.printable)
print

# returning the missing letter
def fear_not_letter(str):
	alpha = str
	for i in string.ascii_lowercase:
		if i not in alpha:
			return i
		else:
			pass
print(fear_not_letter('abce'))
print(fear_not_letter('abcdfghijknlxzy')) # works only for once
print(fear_not_letter('abde'))
print

# sum of fibonacci series
def sum_fibs(num):
	previous_num = 0
	current_num = 1
	resultant = 0
	while (current_num < num):
		if (current_num % 2 != 0):
			resultant += current_num
		current_num += previous_num
		previous_num = current_num - previous_num
	return resultant
print(sum_fibs(4))
print

# best first search
def func(num):
	return num % 2 == 0
def find_element(arr):
	ele = 0
	i = 0
	while (i < len(arr)):
		if func(arr[i]):
			ele = arr[i]
			return ele
		i += 1
print(find_element([1,2,3,4]))
print

"""# drop the elements
def shift(l,n):
	return l[n:] + l[:n]
def drop(n):
	return n < 3
def drop_elements(arr):
	for i in arr:
		if (drop(i)):
			pass
		else:
			shift(arr,i)
print(drop_elements([1,2,3,4,5]))"""

"""l = 'samdjjfbhdbhdfdf'
print("{}").format(l)"""

# n - ascii; b - binary; c - char
def ascii_n(str): # ascii convertor
	return ' '.join(format(ord(i),'n')for i in str)
print(ascii_n('i want to earn billions'))
print
def ascii_b(str): # binary convertor
	return ' '.join(format(ord(i),'b')for i in str)
print(ascii_b('i want to earn billions'))
print
def ascii_c(str): # character convertor
	return ' '.join(format(ord(i),'c')for i in str)
print(ascii_c('i want to earn billions'))
print

# add all the arguments
def add_together(*args):
	result = 0
	for i in args:
		if type(i) == int:
			result += i
		else:
			return 'not possible'
	return result
print(add_together(2,3,4,5,(2)))
print

# returning the type of bool
def boo_whoo(booo):
	if bool(booo):
		return True
	else:
		return False
print(boo_whoo(3 == 1)) # true for everything except 0 and false values
print

# unite_unique and remove duplpicates
def unite_unique(*args):
	unique = []
	for i in args:
		unique.extend(i)
	return list(set(unique))
print(unite_unique([1,2,3],[1,2,3,4,5,6],[1,2,3,4,5,6,7,8],[0,-1,-2,-3]))
print 

# spinal case
def spinal_case(str):
	space = str.split(' ')
	return '-'.join(space).lower()
print(spinal_case('I want to earn billions'))
print(spinal_case('I gotta work for google'))
print(spinal_case('me from village area'))
print

print "%o %x %X" % (64, 64, 255)
# conversion of binary codes into string values
def add_0b(binary):
	temp = []
	for i in binary:
		temp.append('0b' + i)
	return temp
print(add_0b(['10101001','1010101']))
import binascii
#print(dir(binascii))
def bin_ascii(b):
	o = []
	oop = []
	s = b.split(' ')
	q = add_0b(s)
	for i in q:
		o.append(int(i,2)) # converts all binary codes to integer values
	for j in o:
		oop.append(binascii.unhexlify('%x' % j)) # converts all integer values to string values
	return ''.join(oop)
print(bin_ascii('1101001 100000 1110111 1100001 1101110 1110100 100000 1110100 1101111 100000 1100101 1100001 1110010 1101110 100000 1100010 1101001 1101100 1101100 1101001 1101111 1101110 1110011'))
print

# size in byte
units = ['KB', 'MB', 'GB', 'TB', 'PB']
def size_in_byte(size):
	if size < 0:
		raise ValueError('size < 0')
	factor = 1024
	for i in range(len(units)):
		if size < factor:
			if i == 0:
				return '{0:.1f} {1[0]}'.format(size, units)
			elif i == 1:
				return '{0:.1f} {1[1]}'.format(size, units)
			elif i == 2:
				return '{0:.1f} {1[2]}'.format(size, units)
			elif i == 3:
				return '{0:.1f} {1[3]}'.format(size, units)
			else:
				return '{0:.1f} {1[4]}'.format(size, units)
		else:
			size /= factor
	raise ValueError('too big')
print(size_in_byte(9))
print

# prime check of the argument
def prime_check_arg(prime):
	for i in range(2,prime):
		if prime % i == 0:
			return 'not a prime'
			break
	else:
		return 'prime'
print(prime_check_arg(23))
print(prime_check_arg(43))
print(prime_check_arg(53))
print(prime_check_arg(31))
print(prime_check_arg(33))
print(prime_check_arg(39))
print

# run length string encoding
def encoding(text):
	if not text:
		return ''
	else:
		string = text[0]
		length = len(text)
		i = 1
		while i < length and string == text[0]:
			i += 1
		return string + str(i) + encoding(text[i:])
print(encoding('sssssss'))
print

# run length string decoding
def decoding(text):
	if not text:
		return ''
	else:
		char = text[0]
		how_much = text[1]
		return char * int(how_much) + decoding(text[2:])
print(decoding('s3'))
print

# returning a prime number
def prime_mover(prime):
	for i in tuple(range(2,prime)):
		if prime % i == 0:
			return False
			break
	return str(prime) + ' --> prime'

for p in range(2,50):
	print(prime_mover(p))
print
#print tuple(range(10))

# gcd between two numbers
def gcd_two(x,y):
	while y != 0:
		(x,y) = (y,x % y)
	return x
print(gcd_two(8,20))
print(gcd_two(21,63))
print

# string scramble
from random import shuffle
def shuffle_word(word,ano_word):
	word = list(word)
	shuffle(word)
	shuffing =  ''.join(word)
	if shuffing == ano_word:
		return True
	else:
		return 'i want to earn billions'
print(shuffle_word('sameer','amrees'))
print(shuffle_word('saif','asif'))
print(shuffle_word('aaa','aaa'))
print

# arithematical and geometrical challenge
def arithe_geo(arr):
	if len(arr) == 0:
		return 'nil'
	for i in range(len(arr)):
		if arr[i + 1] - arr[i] == arr[i -1] - arr[i - 2]:
			return 'arithematic'
		elif arr[i + 1] / arr[i] == arr[i - 1] / arr[i - 2]:
			return 'geometric'
		else:
			return 'nope'
print(arithe_geo([2,4,8,16,32]))
print(arithe_geo([]))
print(arithe_geo([1,3,5,7,9]))
print(arithe_geo([1,3,4,5,7,8]))
print

# array addition
def arr_addition(arr):
	result = 0
	for i in arr:
		result += i
	return result
print(arr_addition([1,2,3,4,5]))
print 

# counting the repeated letter
# yet to be done

# simple mode, since i'm using python 2.7.6, numpy cannot be imported due to some reasons though i have installed
"""import numpy as np
def simple_mode(arr):
	frequent = np.array(arr)
	frequency = np.bincount(frequent)
	return np.argmax(frequency), np.argmin(frequency) # takes in ascending order including zero
print(simple_mode([1,1,1,12,3,2,4,5,6,1,1,1]))"""

# ceaser cipher
def ceaser_cipher(str):
	empty = []
	string = str.lower()
	string = list(string)
	for i in string:
		empty.append(chr(ord(i) + 3))
	return ' '.join(empty)
print(ceaser_cipher('i want to earn billions'))
print(ceaser_cipher('ft^kqqlb^ok_fiiflkp'))
print(ceaser_cipher('dhjs shgdhs dsdysgfyh evfewhsdcgs'))
print

# debugging by assert statement
def chcassert(num):
	assert type(num) == int
print(chcassert(2))
print

# number search and addition of it
def number_search(str):
	str = str.split()
	empty = []
	for i in str:
		if i.isdigit():
			empty.append(int(i))
	return sum(empty)
print(number_search('jisf 2 jfhud 43 fh3 34 fh'))
print(number_search('1 2 3 4 5 6 7 8 9'))
print

# difference between the two times
from datetime import datetime
# it doesn't follow any rules of am or pm
def hours_minutes_seconds_count(time1, time2):
	date_format = '%m-%d-%Y %H:%M:%S' # special format for representing date
	t1 = datetime.strptime(time1, date_format)
	t2 = datetime.strptime(time2, date_format)
	diff = t2 - t1
	#days = diff.days
	#days_to_hours = str(days * 24)
	#diff_two_times = str(diff.seconds / 3600)
	#overall_hours = str(days_to_hours + diff_two_times)
	hours = str((diff.seconds / 3600)) # for hours divide by 3600
	minutes = str(diff.seconds / 60) # for minutes divide by 60
	seconds = str(diff.seconds) # datetime has 'seconds' option
	return hours, minutes, seconds
print(hours_minutes_seconds_count('8-01-2008 00:00:00', '8-02-2008 01:30:00'))
print(hours_minutes_seconds_count('4-02-2017 00:00:00', '4-02-2017 04:45:00'))
print

# matrix operations
def matrix_operations(x,y):
	resM = [[0,0],
			[0,0]]
	resT = [[0,0],
			[0,0]]
	resA = [[0,0],
			[0,0]]
	resS = [[0,0],
			[0,0]]
	for i in range(len(x)):
		for j in range(len(y[0])):
			for k in range(len(y)):
				resM[i][j] += x[i][k] * y[k][j]
	for i in range(len(x)):
		for j in range(len(y[0])):
			resA[i][j] = x[i][j] + y[i][j]
	for i in range(len(x)):
		for j in range(len(y[0])):
			resS[i][j] = x[i][j] - y[i][j]
	for i in range(len(resM)):
		for j in range(len(resM[0])):
			resT[i][j] = resM[j][i]
	return resA, resS, resM, resT
print(matrix_operations([[1,2],[3,4]],[[1,2],[3,4]]))
print

# fibonacii series
def fib(last_term):
	first_term = 0
	second_term = 1
	nth = 0
	fib_empty = [0,1]
	for count in range(last_term - 2):
		nth = first_term + second_term
		fib_empty.append(nth)
		first_term = second_term
		second_term = nth
	return fib_empty
print(fib(25))

# a number part of fibonacii sequence
def n_in_fib(num, last_term): # last_term is the nth term of the fibonacii sequence
	if num in fib(last_term):
		return 'i want to earn billions'
	else:
		return 'nope'
print(n_in_fib(21, 25))
print(n_in_fib(333, 32))
print(n_in_fib(2, 54243))
print

# pluralizing the word
import re
def pluralize(noun):
	if re.search('[sxz]$',noun): # indicates the alphabet that should be matched accordance with the noun in the collection from the end
		return re.sub('$','es',noun)
	elif re.search('[^aeioudgkprt]h$',noun): # indicates the alphabet not in the collection 'aeioudgkprt' before 'h' from the end
		return re.sub('$','es',noun)
	elif re.search('[^aeiou]y$',noun): # indicates the alphabet not in the collection of 'aeiou' before 'y' from the end
		return re.sub('y$','ies',noun)
	else:
		return noun + 's'
print(pluralize('sjhbdksnseerucy'))
print(pluralize('shdgdph'))
print(pluralize('sgdhsggs'))
print(pluralize('c'))
print

#validating a phone_number
def telephone_number_check(phone_number):
	pattern = re.compile(r'''
		# does not match the begining
	(\d{3}) # matches the number
	\D* # ignores special characters
	(\d{3}) # matches the number
	\D* # ignores special characters
	(\d{4}) # matches the number
	\D* # ignores special characters
	(\d*) # matches the extension
	$ ''', re.VERBOSE) # VERBOSE is mainly used to add comments in between the expression as shown in the code
	return pattern.search(phone_number).groups() # groups() method returns the output in tuple
print(telephone_number_check('(646)-+739+=-3489///3875'))
print(telephone_number_check('jbfdhygfef 1=63725673472537'))
print

# returning the number which repeats consecutively in bothe the arguments
def triple_double(arr1, arr2):
	repeatition = []
	for i in arr1:
		if i in arr2:
			repeatition.append(i)
	for j in arr2:
		if j in arr1:
			repeatition.append(j)
	return list(set(repeatition))
print(triple_double([1,2,3,4,4],[4,5,1,2,3,6,7]))
print(triple_double([1,1,1,1,2],[2,2,2,2,1]))
print

#look say sequence
# NOTE : let the sequence follow the progression rules
def look_say(arr):
	if len(arr) == 0:
		return 'nil'
	for i in range(len(arr)):
		if arr[i + 1] - arr[i] == arr[i - 1] - arr[i - 2]:
			common = arr[1] - arr[0]
			next_term = arr[-1] + common
			return 'Arithematic progression ---> ' + str(next_term)
		elif arr[i + 1] / arr[i] == arr[i - 1] / arr[i - 2]:
			common_ratio = arr[1] / arr[0]
			next_ratio = arr[-1] * common_ratio
			return 'Geometric progression ---> ' + str(next_ratio)
		else:
			return 'nope'
print(look_say([1,3,5,7,9]))
print(look_say([2,2**2,2**3,2**4,2**5]))
print(look_say([1,2,4,5,6,3,2,2]))
print(look_say([]))
print

