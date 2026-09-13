#Celsius to Fahrenheit & vice-versa
def C2F():
    a=int(input("Enter 1 to convert Celsius to Fahrenheit, Enter 2 to convert Fahrenheit to Celsius"))
    if a==1:
        C=float(input("Enter the Celcius value"))
        C_F=(C*9/5)+32
        print("Fahrenheit value:",C_F)
        
    if a==2:
        F=float(input("Enter the Fahrenheit value"))
        F_C=(F-32)*5/9
        print("Celsius value:",F_C)

C2F()        
