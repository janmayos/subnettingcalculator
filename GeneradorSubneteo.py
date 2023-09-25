from itertools import *

def get_clase(ip,dictclase):
    for clase in dictclase:
        valores = dictclase[clase]
        ipsplit = ip.split(".")
        if int(ipsplit[0]) >= valores[0] and int(ipsplit[0]) <=valores[1]:
            return clase
        
#num redes mayor a 1
def get_bits_prestados(numredes,clase):
    bitsdisp = {"A":24,"B":16,"C":8}
    for bits in range(bitsdisp[clase]):
        if numredes <= pow(2,bits)-2:
            return bits

def genera_tablasubeteo(clase,ip,bitsprestados):
    listbits = getbinario(4)
    
    
    return 



def aux_binario(numdecimal,decimal):
    binario = 0
    i = 0
    while (decimal>0):
        digito  = decimal%2
        decimal = int(decimal//2)
        binario = binario+digito*(10**i)
        i = i+1

    return binario
    
def getbinario(bitsprestados):
    listabinario = []
    maxdecimal = pow(2,bitsprestados)
    print(maxdecimal)
    binario = 0
    i = 0
    for numdecimal in range(maxdecimal):
        decimal = numdecimal
        aux__binario = str(aux_binario(numdecimal,decimal))
        for ceros in range(bitsprestados-len(aux__binario)):
            aux__binario = "0"+aux__binario
        listabinario.append(aux__binario)
    return listabinario
dictclase = {
    "A" : (1,126,24,"1.0.0.0","126.0.0.0"),
    "B" : (128,191,"128.0.0.0","191.255.0.0"),
    "C" : (192,223,"192.0.0.0","223.255.255.0")
}

ip = "195.18.3.0"
numredes = 14
clase = get_clase(ip,dictclase)
print(clase)
bitsprestados = get_bits_prestados(numredes,clase)
print(bitsprestados)
print(genera_tablasubeteo(clase,ip,bitsprestados))