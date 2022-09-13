print('HomeWork2')
list = [5, 44, 7, 2, 5]
reslist = []
for i in range((len(list)+1)//2):
    reslist.append(list[i]*list[len(list)-1-i])
print(reslist)
