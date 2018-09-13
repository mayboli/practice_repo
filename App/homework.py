# Write a basic program that prints first 100 digits that are even


first_hundred = []

def hundred_even(n):
    for i in range(n):
        if len(first_hundred) < 100:
            if i % 2 == 0:
                first_hundred.append(i)

    return first_hundred

print(hundred_even(2000))