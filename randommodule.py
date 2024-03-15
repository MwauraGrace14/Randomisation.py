#Random module 
#import random
#score = random.randint(0,1)
#if score == 1:
 # print("Heads")
#else:
 # print("Tails")

#Offset & Appending items to list

import random
names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
names_count =len(names)
pay_bill = random.randint(0, names_count -1)
print(names[pay_bill] +" is going to buy the meal today!") 