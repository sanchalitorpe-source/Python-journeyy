# Writing and reading from a text file
file_name = "example.txt"

# Write to file
with open(file_name, "w") as f:
    f.write("Python is fun!\n")
    f.write("Intermediate topics are interesting.\n")

# Read file
with open(file_name, "r") as f:
    content = f.read()
print("File Content:\n", content)

# Append to file
with open(file_name, "a") as f:
    f.write("Appending a new line.\n")

# Read line by line
with open(file_name, "r") as f:
    for line in f:
        print("Line:", line.strip())
