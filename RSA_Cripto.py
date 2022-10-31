from ast import Return
import random

#Yuri linha 5 até 31
def ValidaPrimo(P):
    for i in range(1, P):
        if (i != 1 and i != P) :
            if (P % i == 0) :
                
                return True 
    return False



# Entrada de Dois dados P e Q 
Validador = True
while(Validador): 
    P = int (input('Valor 1; '))
    Q = int (input('Valor 2; '))
    if(ValidaPrimo (P)):
        print(f'O valor {P} não é primo ')
    if(ValidaPrimo (Q)):
        print(f'O valor {Q} não é primo ')
    Validador = ValidaPrimo(P) or ValidaPrimo(Q)

# Calculo de N 
N = P * Q

# Calculo de Z
Z = (P-1) * (Q - 1)

# Noah linha 34 até 72

# Calculo D


    # Lista de Valores

dLista = []

mdcCompleto = False

for i in range (2, Z - 1) :
    for j in range(2, i - 1) :
        if(Z % j == 0) and (i % j == 0) :
            mdcCompleto = False
            break
        else :
            mdcCompleto = True

    if (mdcCompleto) :
        dLista.extend([i])
        
D = dLista [random.randint(0, len(dLista)-1)]

# Calculo E
eLista = []

for i in range(1, Z*100):
    if(((i * D) % Z) == 1):
        eLista.extend([i])

E = eLista[random.randint(0, len(eLista)-1)]

# O algorito suporta valores da tabela ascii 1 até 220; 
    # ou seja nada de acentos em letras maiusculas

# Lendo Arquivos
fileR = open('texto.txt', 'r')

# Lendo o Conteutdo
fileTXT = fileR.read()

# Caio linha 75 até 101 
# Criptpgrafia

txtCriptografado = ''
for i in range(len(fileTXT)) :
    print(fileTXT[i].upper())
    txtCriptografado += str(ord(fileTXT[i].upper()) ** E % N) 
    txtCriptografado += ' '

#Guarda Msg Criptogravada
Arquivo = open('MensagemCriptografada.txt', 'w')
Arquivo.write(txtCriptografado)
Arquivo.close()

#Chaves Publicas
Chaves = open('ChavesPublicas.txt', 'w')
Chaves.write('Chaves \nE: {} \nN: {}'.format(E, N))
Chaves.close()

#Chaves Privadas
Chaves = open('ChavesPrivadas.txt', 'w')
Chaves.write('Chaves \nD: {} \nN: {}'.format(D, N))
Chaves.close()


Chaves = open('Valores Calculados.txt', 'w')
Chaves.write('Calculados \nP: {} \nQ: {} \nN: {} \nZ: {} \nD: {} \nE: {}'.format(P, Q, N, Z, D, E))
Chaves.close
