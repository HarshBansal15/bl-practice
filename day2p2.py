time=int(input("Enter time in seconds"))

hr=time//3600
time = time-hr*3600
min = time//60
sec= time-min*60

print(f"[{hr}:{min}:{sec}]")
