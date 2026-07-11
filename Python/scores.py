total = []
number = int(input("How many scores do you want to enter? "))
for i in range(number):
    score = int(input("enter score: "))
    total.append(score)
total_sum = sum(total)   
print("Total scores entered:", total_sum)  
