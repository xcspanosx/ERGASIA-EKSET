print "Give a number up to 1.000.000"
num=input()
while (num>1000000):
    print "You gave wrong number."
    num=input()
sum=0
sum1=0
sum2=0
sum3=0
sum4=0
sum5=0
sum6=0
sum7=0
sum8=0
sum9=0
sum10=0
sum11=0
sum12=0
sum13=0


if num>=1000:
    while (num>=1000):
        sum=sum+1
        num=num-1000
if num>=900:
    while (num>=900):
        sum2=sum2+1
        num=num-900
if num>=500:
    while (num>=500):
        sum3=sum3+1
        num=num-500
if num>=400:
    while (num>=400):
        sum4=sum4+1
        num=num-400
if num>=100:
    while (num>=100):
        sum5=sum5+1
        num=num-100
if num>=90:
    while (num>=90):
        sum6=sum6+1
        num=num-90
if num>=50:
    while (num>=50):
        sum7=sum7+1
        num=num-50
if num>=40:
    while (num>=40):
        sum8=sum8+1
        num=num-40
if num>=10:
    while (num>=10):
        sum9=sum9+1
        num=num-10
if num>=9:
    while (num>=9):
        sum10=sum10+1
        num=num-9
if num>=5:
    while (num>=5):
        sum11=sum11+1
        num=num-5
if num>=4:
    while (num>=4):
        sum12=sum12+1
        num=num-4
if num>=1:
    while (num>=1):
        sum13=sum13+1
        num=num-1

print(sum* 'M')+(sum2*'CM')+  (sum3*'D') + (sum4*'CD') + (sum5*'C')  +(sum6*'XC') + (sum7*'L')+  (sum8*'XL')+  (sum9*'X') + (sum10*'IX') + (sum11*'V')  +(sum12*'IV') + (sum13*'I')          
