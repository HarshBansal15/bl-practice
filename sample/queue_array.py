#queue in array class 
class queue:

    def __init__(self):
        self.q=[]
        self.front=-1 #end refers to 
    def push(self,x):
        if self.front==-1:
            self.front=0
        self.q.append(x)
    def pop(self):
        if len(self.q)==0:
            return -1 #queue empty
        x=self.q[self.front]
        self.front+=1
        if self.front==len(self.q):
            self.front=-1
            self.q=[]#manually empty the queue
        return x
    def getfront(self):
        if len(self.q)==0:
            return -1
        return self.q[self.front]
    def size(self):
        if self.front==-1:
            return -1 
        return len(self.q)-self.front    
    
queue =queue()
queue.push(10)
queue.push(20)
queue.push(30)
print(queue.getfront())
queue.pop()
print(queue.getfront())
# queue.pop()
# print(queue.getfront())
# queue.pop()
# print(queue.getfront())
# print(queue)
