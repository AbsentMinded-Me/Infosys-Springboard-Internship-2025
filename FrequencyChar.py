def frequency_char(s):
    freq = {}
    for char in s:
        if char.isalpha():  # Consider only alphabetic characters
            char = char.lower()  # Normalize to lowercase
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

# To provide user input and display the result
while True:
    user_input = input("Enter a string to find the frequency of each character: ")
    frequencies = frequency_char(user_input)
    print("Character frequencies:")
    for char, count in frequencies.items():
        print(f"'{char}': {count}")
    exit = input("Do you want to exit? (yes/no): ").strip().lower()
    if exit == 'yes':
        break