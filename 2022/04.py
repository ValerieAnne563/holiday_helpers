"""
https://adventofcode.com/2022/day/4
"""

test_input = [
	"2-4,6-8",
	"2-3,4-5",
	"5-7,7-9",
	"2-8,3-7",
	"6-6,4-6",
	"2-6,4-8"]

fully_contains = overlaps = 0

with open('input_04.txt') as f:
	# for pair in test_input:
	for line in f.readlines():
		pair = line.strip()

		range1, range2 = pair.split(',')
		elf1 = [int(i) for i in range1.split('-')]
		elf2 = [int(i) for i in range2.split('-')]

		# Check for full containment
		# Assumes each range is ascending.
		# Does elf1's assignment fully contain elf2's?
		if elf1[0] <= elf2[0] and elf1[1] >= elf2[1]:
			fully_contains += 1
		elif elf2[0] <= elf1[0] and elf2[1] >= elf1[1]:
			fully_contains += 1

		# Check for full or partial overlap
		if elf1[0] == elf2[0]:
			# Both elves ranges start at the same spot
			overlaps += 1
		elif elf1[0] < elf2[0] and elf1[1] >= elf2[0]:
			# Elf1 range starts below Elf2's range, but ends in or above it
			overlaps += 1
		if elf2[0] < elf1[0] and elf2[1] >= elf1[0]:
			# Elf2 range starts below Elf1's range, but ends in or above it
			overlaps += 1
			

print("Fully contained pairs: %d" % fully_contains)
print("Overlapping pairs: %d" % overlaps)

