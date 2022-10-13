"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

print(numbers)
numbers.sort()
if (len(numbers)%2==0):
    first_median = numbers[int(len(numbers)/2) - 1]
    second_median = numbers[int(len(numbers)/2)]
    print((first_median + second_median) / 2)
else:
    print(numbers[int(((len(numbers) - 1) / 2))])
