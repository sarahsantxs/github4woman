import math
a = float (input("Informe o valor de a:"))
b = float (input("Informe o valor de b:"))
c = float (input("Informe o valor de c:"))

delta = math.pow(b,2)-4*a*c

if delta<0 or a==0 : print ("Valor do delta incorreto.") 
else:
    raiz1= (-b+math.sqrt(delta))/(2*a)
    raiz2= (-b-math.sqrt(delta))/(2*a)

print ("Valor da primeira raiz calculada:" , raiz1)
print ("Valor da segunda raiz calculada:" , raiz2)