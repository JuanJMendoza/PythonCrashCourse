''' We won't always know how many arguments we'll want to accept, one example involves
building user profiles: you know you'll get information about a user, but you're not
sure what kind of information you;ll receive. The function build_profile() in the 
following exmpale always takes in a first and last name, but it accepts an arbitrary 
number of keyword arguments as well: '''
def build_profile(first, last, **user_info):
    '''Build a dictionary containing everythin we know about a user.'''
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location="princeton", field="physics")
print(user_profile)