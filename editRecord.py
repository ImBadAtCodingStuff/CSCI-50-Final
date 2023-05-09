#!usr/bin/python3
#	Primary author: Nicole Niesen

import sqlite3
import edit

connection = sqlite3.connect("PasswordSquirrel.db")
cVar = connection.cursor()

result = ""
while (len(result) == 0):
	service = input("What service would you like to edit? ")
	sql_select = """SELECT * FROM password_data WHERE service = ?;"""
	cVar.execute(sql_select, (service,))
	result = cVar.fetchall()
	if (len(result) > 0):
		break
	else:
		print("No records found for that record.")
		choice = input("Would you like to search again? Y/N: ").lower()
		if (choice == "n"):
			connection.commit()
			connection.close()
			break

if (len(result) > 0):
        for i in result:
                print(i)
        edit.edit(service)
