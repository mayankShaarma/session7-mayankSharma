import pytest
import session7
import os
import inspect
import re
import importlib


FUNCTIONS_TO_CHECK_FOR = [
    'fibonacci_number',
    'add_iter_even_odd',
    'vowel_remover',
    'relu',
    'sigmoid',
    'char_shifter',
    'profanity_checker',
    'even_adder',
    'biggest_character',
    'alt_adder',
    'num_plate_generator',
    'num_plate_generator_2',
    'num_plate_generator_3'
]

CHECK_FOR_WORDS = [
    'Map',
    'Zip',
    'List comprehensions',
    'Reduce',
    'Partial',
    'Lambda',
    'Filter'
]

### test README file ###
#53
def test_function_name_had_cap_letter():
	functions = inspect.getmembers(session5, inspect.isfunction)
	for function in functions:
		assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

#54
def test_indentations():
	''' Returns pass if used four spaces for each level of syntactically \
	significant indenting.'''
	lines = inspect.getsource(session5)
	spaces = re.findall('\n +.', lines)
	for space in spaces:
		assert len(space) % 4 == 2, "Your script contains misplaced indentations"
		assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

#55
def test_all_functions_exist():
	code_lines = inspect.getsource(session5)
	for word in CHECK_FOR_FUNCTIONS:
		assert word in code_lines, 'Have you heard of Pinocchio?'

#56
def test_readme_exists():
	assert os.path.isfile("README.md"), "README.md file missing!"

#57
def test_readme_contents():
	readme = open("README.md", "r")
	readme_words = readme.read().split()
	readme.close()
	assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

#58
def test_readme_file_for_formatting():
	f = open("README.md", "r", encoding="utf-8")
	content = f.read()
	f.close()
	assert content.count("#") >= 10

#59
def test_readme_proper_description():
	READMELOOKSGOOD = True
	f = open("README.md", "r", encoding="utf-8")
	content = f.read()
	f.close()
	for c in CHECK_FOR_WORDS:
		if c not in content:
			READMELOOKSGOOD = False
			pass
	assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_function_are_listed():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    AllFUNCTIONSDEFINED = True
    for c in FUNCTIONS_TO_CHECK_FOR:
        if c not in content:
            AllFUNCTIONSDEFINED = False
            pass
    assert AllFUNCTIONSDEFINED == True, "You have not defined all the required functions"

# Check Q1 - fibonacci_number
def test_for_fab_no_true():
	assert session7.fibonacci_number(5) == True, "The fibonacci_number function does not work properly"

# Check Q1 - fibonacci_number
def test_for_fab_no_false():
	assert session7.fibonacci_number(7) == False, "The fibonacci_number function does not work properly"

# Check Q2 1- add_even_odd
def test_for_add_even_odd():
	assert session7.add_even_odd([1,2,3,5,8],[2,5,7,3,5,2]) == [7,13], "The add_even_odd function does not work properly"

# Check Q2.2 removevowel
def test_for_removevowel():
	assert session7.removevowel("removevowel") == "rmvvwl", "The removevowel function does not work properly"

# Check Q2. 3 relu_array
def test_relu_array():
	assert session7.relu_array([1,2,6,-4,-3,0,1]) == [1,2,6,0,0,0,1], "The relu_array function does not work properly"

# Check Q2 4 sigmoid_array
def test_for_sigmoid_array():
    assert session7.sigmoid_array([-2,-1,0,1,2]) == [0.12, 0.27, 0.5, 0.73, 0.88], "The sigmoid_array function does not work properly"

# Check Q2 5 test shift_string
def test_for_shift_string():
    assert session7.shift_string("abcd",4) == "efgh", "The shift_string function does not work properly"

# Check Q3 test check for truthiness
def test_for_profanity_checker_true():
    test_string = '''
    Oh Shit, there is something wrong with this paragraph.
    There are many methodologies that deal with the portion of CLV associated with direct purchases, but the two most broad classes are generally defined as historical and predictive CLV. Historical methods look at past data and make a judgment on the value of customers solely based on past transactions, without any attempt to predict what those customers will do next.
    In principle, this is a valid approach if the customers behave similarly and have been interacting with the company for roughly the same amount of time. However, there’s generally a fair amount of heterogeneity among customers. Typical historical approaches will apply a recency of last purchase criterion to distinguish between active and inactive users. Average past purchase behavior is employed to measure the relative (or in some cases, absolute) value of customers.
    However, there are several problems with such methodologies. For example, the first customer in the chart above has made more purchases than the second customer, but in fact, the first customer is more likely to be inactive than the second one. Value based on past averages would claim that the first customer is more valuable — yet the second customer is still active and could make many more purchases in the future. Methods that account for variation in the behavior of customers will allow us to arrive at more accurate conclusions about customer lifetime and purchase behavior.
    '''
    assert session7.check(test_string) == True, "The check function does not work properly"

# test even_adder
def test_for_even_adder():
    assert session7.even_adder([1,2,3,4,5,6]) == 12, "The even_adder function does not work properly"

# test biggest_character
def test_for_biggest_character():
    assert session7.biggest_character("abcd!ABCD|") == "|", "The biggest_character function does not work properly"

# test alt_adder
def test_for_alt_adder():
    assert session7.alt_adder([1,2,3,4,5,6]) == 9, "The alt_adder function does not work properly"

# Q.6 Check test num_plate_generator
def test_for_num_plate_generator():
	