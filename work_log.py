def work_log():
	while True:
		user_input = input("Would you like to create a new entry(c), or look up old ones(L) c/L ? ")
		if user_input == 'c':
			print("Create")
			break
		elif user_input == 'L':
			print("Look up")
			break
		else:
			print("That is not a valid response")

work_log()