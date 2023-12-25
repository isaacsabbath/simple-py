def register():
	db = ("database.txt", "r")
	username = input("Enter your username: ")
	password = input("Enter your password: ")
	password1 = input("Enter your password: ")

	if password != password1:
		print("Enter passord again")
		register()
	else:
		if len(password) < 6:
			print("Enter too short, enter again")
			register()
		elif username id db:
			print("Username exists")
			register()
		else:
			db = open("database.txt", "a")
			db.write(username+","+password+"\n")
			print("Success!")

register()