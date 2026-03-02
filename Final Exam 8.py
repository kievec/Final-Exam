import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))
# Traverse the list using index because we need to MODIFY elements
for i in range(len(random_numbers)):

    # If number is odd (remainder 1 when divided by 2)
    if random_numbers[i] % 2 != 0:
        # Replace odd number with its negative counterpart
        random_numbers[i] = -random_numbers[i]

    else:
        # If number is even, replace it with its double
        random_numbers[i] = random_numbers[i] * 2

# Print the modified list
print(random_numbers)