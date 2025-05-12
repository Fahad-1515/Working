class stack:
    def __init__(self):
        self.__stack__list=[]
    def push(self,value):
        self.__stack__list.append(value)
    def pop (self):
        value=self.__stack__list[-1]
        del self.__stack__list[-1]
        return value
    def __str__(self):
        return  f"stack(top ->bottom):{self.__stack__list[::-1]}"
stack1_object_1=stack()
stack1_object_1.push(4)
stack1_object_1.push(6)
stack1_object_1.push(7)
stack1_object_1.push(8)
stack1_object_1.push(9)
stack1_object_1.push(5)
print(stack1_object_1.pop())
print(stack1_object_1)
