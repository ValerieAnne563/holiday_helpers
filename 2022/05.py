"""
https://adventofcode.com/2022/day/5
"""

"""
needed supplies are buried under many other crates, 
the crates need to be rearranged.

To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top of each stack.

The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.

They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). For example:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.

Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 
In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates:

        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3
Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below crate M:

        [Z]
        [N]
[M]     [D]
[C]     [P]
 1   2   3
Finally, one crate is moved from stack 1 to stack 2:

        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3
The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.

After the rearrangement procedure completes, what crate ends up on top of each stack?
"""

# Number of characters each "stack" takes up in an input line
CRATE_PARSE_WIDTH = 4

sample_input = [
"    [D]    ",
"[N] [C]    ",
"[Z] [M] [P]",
" 1   2   3 ",
"",
"move 1 from 2 to 1",
"move 3 from 1 to 3",
"move 2 from 2 to 1",
"move 1 from 1 to 2"]

def pretty_print_stacks(stacks):
	for i, stack in enumerate(stacks):
		print("%d %s" % (i + 1, stack))

stacks = [[]]
stack_built = False
with open("input_05.txt") as f:
	data = f.readlines()

	for line in data:
		line = line.replace('\n', '')
		if "[" in line:
			# Parsing the diagram
			num_stacks = (len(line) + 1) / CRATE_PARSE_WIDTH

			if num_stacks > len(stacks):
				print("Resizing max_stacks: %d" % num_stacks)
				stacks += [[]] * (num_stacks - len(stacks))

			# s identifies the stack number,
			# i identifies the starting character of the quartet
			for s, i in enumerate(range(0, len(line), CRATE_PARSE_WIDTH)):
  				stack_i = line[i:i+4]
  				if stack_i.strip() != "":
  					crate_id = stack_i[1]
  					# print(s + 1, crate_id)
  					stacks[s] = [crate_id] + stacks[s]
  		else:
  			if not stack_built:
  				print("Done building stacks:")
  				# pretty_print_stacks(stacks)
  				stack_built=True

  			if line.startswith("move"):
  				_, n, _, src, _, dest = line.split(' ')
  				src = int(src) - 1
  				n = int(n)
  				dest = int(dest) - 1
  				# print("===================")
  				# print(line)

  				cargo = stacks[src][-1 * n:]
  				# print("CARGO: %s" % cargo)
  				# cargo.reverse()
  				stacks[dest] += cargo

  				new_len = len(stacks[src]) - n
  				stacks[src] = stacks[src][0:new_len]
  				# pretty_print_stacks(stacks)

# Parsing and moving is done
# pretty_print_stacks(stacks)  	
print("Top of each stack: %s" % 
	''.join(stack[-1] for stack in stacks))
