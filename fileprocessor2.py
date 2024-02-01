#!/usr/bin/env python3
import sys

print("Printing out User Data:\n")

for line in sys.stdin:
    if not line.startswith('#'):
        user_data = line.strip().split(':')
        if len(user_data) == 4:
            print(f"The user {user_data[0]} has a password of {user_data[1]} and has userid {user_data[2]} and groupid {user_data[3]}")
        else:
            print(f"Skipped invalid line: {line.strip()}")
    else:
        commented_user = line.strip()[1:].split(':')[0]
        print(f"User{commented_user} is skipped because it starts with a hashtag (is commented out)")

print("\nEnd of User Data")
