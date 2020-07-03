from random import randint, randrange

nums = []
for i in range(randrange(2, 10)):
	nums.append(randint(0,10))
nums = tuple(nums)

print(f'Length {len(nums)} of tuple {nums}')