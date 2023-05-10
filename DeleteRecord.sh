#!/bin/bash
#Main developer: Emma Ford

DeleteConfirm () {
  delvar="$1"
  echo "Do you want to delete this record? This cannot be undone."
  while true; do 
    echo "Enter Y to delete record."
    echo "Enter N to keep record."
    read -p "Enter selection: " delx
    if [[ $delx == [Yy] ]]; then
      sqlite3 PasswordSquirrel.db "DELETE FROM Password_Data WHERE Service='$delvar' COLLATE NOCASE"
      echo "Record Deleted."
      echo
      break
    elif [[ $delx == [Nn] ]]; then
      echo "Record will remain in the system."
      echo
      break
    else
      echo "Invalid choice. Try again."
    fi
  done
}


clear
status="y"
while [ $status = "y" ]; do
        echo "Password Squirrel"
        echo "Delete Record"
        read -p "Enter name of service to delete record for: " delrec
        count=$(sqlite3 PasswordSquirrel.db "SELECT COUNT(*) FROM Password_Data WHERE Service='$delrec' COLLATE NOCASE") 
        if [ $count -eq 0 ]; then
          echo
          echo "No matching records found."
          sleep 3
        else
          echo
          echo "Matching record found:"
          sqlite3 PasswordSquirrel.db "SELECT * FROM Password_Data WHERE Service='$delrec' COLLATE NOCASE"
          echo
          DeleteConfirm "$delrec"    
        fi
        echo
        echo "Enter Y to delete another record."
        echo "Enter X to return to main menu."
        while true; do
          read -p "Enter choice: " reply
            if [[ $reply == [Yy] ]]; then
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
