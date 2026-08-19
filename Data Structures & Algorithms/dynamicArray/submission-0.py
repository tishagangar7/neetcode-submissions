class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.size=0
        self.arr=[0]*capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i]=n

    def pushback(self, n: int) -> None:
        #if array is full meaning size=capacity then we will have
        #increase array capacity first so call resize
        if self.size==self.capacity:
            self.resize()
        
        #since we are adding one element in the end, increase size
        self.arr[self.size]=n
        self.size+=1

    def popback(self) -> int:
        self.size-=1
        return self.arr[self.size]

    def resize(self) -> None:
        #if empty then [0,0,0] gets doubled to [0,0,0,0]
        #if not empty them [2,5,0] gets doubled to [2,5,0,0,0,0]
        new_arr=[0]*(self.capacity*2)
        for i in range(self.size):
            new_arr[i]=self.arr[i]
        self.arr=new_arr
        self.capacity*=2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity