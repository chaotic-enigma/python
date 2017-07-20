# reversing a string
def reverse_string(str):
	return str[::-1]
print(reverse_string('i want to earn billions'))
print 

# factorial of a number
def factorial(num):
	fact = 1
	ele = 1
	while (ele <= num):
		fact *= ele
		ele += 1
	return fact
print(factorial(5))
print 

# palindrome of string
def palindrome(str):
	rev_str = str[::-1]
	if rev_str == str:
		return "palindrome"
	else:
		return "not palindrome"
print(palindrome('333'))
print(palindrome('234'))
print

# find the longest word
def find_longest_word(str):
	split_string = str.split(' ')
	#print split_string
	nutshell = []
	for i in split_string:
		nutshell.append(len(i))
	long = sorted(nutshell)
	longest_word = long[::-1]
	return longest_word[0]
print(find_longest_word('i want to earn billions'))
print

# test case
def test_case(str):
	lower = str.lower()
	title = lower.title()
	return title
print(test_case('i want to earn billions'))
print

# longest array --length
def longest_array(arr):
	individual = []
	for i in arr:
		individual.append(len(i))
	sort = sorted(individual)
	desc_sort = sort[::-1]
	return desc_sort[0]
print(longest_array([[1,2,3,4],[2,3,4,5,6,7],
	["saf","hds","jdd","chd","jdh","dwe","dew"]]))
print

"""# longest array based on value
def longest_value(arr):
	#bada = [0,0,0,0]
	for i in range(0,len(arr)):
		i += 1
		for j in i:
			j += 1
	return j
print(longest_value([[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,7]]))"""

# repeatition of string
def repeat_exam(str,num):
	if(num != 0):
		return str * num
print(repeat_exam('i want to earn billions--',3))
print

# mutation
def mutation(arr):
	hakuna = arr[1]
	matata = arr[0]
	for i in range(0, len(matata)):
		if (matata[i] == hakuna[i]):
			return 'i want to earn billions'
		else:
			return False
print(mutation([["hello"],["hello"]]))
print(mutation([['sameer'],['loophole']]))
print

# confirming the end
def end_test(str,target):
	if str[-len(target):] == target:
		return True
	else:
		return False
	#print('hdhdhdhhd'[-4:])
print(end_test('i want to earn billions','billions'))
print(end_test('whdudbcudjss','gdhsdt'))
print

# partition of an array according to the size
def chunky_monkey(arr,size):
	new_arr = []
	i = 0
	while (i < len(arr)):
		new_arr.append(arr[i:i+size])
		i += size
	return new_arr
print(chunky_monkey([0,1,2,3,4,5],4))
print(chunky_monkey([1,2,3,4,4,5,6,7,8],3))
print

# splicing the array
def splice_array(arr,how_many):
	splice = arr[how_many:]
	return splice
print(splice_array([1,2,3,4,5,6],4))
print(splice_array([8,7,6,5,4,3,2,6,4,3,7,5,4,2],4))
print

# truncatioin
def truncate(str,num):
	if (len(str) > num and num > 3):
		return str[0:num-3] + '...'
	elif (len(str) > num and num <= 3):
		return str[0:num] + '...'
	else:
		return str
print(truncate('i want to earn billions',12))
print(truncate('earn billions:  i want to',18))
print

# chunk array in groups
def chunk_array_in_groups(arr,size):
	simply = []
	just = []
	temp = arr
	result = []
	for i in range(0,size):
		simply.append(arr[0:size])
	result.append(simply[0])
	for i in range(0,size):
		just.append(temp[2:len(temp)])
	result.append(just[0])
	return result
print(chunk_array_in_groups([1,2,3,4,5,6],5))
print

# get the index
def get_index(arr,num):
	arr = sorted(arr)
	for i in range(0,len(arr)):
		if arr[i] >= num:
			return i
		else:
			pass
print(get_index([1,2,3,4,5],1))
print(get_index([-2,-1,0,1,2,3,4],4))
print

# ascii conversion
def string_ascii(str):
	asc = []
	s_a = list(str)
	for i in s_a:
		asc.append(ord(i))
	return asc
print(string_ascii('abcdefghijklmnopqrstuvwxyz'))
print(string_ascii('i want to earn billions!'))
print

# string conversion
def ascii_string(num):
	n = []
	for i in num:
		n.append(chr(i))
	return ''.join(n)
print(ascii_string([105, 32, 119, 97, 110, 116, 32, 116, 111, 32, 101, 97, 114, 110, 32, 98, 
	105, 108, 108, 105, 111, 110, 115, 33]))
print

# searching for name
def search_engine(text,search):
	my_search = search
	return text.find(my_search)
print(search_engine('jnjhfu jdihfudsfh i want to earn billions hgugydb dusydgdsy','i want to earn billions'))
print

# array destroyer
def array_destroyer(arr1,arr2):
	ground_nut = []
	for i in arr1:
		if i not in arr2:
			ground_nut.append(i)
	return ground_nut
print(array_destroyer([1,2,3,4,5,6,7,'jdhjhf'],[1,2,3]))
print

# substrings .. return only last letter of any string
def sub_string(str):
	return str[len(str)-1:len(str)]
print(sub_string('i want to earn billions'))
print(sub_string('loophole'))
print

# confirmation
def confirm_letter(str,target):
	if target in str:
		return 'i want to earn billions'
	else:
		pass
print(confirm_letter('i want to earn billions','b'))
print

def password_check(str, password):
	if str == password:
		return 'successfully logged in'
	else:
		return 'nope'
print(password_check('google','google'))
print
