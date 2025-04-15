def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Welcome to the Temperature Converter!")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        c = float(input("Enter temperature in Celsius: "))
        f = celsius_to_fahrenheit(c)
        print(f"{c}°C is {f:.2f}°F")
    elif choice == '2':
        f = float(input("Enter temperature in Fahrenheit: "))
        c = fahrenheit_to_celsius(f)
        print(f"{f}°F is {c:.2f}°C")
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
