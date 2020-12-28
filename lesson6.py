array2d = [
          [1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]
          ]
array2d.append([13,14,15,16])
print(array2d[0])
print(array2d[2][3])
for i in range(4):
    array2d[i].append(20)
print(array2d[2][4])
