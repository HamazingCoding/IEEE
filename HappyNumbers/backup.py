# Firstly to check if a number is a happy number
def HappyNumber(number):
    used = set()
    while number != 1 and number not in used:
        used.add(number)
        number = sum(int(digit) ** 2 for digit in str(number))
    return number == 1

# Now to count happy numbers in a range [a, b]
def HappyNumberCount(a, b):
    count = 0
    for number in range(a, b + 1):
        if HappyNumber(number):
            count += 1
    return count

# Two space-separated integers a and b (Input)
a, b = map(int, input().split())

# Number of happy numbers in the range [a, b] (Output)
result = HappyNumberCount(a, b)
print(result)
