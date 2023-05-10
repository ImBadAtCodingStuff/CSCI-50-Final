#!/bin/bash
#Main developer: Emma Ford

while true; do
  echo "Password Squirrel Main Menu"
  echo
  PS3="Select menu option: "
  select Reply in Add_Record Search_Records Edit_Record Delete_Record Password_Generator Exit
  do
    if [ $Reply == "Add_Record" ]; then
      python3 addRecord.py
      break
    elif [ $Reply == "Search_Records" ]; then
      chmod u+rx SearchRecords.sh
      ./SearchRecords.sh
      break
    elif [ $Reply == "Edit_Record" ]; then
      python3 editRecord.py
      break
    elif [ $Reply == "Delete_Record" ]; then
      chmod u+rx DeleteRecord.sh
      ./DeleteRecord.sh
      break
    elif [ $Reply == "Password_Generator" ]; then
      python3 generator.py
      break
    elif [ $Reply == "Exit" ]; then
      chmod u+rx exit.pl
      ./exit.pl
      break
      exit
    else 
      echo "Invalid input."
    fi
  done
done
