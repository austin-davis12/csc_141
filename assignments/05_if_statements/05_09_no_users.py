users = ['']

for i in users:
    if i == 'admin':
        print ("Hello admin, would you like a status report?")
    else:
        print ("Hello f{i}, thank you for logging in.")
    if users == ['']:
        print("We need to find users!")
