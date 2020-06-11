
print(
"""
  GRADING SYSTEM
(enter q to quit)
"""
	)
def start():
	score = input("Enter Score: ")

	if score.lower() == 'q':
		pass
	else:
		score = int(score)
		if score in range(70, 100):
			print("Grade: A")
			start()
		elif score in range(60, 69):
			print("Grade: B")
			start()
		elif score in range(50, 59):
			print("Grade: C")
			start()
		elif score in range(40, 49):
			print("Grade: D")
			start()
		elif score <= 39:
			print("Grade: E (Failed)")
			start()
		else:
			print("Please enter a number between 0 - 100")
			start()
start()
