from test_framework import generic_test


def parity(x: int) -> int:
	res = 0

	while x:
		res ^= x & 1
		x >>= 1

	return res


def set_rightmost(x: int) -> int:
	return x | (x - 1)


def mod_power_of_two(x: int, y: int) -> int:
	return x & ~y


def is_power_of_two(x: int) -> int:
	return (x & (x - 1)) == 0


if __name__ == "__main__":
	# parity(855)
	# exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
	print(mod_power_of_two(77, 64))
	print(is_power_of_two(3))

