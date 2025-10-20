def show_even_numbers(n):
    for i in range(1, n + 1):
        print(i * 2)
    return [i * 2 for i in range(1, n + 1)]
n = int(input("Enter how many even numbers: "))
evens = show_even_numbers(n)
sum_even = sum(evens)
product = 1
for num in evens:
    product *= num
print("Sum =", sum_even)
print("Product =", product)
