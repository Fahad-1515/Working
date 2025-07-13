#program to print Fizz multiple of 3,Buzz multiple of 5 and FizzBuzz multiple of 15
my_list=[]
n=int(input("Enter the specified NO:"))
for i in range(1,n+1):
    result=""
    if i%3==0:
        if i%5==0:
                  result=result+"FizzBuZZ"
                  my_list.append(result)
        else:
                  result=result+"Fizz"
                  my_list.append(result)

    elif i%5==0:
                result=result+"BuZZ"
    else:
             my_list.append(i)

print(my_list)






