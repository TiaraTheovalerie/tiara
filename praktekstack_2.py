class stackPool:
    def __init__(self,dat, uk):
        self.dat = dat
        for i in range(uk):
            self.dat.append(0)
        self.uk = uk
        self.top = 0
    
    def clearStack(self):
        self.uk = 0
        self.dat = [0] * self.uk

    def isEmpty(self):
        return self.top == 0

    def isFull(self):
        return self.top == self.uk
    
    def push(self, el):
        if self.isFull():
            print ("stack overflow!")
        else:
            self.dat[self.top] = el
            print(f"inputan : {el}")
            self.top = self.top + 1

    def pop(self):
        if self.isEmpty():
            print("Stack underflow!")
            return None 
        self.top -= 1
        temp = self.dat[self.top]
        self.dat[self.top] = 0
        return temp
    
    def topEl(self):
        if self.isEmpty():
            return None
        return self.dat[self.top-1]
    
    def show_stack(self):
        print(f"{self.dat[:self.top]}")

arr = [15, 7, 20, 3 ,0]
s1 = stackPool([], len(arr))

for i in arr:
    s1.push(i)

s1.show_stack()