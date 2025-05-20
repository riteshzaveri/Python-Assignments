# Write initial user input to the file
initial_data = input("Enter initial data to write to the file: ")
with open("output.txt", "w") as file:
    file.write(initial_data + "\n")
print("Data successfully written to output.txt")

# Append additional data to the same file
append_data = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(append_data + "\n")
print("Data successfully appended.")

# Read and display final content of the file
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    print(file.read())