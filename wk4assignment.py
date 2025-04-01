# there is a created file called example.txt
# reading original file
file = open("Assignments/example.txt", "r")
data = file.read()

# writing new file
new_file = open("Assignments/new_example.txt", "w")
new_file.write(data)

# reading the new file
new_file = open("Assignments/new_example.txt", "r")
new_file_data = new_file.read()
print(new_file_data)
new_file.close()

try:
    fileName = input("\nEnter the name of the file to read together with the file extension: ")
    file = open(f"Assignments/{fileName}", "r")
    data = file.read()
    print(data)
except FileNotFoundError:
    print("\nFile not found. Please check the file name and try again.")
    file = None # ensure no error in the finally block if file was not opened
finally:
    print("\nThe program has run successfully.")
    if file: # closes file if file was opened 
        file.close()
    