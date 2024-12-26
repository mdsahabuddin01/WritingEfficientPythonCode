Using %timeit: your turn!
You'd like to create a list of integers from 0 to 50 using the range() function. However, you are unsure whether using list comprehension or unpacking the range object into a list is faster. Let's use %timeit to find the best implementation.

For your convenience, a reference table of time orders of magnitude is provided below (faster at the top).

symbol	name	unit (s)
ns	  nanosecond	10-9
µs   (us)	microsecond	10-6
ms	  millisecond	10-3
s	    second	100

# Create a list of integers (0-50) using list comprehension
nums_list_comp = [num for num in range(51)]
print(nums_list_comp)

# Create a list of integers (0-50) by unpacking range
nums_unpack = [*(nums_list_comp)]
print(nums_unpack)

%timeit [num for num in range(51)]

%timeit [*(range(51))]

# Create a list using the formal name
formal_list = list()
print(formal_list)

# Create a list using the literal syntax
literal_list = []
print(literal_list)

# Print out the type of formal_list
print(type(formal_list))

# Print out the type of literal_list
print(type(literal_list))
