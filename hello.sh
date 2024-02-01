#!/bin/bash

a=2
b=2
c=$((a+b))

echo "Bash says: Hello, world!"
echo "$a+$b=$c"

# Create an array of strings
listOfUsers=("User1" "User2" "User3")

# For loop to print each user
for user in "${listOfUsers[@]}"; do
    echo $user
done

