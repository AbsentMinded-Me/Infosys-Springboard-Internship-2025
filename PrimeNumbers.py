# Function to return a list of prime numbers less than the given number
def prime(num):
    prime_numbers = []
    is_prime = True
    for i in range(2, num):
        for j in range(2, int(i ** 0.5)+1):
            if i % j == 0:
                is_prime = False
                break
            else:
                is_prime = True
        if is_prime:
            prime_numbers.append(i)
    return prime_numbers


# To provide user input and display the result
while True:
    try:
        number = int(input("Enter a number to find all prime numbers less than it: "))
        if number > 1:
            primes = prime(number)
            print(f"Prime numbers less than {number}: {primes}")
        else:
            print("Please enter a number greater than 1.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    exit = input("Do you want to exit? (yes/no): ").strip().lower()
    if exit == 'yes':
        break