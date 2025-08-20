file = open("Prajval.txt","w")

file.write("Hello Brother\n")
file.write("Ram Ram Bhai ")
file.close()


file1 = open("Prajval.txt","r")
content = file1.read()
print(content)
file1.close()

file2 = open("Prajval.txt","a")

file2.write("\nOm Namo Bhagvatey Vasudevay Namahaa ")
file2.close()


