#!/bin/bash
while true; do
  echo "Password Squirrel Main Menu"
  echo
  PS3="Select menu option: "
  select Reply in Add_Record Search_Records Edit_Record Delete_Record Password_Generator Exit
  do
    if [ $Reply == "Add_Record" ]; then
      python3 addRecord.py
    elif [ $Reply == "Search_Records" ]; then
      bash SearchRecords.sh
    elif [ $Reply == "Edit_Record" ]; then
      python3 editRecord.py
    elif [ $Reply == "Delete_Record"]; then
      bash DeleteRecord.sh
    elif [ $Reply == "Password_Generator" ]; then
      python3 generator.py
    elif [ $Reply == "Exit" ]; then
      PERL exit.pl
    else 
      echo "Invalid input."
    fi
  done
done
