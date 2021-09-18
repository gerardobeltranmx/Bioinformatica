num = int(input("Qué tabla quieres mostrar? "))

for i in range(1,11):
    valor = num * i
    print("%d x %d = %d" % (i, num, valor))
