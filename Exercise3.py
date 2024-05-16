lst_numbers =[]
num = 2950
while (5210 >=num >= 2950):
    if num % 9 == 0 and num % 13 == 0:
        lst_numbers.append(num)
    num += 1
        
print(f"The table is: {lst_numbers}")