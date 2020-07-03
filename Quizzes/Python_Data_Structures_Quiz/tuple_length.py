from random import randint, randrange

nums = []
for i in range(randrange(2, 10)):
	nums.append(randint(0,10))
nums = tuple(nums)

print(f'Length {len(nums)} of tuple {nums}')

# Randrange on line 4 sets a random length,
# btn 2 & 10, of our nums list

# Randint on line 5 populates the list with a
# random number btn 0 & 10