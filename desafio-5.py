def inverte(sequenciaString):
    invertida = ""
    tamanho = len(sequenciaString)
    for i in range(tamanho-1, -1, -1):
        invertida += sequenciaString[i]
    return invertida

sequenciaString = input("Digite uma string para inverter: ")
print("String invertida:", inverte(sequenciaString))
