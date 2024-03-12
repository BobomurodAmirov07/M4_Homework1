s = input(">>> ")

i = int(len(s) // 2) + 1

lst = [s[:i], s[i:]]

lst[0], lst[1] = lst[1], lst[0]

s = "".join(lst)

print(s)