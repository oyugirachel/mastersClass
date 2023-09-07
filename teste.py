# i = 5

# while(i > 0):

#      i = i + 1

#      print("%d ", i)

def fib(x):

    if(x == 0 or x == 1):

        return x

    else:

        return fib(x-2) + fib(x-1)



n = 7

resultado = fib(n)

print(resultado)

m=[]

m.append(["","",""])

m.append(["1","3","5"])

m.append(["2","4","6"])

for i in range(1,3):

    for j in range(1,3):

        print(m[j][i])



resto=0

Numero=int(input("Digite um número inteiro:"))

resto = Numero % 2

if (resto == 0):

    print("Condição satisfeita.\n")

else:

    print("Condição não Satisfeita.\n")


A=int(174)

B=int(2)

C=float()

C = A / B

print (A," / ", B, " = ", C)