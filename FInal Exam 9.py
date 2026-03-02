# ----- LIST (Mutable) -----

numbers = [1, 2, 3]

print("Original list:", numbers)

# Modify the first element directly
numbers[0] = 10

print("Modified list:", numbers)


# ----- STRING (Immutable) -----

text = "cat"

print("\nOriginal string:", text)

# Attempt to modify a character (will cause error)
try:
    text[0] = "b"
except TypeError:
    print("Strings cannot be modified directly.")


# Correct way to 'modify' a string
new_text = "b" + text[1:]

print("Original string after attempt:", text)
print("New string created:", new_text)