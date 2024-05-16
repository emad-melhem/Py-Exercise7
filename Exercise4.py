try:
    numbers = input('Enter your number :')
    odd_nums = 0
    for x in numbers:
        if int(x) % 2 != 0:
            odd_nums += 1
            
    print(f"This number has {odd_nums} odd digits and {len(numbers) - odd_nums} even digits")
    
except ValueError:
    print("Input error!!\nYou must enter numbers only.")