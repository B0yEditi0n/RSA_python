#Descriptografa arquivo
arquivoCriptografado = open('MensagemCriptografada.txt', 'r')
fileTXT = arquivoCriptografado.read()
arquivoCriptografado.close()

# Entrar Com as Chaves
D = int(input('Entre com o valor de D: '))
N = int(input('Entre com o valor de N: '))

# Descriptografia
txt_int = ''
txtDescipt = ''
i = 0
while i <= len(fileTXT)-1 :
    if (fileTXT[i] != ' ') :

        txt_int += str(fileTXT[i])
    else :

        txtDescipt += chr(int(txt_int) ** D % N) 
        txt_int = ''

    i = i + 1


print(txtDescipt)