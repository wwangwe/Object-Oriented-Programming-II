print(
"""
	TEMPERATURE CONVERTER
F --> to Farenheit or C --> to Celius
"""
)
# following the F=formula : c/5 = (f-32)/9
def to_celcius():
	temp = int(input("Temperature: "))
	celc = (temp - 32)*(5/9)
	
	print(f'{temp}F = {celc:.2f}°C')

def to_farenheit():
	temp = int(input("Temperature: "))
	faren = ((9/5)*temp + 32)

	print(f'{temp}°C = {faren:.2f}F')

def start():
	choice = str(input("Convert to: "))

	if choice.upper() == 'F':	
		to_farenheit()
		again = str(input("Convert again? (y/n): "))
		if again.lower() == 'y': start()

	elif choice.upper() == 'C':
		to_celcius()
		again = str(input("Convert again? (y/n): "))
		if again.lower() == 'y': start()

	else:
		print("Please Enter F or C")
		start()
start()
