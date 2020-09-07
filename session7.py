import random


# Question 1
def fibonacci_number(input_number):
	fibonacci=(lambda number: number if number <=1 else fibonacci(number -1) + fibonacci(number -2));
	listOffibonacci = list(map(fibonacci, range(0,22,1)))
	if input_number in listOffibonacci:
		return True
		#print('Fibonacci no.',input_number)
	#else:
		#print('Not Fibonacci no.')

# for i in range(10000):
# 	fibonacci_number(i)

# Questiom 2.1 (add iterbles)
# Q2.1. Using list comprehension (and zip/lambda/etc if required) write an expression that
#       add 2 iterables a and b such that a is even and b is odd
def add_even_odd(in_list1 = list, in_list2 = list)->list:
	'''
	This function adds 2 iterables a and b such that a is even and b is odd
	The input should be a list of numbers.
	The function returns list with addition as per the above mentioned rule
	'''
	final_list = list(filter(None,[a+b if a%2==0 and b%2!=0 else 0 for a,b in zip(in_list1,in_list2)]))
	return final_list


# Question 2.2 (vowel)
def removevowel(input):
	return ''.join([i for i in input if i not in 'aeiou'])

# Question 2.3
def relu_array(input_list):
	return [x if x > 0 else 0 for x in input_list]

# Question 2.4
import math
def sigmoid_array(input_list):
	return [(1.0 / (1.0 + math.exp(-x))) if x>=0 else (math.exp(x) / (1.0 + math.exp(x))) for x in input_list]
#sigmoid([1,2,5,-3,-2,-1,0,2,3])

# Question 2.5
import string
def shift_string(mystring,shift):
	return ''.join([ chr(ord(c)+shift) if c in alph_string else c for c in mystring])

# Question 3
def check(sentence, words): 
	res = [] 
	for substring in sentence.split():
		[res.append(w) for w in words if w == substring]
	return res

# Question 3 helper
# Example of getting file content
def getFileContent(pathAndFileName):
	with open(pathAndFileName, 'r') as theFile:
		# Return a list of lines (strings)
		data = theFile.read().split('\n')
		return data

# data =getFileContent('D:\study\EPai\session7-mayankSharma\list.txt')
# paragraph = 'may be you to yes be bestial love me come sex bitch  boob fucker ere jake aaja'
# r = check(paragraph, data)
# len(r) == True

# Question 4.a
from functools import reduce
import operator
def add_even(lst):
	return functools.reduce(operator.add, [i for i in lst if i%2 == 0])

# Q4.b. Using reduce function - find the biggest character in a string (printable ascii characters)
def biggest_character(in_str = str)->str:
	'''
	This function finds the biggest character in a string (printable ascii characters)
	The input should be a string containing printable ascii characters.
	The function returns the biggest character in the provided string
	'''
	if not isinstance(in_str,str):
		raise TypeError("Only strings allowed as input")

	return reduce(lambda a,b: a if ord(a)>ord(b) else b,in_str)

# Question 4.3
def add_every_third(lst):
	return reduce(operator.add, lst[2::3])

# Q5. Using randint, random.choice and list comprehensions, write an expression that 
#     generates 15 random KADDAADDDD number plates, where KA is fixed, D stands for a digit
#     and A stands for Capital alphabets. 10<<DD<<99 & 1000<<DDDD<<9999
def num_plate_generator()->list:
	'''
	This function that generates 15 random number plates starting with KA (for Karnataka)
	The function doesn't take any input
	The function returns list of 15 random number plates starting with KA
	'''
	num = ['KA'+str(a)+str(b1)+str(b2)+str(c) for a,b1,b2,c in zip(random.sample(list(range(10,100)),15),
                                                                   random.sample(list(map(chr, (range(65,91)))),15),
                                                                   random.sample(list(map(chr, (range(65,91)))), 15),
                                                                   random.sample(list(range(1000, 10000)),15))]
	return num

# Q6.a. Write the above again from scratch where KA can be changed to DL
#       and 1000/9999 ranges can be provided.
def num_plate_generator_scratch(start=int,end=int,statepin=str)->list:
    '''
    This function that generates 15 random number plates for the state code provided
    and the vehicle number between the range provided
    The function takes 3 inputs:
        num_start: The least number allowed as vehicle number
        num_end: The highest number allowed as vehicle number
        state_code: Code of the state for which the number plate is to be generated
    The function returns list of 15 random number plates based on the inputs
    '''
    if not isinstance(start,int):
        raise TypeError("Only integeres allowed as minimum number")

    if not isinstance(end,int):
        raise TypeError("Only integeres allowed as maximum number")

    if not isinstance(statepin,str):
        raise TypeError("Only strings allowed as input")

    if statepin not in ['AN','AP','AR','AS','BR','CG','CH','DD','DL','GA','GJ','HP','HR','JH','JK','KA','KL','LA','LD','MH','ML','MN','MP','MZ','NL','OD','PB','PY','RJ','SK','TN','TR','TS','UK','UP','WB']:
        raise ValueError("Only following State codes are allowed: AN, AP, AR, AS, BR, CG, CH, DD, DL, GA, GJ, HP, HR, JH, JK, KA, KL, LA, LD, MH, ML, MN, MP, MZ, NL, OD, PB, PY, RJ, SK, TN, TR, TS, UK, UP, WB")

    if len(statepin)!=2:
        raise ValueError("State code must have only 2 characters")

    num = [statepin + str(a) + str(b1) + str(b2) + str(c) for a,b1,b2,c in zip(random.sample(list(range(10,100)),15),
                                                                random.sample(list(map(chr,(range(65,91)))),15),
                                                                random.sample(list(map(chr,(range(65,91)))),15),
                                                                random.sample(list(range(start,end+1)),15))]
    return num

# Q6.b. Now use a partial function on top of above function such that 1000/9999 are hardcoded, but KA can be provided
