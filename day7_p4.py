colors = [ "Red" , 'Green', 'Pink', 'Blue', 'Black', 'Purple','Yellow', 'Magenta', 'Brown']

n=int(input("Enter number of colors to be removed"))

arr=[]
for i in range(n):
    x=int(input("Enter index to be removed"))
    arr.append(x)

for i in range(n):
    colors.pop(arr[i])
    

print(colors)

