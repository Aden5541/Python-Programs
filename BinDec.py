#Binary to Decimal
#a=Binary value, b=Decimal value, e=Exponent

a=input("Enter a binary value:")
b=0
e=0

for i in reversed(a):
    b+=int(i)*(2**e)
    e+=1
print(b)

#_____________________________________________________________________________________________________________________________________________________________

#Decimal to Binary
#x=Decimal value, y=Binary value, r=Remainder

x=int(input("Enter a Decimal value:"))
y=""

while x>0:
    r=x%2
    y+=str(r)
    x//=2
print(y[::-1])    

