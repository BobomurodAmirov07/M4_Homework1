lst = input(">>> ").split()

lst_d = list()

for i in lst:
    for j in i:
        if i.count(j) > 1 and i in lst and i not in lst_d:
            lst_d.append(i)

lst2 = list()

for i in lst_d:
    for l in lst:
        if i == l:
            lst.remove(l)

for i in lst:
    l = int(len(i) // 2) + 1
    lst2.append([i[:l], i[l:]])

for i in range(len(lst2)):
    lst2[i][0],lst2[i][1] = lst2[i][1], lst2[i][0]
    lst2[i] = "".join(lst2[i])

print(lst2)