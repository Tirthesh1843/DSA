# sum of n numbers:

def sum_of_n_numbers(n):
    if n == 0:
        return 0
    sum = n * (n + 1) / 2
    return int(sum)

n = int(input("Enter number: "))
print("Sum of first", n, "numbers is: ", sum_of_n_numbers(n))