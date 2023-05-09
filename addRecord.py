#!usr/bin/python3
#	Primary Author: Nicole Niesen
import sqlite3
import edit

connection = sqlite3.connect("PasswordSquirrel.db")
cVar = connection.cursor()

service = input("For what service would you like to add a password? ")

sql_select = """SELECT * FROM password_data WHERE service = ?;"""
cVar.execute(sql_select, (service,))
result = cVar.fetchall()
if (len(result) == 0):
	username = input("What is the associated username? ")
	password = input("What is the password you would like to store? ")
	sql_insert = """INSERT INTO password_data VALUES (?, ?, ?);"""
	cVar.execute(sql_insert, (service, username, password))
	print("Your entry was saved")
	connection.commit()
	connection.close()
else:
	print("This service already has a username and password associated with it")
	for i in result:
		print(i)
	action = input("Would you like to edit this record? Y/N ").lower()
	if action == "y":
		connection.commit()
		connection.close()
		edit.edit(service)
	else:
		print("Redirecting to the main menu...")
		connection.commit()
		connection.close()

