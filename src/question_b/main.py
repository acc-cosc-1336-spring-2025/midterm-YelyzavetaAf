#add import
from question_b import get_day_of_week

def main():
    while True:
        user_input = input("Enter a number (1-7) or 'quit' to exit: ")
        if user_input.lower() =='quit':
            break
        if not user_input.isdigit():
            print("Invalid input.Please enter a number.")
            continue
        day = int(user_input)
        result = get_day_of_week(day)
        print("Result:", result)