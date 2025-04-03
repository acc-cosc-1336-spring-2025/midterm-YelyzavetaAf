#add import
from question_c import is_prime

def main():
    while True:
        user_input = input("Enter a number (or 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break
        if not user_input.isdigit():
            print("Invalid input. Please enter a number.")
            continue
        number = int(user_input)
        if is_prime(number):
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")

if __name__ == "__main__":
    main()