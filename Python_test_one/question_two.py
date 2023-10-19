
def average_of_two_numbers(x,y):
    output=(x+y)/2
    print(output)
average_of_two_numbers(4,6)       # average of two numbers


num1=int(input("Enter the num1:"))
num2=int(input("Enter the num2:"))
num3=int(input("Enter the num3:"))
if num1<num2 and num2<num3:
        print(f"{num1} is less than {num2} and {num3}")
elif num2<num1 and num2<num3:
     print(f"{num2} is less than {num1} and {num3}")
else:
       print(f"{num3} is less than {num1} and {num2}")


    

    