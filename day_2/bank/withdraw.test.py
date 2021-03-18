import withdraw

# test cases
print(withdraw.withdraw(10, 100)) #90
print(withdraw.withdraw(5, 100)) #95
print(withdraw.withdraw(8.50, 100)) #91.5
print(withdraw.withdraw(10.27, 99.50)) #89.23

print(withdraw.withdraw(10.27, 10)) #Insufficient Balance
