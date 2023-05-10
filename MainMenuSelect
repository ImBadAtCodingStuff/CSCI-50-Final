#!/bin/bash
while true; do
  echo "Password Squirrel Main Menu"
  echo
  PS3="Select menu option: "
  select Reply in Add_Record Search_Records Edit_Record Delete_Record Password_Generator Exit
  do
    if [ $Reply == "Add_Record" ]; then
      AddRecords #Addrecord subprogram here
    elif [ $Reply == "Search_Records" ]; then
      SearchRecords #searchrecord subprogram here
    elif [ $Reply == "Edit_Record" ]; then
      EditRecord #editrecord subprogram here
    elif [ $Reply == "Delete_Record"]; then
      DeleteRecord #deleterecord subprogram here
    elif [ $Reply == "Password_Generator" ]; then
      PasswordGenerator #PassGenerator subprogram here
    elif [ $Reply == "Exit" ]; then
      Exit #exit subprogram here
      exit #remove after adding subprogram in
    else 
      echo "Invalid input."
    fi
  done
done
