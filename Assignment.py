def main():
    # Ask the user for the input filename
    input_file = input("Enter the filename to read: ")

    try:
        # Try to open and read the file
        with open(input_file, 'r') as file:
            content = file.readlines()
        
        # Modify content: Example - convert all text to uppercase
        modified_content = [line.upper() for line in content]

        # Define the output filename
        output_file = "modified_" + input_file

        # Write modified content to the new file
        with open(output_file, 'w') as file:
            file.writelines(modified_content)

        print(f"Modified content has been written to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except IOError:
        print(f"Error: The file '{input_file}' could not be read or written.")

if __name__ == "__main__":
    main()
