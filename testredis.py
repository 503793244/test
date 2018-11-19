li = []
for i in range(20):
    if i <=1 :
        li.append(1)
    else:
        li.append(li[i-1]+li[i-2])
print(li)


