"""Given a list of numbers, stop processing input after the cumulative sum of all the input becomes negative."""

current = int(input())
sum = current
while sum>=0:
	print(current)
	current = int(input())
	sum += current
