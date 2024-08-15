while True:
    percentage= int(input('Enter your percentage:  '))
    grade = ['A','B','C','E']
    if percentage >= 91:
        print(f'Your grade is {grade[0]}')
    elif percentage  >= 81:
        print(f'Your grade is {grade[1]}')
    elif percentage >= 60:
        print(f'Your grade is {grade[2]}')  
    else:
        print(f'Your grade is {grade[3]}')