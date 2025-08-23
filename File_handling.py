filename = input("Enter the file name: ")

try:
    # Open the file and read its content
    with open(filename, "r") as f:
        content = f.read()

    # Change the content (example: make it uppercase)
    new_content = content.upper()

    # Write the new content into a new file
    new_filename = "new_" + filename
    with open(new_filename, "w") as f:
        f.write(new_content)

    print(f"✅ Done! Modified content saved in '{new_filename}'")

except FileNotFoundError:
    print("❌ File not found! Please check the name and try again.")
except Exception as e:
    print("⚠️ Something went wrong:", e)
