
try:
    number= int(input('Enter a number to calculate the sum :'))
    sum_number = 0
    while number > 0:
        sum_number += number
        number -= 1
    print(f'The sum is: {sum_number}')
    
    #other way
    # sum_number = number * (number + 1)/2
    # print(f'The sum is: {sum_number}')
    
except ValueError:
    print("Input error!!\nYou must enter numbers only.")