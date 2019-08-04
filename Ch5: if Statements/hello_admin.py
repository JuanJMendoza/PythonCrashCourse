'''
Make a list of five or more usernames, including the name 'admin'. Imagine you are 
writing code that will print a greetin to each user after they log in to a website. Loop 
through the list, and print a greeting to each user:
- If the username is 'admin', print a special greeting, such as Hello admin, would you
    like to see a status report?
- Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging
    in again.
'''
users = ["daniel", "jacob", "juan","shawn"]

if users:
    for user in users:
        if user == ("juan" or "jacob"):
            print(f"Hello, {user}, would you like to see a status report?")
        else:
            print(f"Get out, {user}")
else:
    print("We need to find some users!")