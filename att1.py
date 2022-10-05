def quadrante(x,y):
        if(x >= 1 and y >= 1):
            print("Primeiro quadrante")
        elif(x < 0 and y > 0):
            print("Segundo quadrante")
        elif(x < 0 and y < 0):
            print("Terceiro quadrante")
        elif(x >= 1 and y < 0):
            print("Quarto quadrante")
        else:
            print("Números nulos são inválidos")

x = int(input("Informe uma cordenada X: "))
y = int(input("Informe uma cordenada Y: "))
quadrante(x,y)



