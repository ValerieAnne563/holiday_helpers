sample_data = [1000,
2000,
3000,
None,
4000,
None,
5000,
6000,
None,
7000,
8000,
9000,
None,
10000]

"""
This list represents the Calories of the food carried by five Elves:

The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
The second Elf is carrying one food item with 4000 Calories.
The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
The fifth Elf is carrying one food item with 10000 Calories.
In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know how many Calories are being carried by the Elf carrying the most Calories. In the example above, this is 24000 (carried by the fourth Elf).

Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
"""

class State:
	def __init__(self):
		self.elf_count = 0

		self.current_cal_count = 0

		self.max_elf = -1
		self.elf_max = 0
		self.top_three = [-1, -1, -1]

	def finalize(self):
		self.elf_count += 1
		if self.current_cal_count > self.elf_max:
			self.elf_max = self.current_cal_count
			self.max_elf = self.elf_count

		min_index = self.top_three.index(min(self.top_three))
		if self.current_cal_count > self.top_three[min_index]:
			self.top_three[min_index] = self.current_cal_count

		print("Elf %d: Total was %s. Max is: %s %s" % (self.elf_count, self.current_cal_count, self.elf_max, self.top_three))
		self.current_cal_count = 0

	def entry(self, line):
		if line is None or line == "":
			self.finalize()
		else:
			self.current_cal_count += int(line)

	def done(self):
		state.finalize()
		print("Max elf is %d with %d calories" % (self.max_elf, self.elf_max))
		print("Top Three: %s, sum: %d" % (self.top_three, sum(self.top_three)))


state = State()
with open("input_01.txt") as input_file:
	for line in input_file.readlines():
		state.entry(line.strip())
# for line in sample_data:
# 	state.entry(line)
state.done()

