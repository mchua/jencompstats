# Math topics
# ---------------
# max
# min
# mean
# mode
# median

# Code topics
# ---------------
# variables
# indentation
# order of operations
# functions
# if/else statements
# lists and list indexing
# modular arithmetic (%)
# the difference between integers and floats (decimals) to a computer

# Give this function a list of numbers,
# And it will find the median.
# Example call: median([1,2,4,2,5])
def median(Lucy):
	# if Lucy
	if len(Lucy)%2 == 1:
		Lucy.sort()
		return Lucy[len(Lucy)/2]

	else:
		Lucy.sort()
		num1 = Lucy[len(Lucy)/2]
		num2 = Lucy[(len(Lucy)/2)-1]
		return (num1 + num2)/ 2.0
