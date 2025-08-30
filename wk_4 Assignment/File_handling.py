# 1. Function to read from a file
def read_file(filename):
    with open(filename, "r") as f:
        content = f.read()
    return content


# 2. Function to modify the content
def modify_content(content, choice):
    if choice == "1":
        return content.upper()               # Make text uppercase
    elif choice == "2":
        return content.lower()               # Make text lowercase
    elif choice == "3":
        return content.title()               # Capitalize each word
    elif choice == "4":
        return content + "\n\n-- Modified File --"  # Add extra text
    else:
        return content                       # No change if invalid choice


# 3. Function to write to a new file
def write_file(new_filename, content):
    with open(new_filename, "w") as f:
        f.write(content)


# 4. Main program
def main():
    filename = input("Enter the file name: ")

    try:
        # Step 1: Read file
        content = read_file(filename)

        # Step 2: Ask user for modification type
        print("\nChoose a modification:")
        print("1. Convert to UPPERCASE")
        print("2. Convert to lowercase")
        print("3. Capitalize Each Word")
        print("4. Add extra text at the end")
        choice = input("Enter your choice (1-4): ")

        # Modify content based on choice
        new_content = modify_content(content, choice)

        # Step 3: Write to a new file
        new_filename = "new_" + filename
        write_file(new_filename, new_content)

        # Step 5: Success message
        print(f"\n✅ Done! Modified content saved in '{new_filename}'")

    except FileNotFoundError:
        print("❌ File not found! Please check the name and try again.")
    except Exception as e:
        print("⚠️ Something went wrong:", e)


# Run the program
if __name__ == "__main__":
    main()
