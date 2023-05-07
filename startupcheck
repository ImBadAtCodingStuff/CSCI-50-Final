#!/bin/bash
#check if run before
Check_File=".runflag"

if [ -e "$Check_File" ]; then
  echo "The script has been run before"
else  
  echo -e "\t\tWelcome to Password Squirrel!
\tThis program helps you securely store your passwords.
To get started, you need to set up a main password that will be used to encrypt and protect your data. 
This password should be at least 8 characters long and contain a combination of uppercase letters, lowercase letters, and numbers. No special symbols will be accepted."
  while true; do
    read -p "Enter your main password: " mainpass
    strong="^[a-zA-Z0-9]{8,}$"
    if [[ "$mainpass" =~ $strong ]]; then
      echo "Main password is set."
      echo $mainpass
      break
    else
      echo -e "Uh oh! 
Password must be at least 8 characters long and contain at least one letter and one number.
\tTry again."
    fi
  done
  touch "$Check_File"
fi
