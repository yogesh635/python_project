cantacts = {}

while True
print('\n Contact Book app')
print('1. Create contact')
print('2. view contact')
print('3. update contact')
print('4. delete contact')
print('5. search contact')
print('6. count contact')
print('7. Exit')

choice = input('enter your choice = ')
if choice == '1':
    name = input('enter the name = ')
    if name in contact: