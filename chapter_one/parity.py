from test_framework import generic_test


def parity(x: int) -> int:
	pass


if __name__ == "__main__":
	exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))