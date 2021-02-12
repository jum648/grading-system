print("Enter marks for 5 units :")
math=int(input())
eng=int(input())
kis=int(input())
chem=int(input())
phy=int(input())
sum=math+eng+kis+chem+phy
avg=sum/5
if avg>=70 and avg<=100:
  print('A=EXELLENT')
elif avg>=60 and avg<=69:
    print('B=GOOD')
elif avg>=50 and avg<=59:
    print('C=FAIR')
elif avg>=40 and avg<=49:
    print('D=PASS')
elif avg>=30 and avg<=39:
    print('E=FAIL')