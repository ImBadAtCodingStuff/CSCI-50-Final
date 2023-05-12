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


status="y"
while [ $status = "y" ]; do
        echo "Password Squirrel"
        echo "Delete Record"
        read -p "Enter name of service/username to delete record for: " delrec
        count=$(sqlite3 PasswordSquirrel.db "SELECT COUNT(*) FROM Password_Data WHERE Service LIKE '%$delrec%' COLLATE NOCASE OR Username LIKE '%$delrec%' COLLATE NOCASE")
        if [ $count -eq 0 ]; then
          echo
          echo "No matching records found."
          sleep 2
        else
          echo
          echo "Matching record(s) found:"
          sqlite3 PasswordSquirrel.db "SELECT rowid, * FROM Password_Data WHERE Service LIKE '%$delrec%' COLLATE NOCASE OR Username LIKE '%$delrec%' COLLATE NOCASE" | awk -F"|" '{printf "Record ID: %s\nService: %s\nUsername: %s\nPassword: %s\n\n", $1, $2, $3, $4}'
          echo
          if [ $count -eq 1 ]; then
                read -p "Enter the Record ID of the record you want to delete: " delid
                delcheck=(sqlite3 PasswordSquirrel.db "SELECT Service FROM Password_Data WHERE rowid=$delid")
                if [ "$delcheck" ]; then
                        delrec=$(sqlite PasswordSquirrel.db "SELECT Service FROM Password_Data WHERE rowid=$delid")
                        DeleteConfirm "$delrec"
                else
                        echo "Invalid choice. Try again."
                fi
          else
                while true; do
                        read -p "Enter the Record ID of the record you want to delete: " delid
                        if [ -z "$delid" ]; then
                                echo "Invalid choice. Try again."
                        else
                                delcheck=$(sqlite3 PasswordSquirrel.db "SELECT Service FROM Password_Data WHERE rowid=$delid")
                                if [ "$delcheck" ]; then
                                        delrec=$(sqlite3 PasswordSquirrel.db "SELECT Service FROM Password_Data WHERE rowid=$delid")
                                        DeleteConfirm "$delrec"
                                        break
                                else
                                        echo "Invalid choice. Try again."
                                fi
                        fi
                done
          fi
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


