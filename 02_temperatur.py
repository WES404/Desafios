def main():
    print("Converte para F, K e C\n")

    de = input("DE: ")
    para = input("PARA: ")

    de = de.upper()
    para = para.upper()
    nomes = ["F", "C", "K"]
    if de not in nomes or para not in nomes:
        print("Unidade não existente! Tente de novo")

    valor = float(input("Temperatura: "))

    if para == "F":
        if de == "C":
            k = 0
        else:
            k = 1
        temp =  FEHREINHEIT(valor, k)
        print(f"{valor}{de} para {para} é igual a: {temp}{para}")
    
    elif para == "K":
        if de == "F":
            k = 0
        else:
            k = 1
        temp = KELVIN(valor, k)
        print(f"{valor}{de} para {para} é igual a: {temp}{para}")

    else:
        if de == "F":
            k = 0
        else:
            k = 1
        temp = Celsius(valor, k)
        print(f"{valor}{de} para {para} é igual a: {temp}{para}")



def FEHREINHEIT(t, k):
    if k == 0:
        F = t * 1.8 + 32
    else:
        F = t * 1.8 - 459.67
    return F

def KELVIN(t, k):
    if k == 0:
        K = (t + 459.67) / 1.8
    else:
        K = t + 273.15
    return K

def Celsius(t, k):
    if k == 0:
        C = (t - 325) / 1.8
    else:
        C = t - 273.15
    return C

main()
