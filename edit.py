#!usr/bin/python3
#	Primary author: Nicole Niesen

import sqlite3

connection = sqlite3.connect("PasswordSquirrel.db")
cVar = connection.cursor()

def edit(service):
	choice = input("Which field would you like to edit? Enter username or password: ").lower()
	if (choice == "username"):
		username = input("What is the new username? ")
		sql_update = """UPDATE password_data SET username = ? WHERE service = 
		?;"""
		cVar.execute(sql_update, (username, service))
		print("Your username has been updated. Redirecting to the menu...")
		connection.commit()
		connection.close()
	elif (choice == "password"):
		password = input("What is the new password? ")
		sql_update = """UPDATE password_data SET password = ? WHERE service = 
		?;"""
		cVar.execute(sql_update, (password, service))
		print("Your password has been updated. Redirecting to the menu...")
		connection.commit()
		connection.close()
	else:
		print("Please try again.")
		edit(service)
