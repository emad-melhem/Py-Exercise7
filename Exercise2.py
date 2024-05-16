
try:
    number= int(input('Enter a number to calculate the multiplication :'))
    multi_list = []
    for x in range(10):
        multi_list.append(number * (x + 1))
    print(f"The table is: {multi_list}")
    
except ValueError:
    print("Input error!!\nYou must enter numbers only.")