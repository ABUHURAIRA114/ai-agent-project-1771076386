class Calculator:
    def __init__(self):
        self.history = []

    def run(self):
        while True:
            print("1. Operations")
            print("2. Quit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.operations()
            elif choice == "2":
                break
            else:
                print("Invalid choice. Please choose a valid option.")

    def operations(self):
        print("Operations menu")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        choice = input("Enter your choice: ")

def main():
    calculator = Calculator()
    calculator.run()

if __name__ == "__main__":
    main()