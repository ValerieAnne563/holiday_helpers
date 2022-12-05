"""
Solutions for:
https://adventofcode.com/2022/day/3
https://adventofcode.com/2022/day/3#part2
"""

PRIORITY_a = 1
PRIORITY_A = 27

test_rucks = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw"
]

def priority(item):
	"""
	Lowercase item types a through z have priorities 1 through 26.
	Uppercase item types A through Z have priorities 27 through 52.

	:param char item: an alphabetical character [a-zA-Z]
	"""
	i = ord(item)
	if i >= ord('a'):
		assert i <= ord('z')
		return i - ord('a') + PRIORITY_a
	elif i <= ord('Z'):
		assert i >= ord('A')
		return i - ord('A') + PRIORITY_A

	raise Exception("Invalid character: %s" % item)


def split_and_diff(rucksack):
	"""
	Find the common characters between the first half of the string and the 2nd
	"""
	assert len(rucksack) % 2 == 0
	halfway = len(rucksack) / 2

	return set(rucksack[0:halfway]).intersection(set(rucksack[halfway:]))


item_type_sum = 0
badges_sum = 0
with open('input_03.txt') as f:
	sets = []
	
	# for rucksack in test_rucks:
	for line in f.readlines():
		rucksack = line.strip()

		# Problem 1
		matches = split_and_diff(rucksack)
		for m in set(matches):
			# print(m, priority(m))
			item_type_sum += priority(m)

		# Problem 2
		sets += [set(rucksack)]
		if len(sets) == 3:
			# print(sets[0], sets[1], sets[2])
			badge = sets[0].intersection(sets[1]).intersection(sets[2])
			badges_sum += priority(badge.pop())
			sets = []


print("Item Type Sum: %s" % item_type_sum)
print("Badge Sum: %s" % badges_sum)