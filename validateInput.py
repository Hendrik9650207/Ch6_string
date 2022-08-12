while True:
    age = input('Enter your age:')
    if age.isdecimal():
        break
    print('Enter a number for your age.')

while True:
    print('Select a new password(letters and numbers only):')
    password = input()
    if password.isalnum():
         # isalnum() method : check it is alphabet or number?
        if password.isalnum():
            break
        print('Password can only have letters and numbers')

