from test_framework import generic_test
import math

def integer_palindrome(x: int) -> bool:
	"""
	check if the number can be read the same forwards or backwards if it was a string
	cop out is to automatically jump to converting to string
	:param x:
	:return:
	"""
	if x < 0:
		return False
	if 0 <= x < 10:
		return True

	# reverse the int and if they're equal at some midpoint? kind of only works for even digit strings
	res, remainder = 0, x

	while remainder:
		res *= 10
		res += remainder % 10
		remainder //= 10

	# book also outlines a different method that does math work
	digit_count = math.floor(math.log10(x)) + 1 #
	most_sig_digit_mask = 10 ** (digit_count - 1)

	for i in range(digit_count // 2):
		if x // most_sig_digit_mask != x % 10:
			return False
		x %= most_sig_digit_mask # remove leading digit
		x //= 10 # removing trailing digit
		most_sig_digit_mask //= 100

	return True


if __name__ == "__main__":
	print(integer_palindrome(3))
	print(integer_palindrome(-1))
	print(integer_palindrome(100))
	print(integer_palindrome(32123))
	exit(generic_test.generic_test_main('palindrome_integer.py', 'is_number_palindromic.tsv', integer_palindrome))
