#add import
from question_d import get_fahrenheit

def main():
    print("Celsius\tFahrenheit")
    for c in range(0, 21):
        f = get_fahrenheit(c)
        print(f"{c}\t{f}")

if __name__ == "__main__":
    main()
