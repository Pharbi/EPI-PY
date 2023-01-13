from test_framework import generic_test
def reverse_digits(x: int) -> int:
	"""
	best way to reverse digits is to get the least significant digit of the full number, so get the remainder of
	x % 10, and so on while x
	:param x:
	:return:
	"""

	res = 0
	remainder = abs(x)

	while remainder:
		res = res * 10 + remainder % 10
		remainder //= 10

	return -res if x < 0 else res


if __name__ == "__main__":
	exit(generic_test.generic_test_main('reverse_digits.py', 'reverse_digits.tsv', reverse_digits))
