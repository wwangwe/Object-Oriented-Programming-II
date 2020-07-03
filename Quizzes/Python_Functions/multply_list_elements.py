nums = [2, 4, 5, 10]
mult = 1

def incest(lst):
	global mult

	for el in lst:
		mult = el * mult

	print(f'Sum: {mult}')

incest(nums)

# mult is initialized/populated with one(1) 
# because muiltiplying 1 with any of the
# elements doesn't affect the values
# Called *global* because mult is outside function