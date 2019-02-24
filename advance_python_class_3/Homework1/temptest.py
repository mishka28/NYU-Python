#!/usr/bin/env python3

# sequence = []
defence = 0.4
for x in range(1):	
	print(x)

for x in range(10):
	if x == 0:
		defence = defence
	else:
		defence = defence + (1 - defence) * (1 / 2)
print(defence)
# print(defence)	
# print(sequence)
# print(sum(sequence))

# x = input()
# print(x)