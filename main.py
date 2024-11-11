from input.file_input import FileInput
from input.console_input import ConsoleInput

def main():
    while True:
        print("\n---//PackML Converter\\---")
        print("\nChoose an input option:")
        print("1. Console")
        print("2. Kafka")
        print("3. File")
        print("4. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == '1':
            console_input = ConsoleInput()
            console_input.input_console()
        elif choice == '2':
            pass

        elif choice == '3':
            file_input = FileInput()
            file_input.input_file()
        elif choice == '4':

            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()