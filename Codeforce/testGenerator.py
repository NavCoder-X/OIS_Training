n = 1000000
q = 1000000

with open("input.txt", "w") as f:
    f.write(f"{n} {q}\n")
    for i in range(n):
        f.write(f"1 ")
    f.write("\n")
    for i in range(q):
        f.write("1 ")