bonus=20

def marks(marks:int) ->int:
    total = marks+bonus
    return total

score =55
print(marks(score))
print(type(marks))
print("bonus " + str(bonus))