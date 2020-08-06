#utilizando dunder methods 
class Train:
    def __init__(self,num):
        self.num = num

    def __repr__(self):
        return f"The number of cars is {self.num}"

    def __len__(self):
        return self.num

train = Train(4)
print(len(train))
print(train)