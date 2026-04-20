def transpose(arr):
    arr1=[[0 for i in range(3)]for j in range(3)]
    for i in range (3):
        for j in range (3):
            arr1[j][i]=arr[i][j]

    for i in range (3):
        for j in range (3):
            print(arr1[i][j],end='')
        print()        

arr=[]
for i in range(3):
    row =[]
    for j in range(3):
        x=int(input(f"Enter ELEMENT {i},{j} : "))
        row.append(x)
    arr.append(row)
transpose(arr)
