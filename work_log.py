import csv
import datetime

def print_csv():
	with open('tasks.csv', newline='') as csvfile:
		task_reader = csv.reader(csvfile, delimiter=",")
		rows = list(task_reader)
		for row in rows:
			print(row)

def write_csv_header():
	with open('tasks.csv', 'a') as csvfile:
		fieldnames = ['date', 'name', 'minutes', 'notes']
		taskwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

		taskwriter.writeheader()

def write_csv(name, minutes, notes):
	with open('tasks.csv', 'a') as csvfile:
		fieldnames = ['date', 'name', 'minutes', 'notes']
		taskwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

		taskwriter.writeheader()
		taskwriter.writerow({
			'date': datetime.datetime.now(),
			'name': name,
			'minutes': minutes,
			'notes': notes
		})

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

# work_log()
write_csv_header()