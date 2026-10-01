# sum of even numbers between 20 to 40(both included.)
sum = 0
for i in range(20, 41):
    if i % 2 == 0:
        sum += i
print("Sum of even numbers between 20 to 40 is: ", sum)