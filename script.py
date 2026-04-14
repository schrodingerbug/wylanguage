var = input("Before printing,would you like to set a variable?If so,x=")

output = input("Write your print code here:")

if output != "log<'x'>":
 print(output[5:-2])
elif output == "log<'x'>":
 print(var)

value = input("Check the value of x? x?=")
if value == var:
    print("True")
elif value != var:
    print("False")


