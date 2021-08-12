#odd numbers between 1 and user input
max= int(input("enter the number"))
odd_number=[]
for i in range(1,max):
    if i%2==1:
        odd_number.append(i)
        print("odd number :",odd_number)
