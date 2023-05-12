#!/bin/bash
#Main developer: Emma Ford

status="y"
while [ $status = "y" ]; do
        echo "Password Squirrel"
        echo "Search Records"
        read -p "Enter service/username to search for: " searchterm
        count=$(sqlite3 PasswordSquirrel.db "SELECT COUNT(*) FROM Password_Data WHERE Service LIKE '%$searchterm%' COLLATE NOCASE OR Username LIKE '%$searchterm%' COLLATE NOCASE")
        if [ $count -eq 0 ]; then
                echo
                echo "No match found."
                sleep 2
        else
                echo
                echo "Matching record(s) found:"
                echo
                result=$(sqlite3 PasswordSquirrel.db "SELECT rowid, * FROM Password_Data WHERE Service LIKE '%$searchterm%' COLLATE NOCASE OR Username LIKE '%$searchterm%' COLLATE NOCASE ")
                echo "$result" | awk -F'|' '{printf "Record ID: %s\nService: %s\nUsername: %s\nPassword: %s\n\n", $1, $2, $3, $4}'
                sleep 2
        fi
        echo
        echo "Enter Y to search for another record."
        echo "Enter X to return to main menu."
        while true; do
                read -p "Enter choice: " reply
                if [[ $reply == [Yy] ]]; then
                        echo "Returning to search..."
                        echo
                        break
                elif [[ $reply == [Xx] ]]; then
                        echo "Returning to main menu..."
                        echo
                        status="n" ; break
                else
                        echo "Invalid choice. Try again."
                fi
        done
done
