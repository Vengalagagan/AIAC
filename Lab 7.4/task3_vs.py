with open("example.txt", "w") as f:
    f.write("Hello, world!")

f1 = open("data1.txt", "w")
f2 = open("data2.txt", "w")

f1.write("First file content\n")
f2.write("Second file content\n")

print("Files written successfully")
