while True:
    ticket = int(input('How old are you?'))
    
    if ticket < 3:
        print('Your ticket is free')
    elif 3 <= ticket <= 12:
        print('Your ticket is $10')
    elif ticket > 12:
        print('Your ticket is $15')
    elif ticket != 'quit':
        print(ticket)