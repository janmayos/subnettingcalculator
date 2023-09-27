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
    clasebits = {"A":"00000000.00000000.00000000","B":"00000000.00000000","C":"00000000"}
    listbits = getbinario(bitsprestados,clase)
    #print("IP: ",ip)
    ipsplit = ip.split(".")
    #print(ipsplit)
    listasegmentos = []
    if clase == "C":
        ultimo = []
        ban = False
        for combinacionesip in listbits:
            
            #print(combinacionesip + " :  "+str(binario_a_decimal(combinacionesip)))
            if ban:
                ultimo.append(binario_a_decimal(combinacionesip)-1)
                listasegmentos.append(ultimo)
                ultimo = [ipsplit[0],ipsplit[1],ipsplit[2],combinacionesip,binario_a_decimal(combinacionesip)]
            else:
                ultimo = [ipsplit[0],ipsplit[1],ipsplit[2],combinacionesip,binario_a_decimal(combinacionesip)]
                ban = True
        ultimo.append(255)
        listasegmentos.append(ultimo)
    elif clase == "B":
        ultimo = []
        ban = False
        for combinacionesip in listbits:
            combinacionesipuno = combinacionesip[0:8]
            combinacionesipdos = combinacionesip[8::]

            print(combinacionesip+ "   " +combinacionesipuno+"."+combinacionesipdos + " :  "+str(binario_a_decimal(combinacionesipuno)) + " :  "+str(binario_a_decimal(combinacionesipdos)))
            if ban:
                if combinacionesipdos.find("1") != -1:
                    ultimo.append(str(binario_a_decimal(combinacionesipuno)-1)+"."+str(binario_a_decimal(combinacionesipdos)-1))
                else:
                    ultimo.append(str(binario_a_decimal(combinacionesipuno)-1)+".255")
                listasegmentos.append(ultimo)
                ultimo = [ipsplit[0],ipsplit[1],combinacionesipuno+"."+combinacionesipdos,str(binario_a_decimal(combinacionesipuno))+"."+str(binario_a_decimal(combinacionesipdos))]
            else:
                ultimo = [ipsplit[0],ipsplit[1],combinacionesipuno+"."+combinacionesipdos,str(binario_a_decimal(combinacionesipuno))+"."+str(binario_a_decimal(combinacionesipdos))]
                ban = True
        ultimo.append("255.255")
        listasegmentos.append(ultimo)
    elif clase == "A":
        ultimo = []
        ban = False
        for combinacionesip in listbits:
            combinacionesipuno = combinacionesip[0:8]
            combinacionesipdos = combinacionesip[8:16]
            combinacionesiptres = combinacionesip[16::]    
            print(combinacionesip+ "   " +combinacionesipuno+"."+combinacionesipdos +"."+combinacionesiptres + " :  "+str(binario_a_decimal(combinacionesipuno)) + " :  "+str(binario_a_decimal(combinacionesipdos)) + " :  "+str(binario_a_decimal(combinacionesiptres)))
            if ban:
                print(binario_a_decimal(combinacionesipuno)-1)
                if bitsprestados > 0 and bitsprestados <=8:    
                    ultimo.append(str(binario_a_decimal(combinacionesipuno)-1)+".255.255")
                elif bitsprestados > 8 and bitsprestados <=16:
                    if binario_a_decimal(combinacionesipuno)-1 != -1:
                        ultimo.append(str(binario_a_decimal(combinacionesipuno)-1)+"."+str(binario_a_decimal(combinacionesipdos)-1)+".255")
                    else:
                        ultimo.append(str(binario_a_decimal(combinacionesipuno))+"."+str(binario_a_decimal(combinacionesipdos)-1)+".255")
                listasegmentos.append(ultimo)
                ultimo = [ipsplit[0],combinacionesipuno+"."+combinacionesipdos+"."+combinacionesiptres,str(binario_a_decimal(combinacionesipuno))+"."+str(binario_a_decimal(combinacionesipdos))+"."+str(binario_a_decimal(combinacionesiptres))]
            else:
                ultimo = [ipsplit[0],combinacionesipuno+"."+combinacionesipdos+"."+combinacionesiptres,str(binario_a_decimal(combinacionesipuno))+"."+str(binario_a_decimal(combinacionesipdos))+"."+str(binario_a_decimal(combinacionesiptres))]
                ban = True
        ultimo.append("255.255.255")
        listasegmentos.append(ultimo)

    return listasegmentos



def aux_binario(decimal):
    binario = 0
    i = 0
    while (decimal>0):
        digito  = decimal%2
        decimal = int(decimal//2)
        binario = binario+digito*(10**i)
        i = i+1

    return binario

def binario_a_decimal(binario):
    posicion = 0
    decimal = 0
    # Invertir la cadena porque debemos recorrerla de derecha a izquierda
    binario = binario[::-1]
    for digito in binario:
        # Elevar 2 a la posición actual
        multiplicador = 2**posicion
        decimal += int(digito) * multiplicador
        posicion += 1
    return decimal

def getbinario(bitsprestados,clase):
    bitsdisp = {"A":24,"B":16,"C":8}
    listabinario = []
    maxdecimal = pow(2,bitsprestados)
    print(maxdecimal)
    binario = 0
    i = 0
    for numdecimal in range(maxdecimal):
        decimal = numdecimal
        aux__binario = str(aux_binario(decimal))
        for ceros in range(bitsprestados-len(aux__binario)):
            aux__binario = "0"+aux__binario     
        
        for ceros in range(bitsdisp[clase]-len(aux__binario)):
            aux__binario = aux__binario+"0"
        
        listabinario.append(aux__binario)
    return listabinario

dictclase = {
    "A" : (1,126,24,"1.0.0.0","126.0.0.0"),
    "B" : (128,191,"128.0.0.0","191.255.0.0"),
    "C" : (193,223,"192.0.0.0","223.255.255.0")
}

ip = "32.0.0.0"
numredes = 1025
clase = get_clase(ip,dictclase)
print(clase)
bitsprestados = get_bits_prestados(numredes,clase)
print(bitsprestados)
for subneteo in genera_tablasubeteo(clase,ip,bitsprestados):
    print(subneteo)