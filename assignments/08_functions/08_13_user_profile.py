def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('Austin', 'Davis',Weight='185',Height='Six foot',Hometown='West Grove')
print(user_profile)