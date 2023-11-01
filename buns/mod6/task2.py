class DoubleElement:
    def __init__(self, *lst):
        self.data = lst
        self.num = 0
        
    def __next__(self):
        self.num += 2
        if self.num <= len(self.data):
            return (self.data[self.num - 2], self.data[self.num - 1])
        elif self.num <= len(self.data) + 1:
            return (self.data[self.num - 2], None)
        else:
            raise StopIteration
            
    def __iter__(self):
        return self        
            

dL = DoubleElement(1,2,3,4)
for pair in dL:
    print(pair)

print("\n")

dL = DoubleElement(1,2,3,4,5)
for pair in dL:
    print(pair)    
    
#Ожидаемый результат кода:
#(1, 2)
#(3, 4)
#
#(1, 2)
#(3, 4)
#(5, None)

