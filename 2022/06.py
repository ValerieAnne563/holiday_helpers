"""
https://adventofcode.com/2022/day/6
"""

test_examples = [
	"bvwbjplbgvbhsrlpgdmjqwftvncz", # first marker after character 5
	"nppdvjthqldpwncqszvftbrmjlhg", # first marker after character 6
	"nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", # first marker after character 10
	"zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", # first marker after character 11
]

def find_unique_sequence(transmission, n):
	"""
	Find the first sequence of n characters where all
	characters are unique.
	"""
	for i in range(len(transmission) - n):
		quad = transmission[i:i+n]
		if len(set(quad)) == n:
			return i + n

# for t in test_examples:
# 	print(find_sop(t))

with open("input_06.txt") as f:
	transmission = f.read()
	print("First Start of Packet marker is after character: %d" %
		   find_unique_sequence(transmission, 4))
	print("First Start of Packet marker is after character: %d" %
			   find_unique_sequence(transmission, 14))