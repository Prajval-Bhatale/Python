with open("Prajval.txt", "r+") as f:
    content = f.read()
    f.write("\nAdded using r+")


with open("Prajval1.txt", "w+") as f:
    f.write("New content added using the w+")
    # f.seek(0)  # move cursor to beginning
    print(f.read())

with open("Prajval2.txt", "a+") as f:

    f.write("Appended with a+")
    # f.seek(0)
    print(f.read())
    f.close()