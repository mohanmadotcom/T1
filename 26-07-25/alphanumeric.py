def check_element(elem):
    vowels = {'a', 'e', 'i', 'o', 'u'}

    # Try to convert to integer
    try:
        num = int(elem)
        if num > 0:
            print(f"{elem} is a positive number.")
        elif num < 0:
            print(f"{elem} is a negative number.")
        else:
            print(f"{elem} is zero.")
    except ValueError:
        # Not a number, check if it's a single alphabet character
        if isinstance(elem, str) and elem.isalpha() and len(elem) == 1:
            if elem.lower() in vowels:
                print(f"{elem} is a vowel.")
            else:
                print(f"{elem} is a consonant.")
        else:
            print(f"{elem} is not a valid single alphabet character.")

# Example list
elements = [1, 2, 3, -4, -5, 'a', 'b', 'c']

# Apply function to each element
for item in elements:
    check_element(item)
