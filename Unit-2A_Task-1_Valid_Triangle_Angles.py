a=float(input("enter angle value(a);"))
b=float(input("enter angle value(b);"))
c=float(input("enter angle value(c);"))
sum_of_angles=a+b+c
if a>0 and b>0 and c>0 and sum_of_angles==180:
    print("yes it forms a triangle")
else:
    print("no if it does not forms a triangle")