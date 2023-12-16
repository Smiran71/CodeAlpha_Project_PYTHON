def fibonacci(num):
    t1=0
    t2=1
    print(t1,t2,end=" ")
    sum=0
    for i in range(1,num+1):
        sum=t1+t2
        print(sum,end=" ")
        t1=t2
        t2=sum
num=int(input("Enter number to get fibonacci series till that number:"))
fibonacci(num)

