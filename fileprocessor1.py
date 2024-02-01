#!/usr/bin/env python3

with open('fileprocessor.input', 'r') as file:
    lines = file.readlines()

print("Printing out User Data:\n")

for line in lines:
    if not line.startswith('#'):
        user_data = line.strip().split(':')
        # Ensure user_data has exactly 4 elements before attempting to print
        if len(user_data) == 4:
            print(f"The user {user_data[0]} has a password of {user_data[1]} and has userid {user_data[2]} and groupid {user_data[3]}")
        else:
            print(f"Skipping line due to incorrect format: {line.strip()}")
    else:
        # Adjusted to correctly extract and print the user name
        commented_user = line.strip().split(':')[0].lstrip('#')
        print(f"{commented_user} is skipped because it starts with a hashtag (is commented out)")

print("\nEnd of User Data")
