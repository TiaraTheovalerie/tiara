'''
Buatkan class stackpool yang memiliki atribut data, ukuran, dan top.
Buatkan method pada class tersebut yaitu:
1. clearstick
2. isEmpty
3. Topel
4. pop
5. push
'''

class Stackpool:
    def __init__(self, data, ukuran):
        self.data = data
        for i in range(ukuran):
            self.data.append(0)
        self.ukuran = ukuran
        self.top = 0
    
    def clearstack(self):
        self.ukuran = 0
        self.data = [0] * self.ukuran
    
    def isEmpty(self):
        return self.top == 0
    
    def isFull(self):
        return self.top == self.ukuran
    
    def push(self, el):
        if self.isFull():
            print("Stack overflow")
        else:
            self.data[self.top] = el
            print(f"inputan : {el}")
            self.top = self.top + 1
    
    def pop(self):
        if self.isEmpty():
            print("Stack underflow")
            return None
        self.top -= 1
        temp = self.data[self.top]
        self.data[self.top] = 0
        return temp
    
    def topEl(self):
        if self.isEmpty():
            return None
        return self.data[self.top-1]
    
    def show_stack(self):
        print(f"{self.data[:self.top]}")

        
pool = Stackpool([], 5)
for i in range(1,7):
    pool.push(i)

for i in range(3):
    pool.pop

print("\n")
for i in range(len(pool.data)):
    print(pool.data[i])

arr =[15,7,20,3,0]
size = len(arr)
s1 = Stackpool([],len(arr))

for i in arr:
    s1.push(i)

s1.show_stack()

s2 = Stackpool([], size)

def sort(s1, s2):
    s3 = Stackpool([], size)
    while not s1.isEmpty(): #selama s1 tidak empty
        temp = s1.pop() #ambil elemen dari s1
        while not s3.isEmpty(): #selama s3 tidak empty
            top_el = s3.topEl() #ambil elemen teratas dari s3
            if temp > top_el: #jika elemen yang diambil lebih besar dari elemen teratas di s3
                s1.push(s3.pop()) #pindahkan elemen dari s3 ke s1 lagi
            else:
                break #jika temp lebih kecil atau sama besar, berhenti

        s3.push(temp) #masukan elemen temp kepada s3

    while not s3.isEmpty(): #selama s3 tidak empty
        s2.push(s3.pop()) #pindahkan elemen s3 ke s2

sort(s1, s2) #mengambil angka2 dari s1 dan disusun ke s2
s2.show_stack() #menampikan s2

i_genap = Stackpool([], size)
i_ganjil = Stackpool([], size)

while not s2.isEmpty(): #selama s2 tidak empty
    temp = s2.pop() #ambil elemen dari s2
    if temp % 2 == 0: #jika temp habis dibagi 2
        i_genap.push(temp) #masukan elemen temp ke i_genap
    else:
        i_ganjil.push(temp) #masukan elemen temp ke i_ganjil

i_genap.show_stack() #menampilkan i_genap
i_ganjil.show_stack() #menampilkan i_ganjil