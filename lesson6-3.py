name = ['T','I','M','O','T','H' ,'Y']
name.sort()
print(name)
toSort = [4,2,1,5,3]

for i in range(len(toSort)):
    key = toSort[i]
    j = i -1
    while j >= 0 and key < toSort[j]:
        toSort[j + 1], toSort[j]
        j -= 1
        toSort[j + 1]=key
    swapped = False
    for j in range(0,len(toSort)-1-i):
        if toSort[j] > toSort[j+1]:
            toSort[j],toSort[j+1] = toSort[j+1],toSort[j]
            swapped = True
        if swapped == False:
            break
print(toSort)