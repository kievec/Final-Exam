def longest_un_word(file_name):
    """
    Returns the longest word in the file that starts with 'un'.
    If no such word exists, returns None.
    """

    # Variable that will store the longest matching word found
    longest = None

    try:
        # Open the file in read mode
        with open(file_name, "r") as f:

            # Read the file line by line
            for line in f:

                # Split the line into individual words
                words = line.split()

                # Check each word in the line
                for word in words:

                    # Convert to lowercase to make comparison case-insensitive
                    w = word.lower()

                    # Check if the word starts with "un"
                    if w[:2] == "un":

                        # If no word stored yet OR current word is longer,
                        # update the longest word
                        if longest is None or len(w) > len(longest):
                            longest = w

        # After checking all lines, return the result
        return longest

    # Handle case where file does not exist
    except FileNotFoundError:
        print("File not found")
        return None

result = longest_un_word("test.txt")
print(result)