#add import
from question_a import reverse_string
def main():
    while True:
        user_input = input("Enter a string (or 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break
        reversed_str = reverse_string(user_input)
        print("Reversed string:", reversed_str)

if __name__ == "__main__":
    main()