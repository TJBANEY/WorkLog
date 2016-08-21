def work_log():
	while True:
		user_input = input("Would you like to create a new entry(c), or look up old ones(L) c/L ? ")
		if user_input == 'c':
			create_new_task()
			break
		elif user_input == 'L':
			search_task()
			break
		else:
			print("That is not a valid response")

def create_new_task():
	task_name = input("Enter a task name: ")
	minutes_spent = input("Enter minutes spent on task: ")
	notes = input("Enter any additional notes about the task: ")

def search_task():
	while True:
		search_filter = input("Search for tasks by date(d), time spent on task(t), pattern(p), or keyword search(k): ")
		if search_filter == 'd':
			print("Date")
			break
		elif search_filter == 't':
			print("Time Spent")
			break
		elif search_filter == 'p':
			print("Pattern")
			break
		elif search_filter == 'k':
			print("Keyword")
			break
		else:
			print("Not a valid selection")


work_log()