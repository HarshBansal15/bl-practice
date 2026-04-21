drain=int(input("Enter battery drain per min"))
battery=100
min=0
while battery>=0:
    battery-=drain
    min+=1

print (min)
