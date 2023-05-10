#!/bin/bash

#MAIN SUBPROGRAM START
status="y"
clear
while [ $status = "y" ]; do
        echo "Password Squirrel"
        echo "Search Records"
        read -p "Enter name of service to search for: " searchterm
        count=$(sqlite3 PasswordSquirrel.db "SELECT COUNT(*) FROM Password_Data WHERE Service='$searchterm' COLLATE NOCASE") #Strict case insensitive match option
        #Option for similar matching "SELECT COUNT(*) FROM Password_Data WHERE Service LIKE '%$searchterm%' COLLATE NOCASE"
        if [ $count -eq 0 ]; then
                echo
                echo "No match found."
                sleep 3
        else
                echo
                echo "Matching record found:"
                sqlite3 PasswordSquirrel.db "SELECT * FROM Password_Data WHERE Service='$searchterm' COLLATE NOCASE"
               sleep 3
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

echo "Exiting..."
                     
