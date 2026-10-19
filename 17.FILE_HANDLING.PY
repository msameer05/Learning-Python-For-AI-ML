# NOW IN THIS CHEAPTER WE WILL LEARN ABOUT FILE HANDLING IN PYTHHON PROGRAMMING LANGUAGE:-
# FILE HANDLING:-
# FILE MODES:-
# "r"   -------> read only
# "w"   -------> write (overwrite)
# "a"   -------> append to end
# "x"   -------> create (fails if exists)

file = open("sam.txt", "w")
data = input("what you want to write : ")
file.write(data)

file = open("sam.txt", "r")
print(file.read())

# WRITTING:-
with open("notes.txt" , "w") as f:
    f.write("hello from python")

# READING:-
with open("notes.txt", "r") as f:
    content = f.read()
    print(content)

# APPENDING:-
with open("notes.txt", "a") as f:
    f.write("\n added a new line")

# ALWAYS USE THE:-
#               WITH:-
#                   it automatically closes the file for you, even if an error occurs