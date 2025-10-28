current_users = ('Austin', 'Tyler', 'Sam', 'Hunter', 'Luke')

new_users = ('Austin', 'Tyler', 'Jackson', 'Ryan', 'Phil')

for new_users in new_users:
    if new_users in current_users:
        print("you need to enter a new username.")

for new_users in new_users:
    if new_users not in current_users:
        print("This username is available.")