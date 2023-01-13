from typing import List

from test_framework import generic_test


def reverse_bits(x: int) -> int:
	size = 16
	position = size - 1
	y = 0
	while position >= 0:
		y |= (x & 1) << position
		x >>= 1
		position -= 1

	return y


def create_bit_cache() -> List[int]:
	cache = []

	for i in range(0, 2 ** 16):
		cache.append(reverse_bits(i))

	return cache


def reverse_bits_with_cache(x: int) -> int:
	cache = create_bit_cache()
	mask_size = 16
	bit_mask = 0xffff  # 16 1's

	return (cache[x & bit_mask] << (3 * mask_size) |
	        cache[(x >> mask_size) & bit_mask] << (2 * mask_size) |
	        cache[(x >> (2 * mask_size)) & bit_mask] << mask_size |
	        cache[(x >> (3 * mask_size)) & bit_mask] & bit_mask)


if __name__ == "__main__":
	exit(generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv', reverse_bits_with_cache))

