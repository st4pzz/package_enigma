import numpy as np


#implementando alfabeto e encoder
alfabeto = 'abcdefghijklmnopqrstuvwxyz ãé,.'
alfabeto_identidade = np.identity(len(alfabeto))
encoder = np.roll(alfabeto_identidade,-2,1)
segundo_encoder = np.roll(alfabeto_identidade,7,1)

#Uma função para_one_hot(msg : str) para codificar mensagens como uma matriz usando one-hot encoding
def para_one_hot(msg: str):
    lista = list()
    for a in msg:
        i = alfabeto.index(a)
        lista.append(alfabeto_identidade[i])
    lista= np.array(lista)
    return lista.T
   
#Uma função para_string(M : np.array) para converter mensagens da representação one-hot encoding para uma string legível
def para_string(M : np.array):
    saida = ''
    M = M.T
    for lista in M:
        saida += alfabeto[ np.where(lista == 1)[0][0] ]
    return saida

#Uma função cifrar(msg : str, P : np.array) que aplica uma cifra simples em uma mensagem recebida como entrada e retorna a mensagem cifrada. P é a matriz de permutação que realiza a cifra.
def cifrar(msg: str,P : np.array):
    msg = para_one_hot(msg)
    msg_cifrada = P @ msg
    return para_string(msg_cifrada)

#Uma função de_cifrar(msg : str, P : np.array) que recupera uma mensagem cifrada, recebida como entrada, e retorna a mensagem original. P é a matriz de permutação que realiza a cifra.
def de_cifrar(msg: str,P : np.array):
    msg = para_one_hot(msg)
    
    msg_decifrada = np.linalg.solve(P,msg)
    return para_string(msg_decifrada)

#Uma função enigma(msg : str, P : np.array, E : np.array) que faz a cifra enigma na mensagem de entrada usando o cifrador P e o cifrador auxiliar E, ambos representados como matrizes de permutação.
def enigma(msg: str, P : np.array, E : np.array):
    tamanho = len(msg)
    msg = para_one_hot(msg)
    lista = list()
    for i in range(tamanho):
        j = msg[:,i].T
        a = P@j
        for _ in range(i+1):
            a = E@a
        lista.append(a)
    enigma = np.array(lista).T
    return para_string(enigma)

#Uma função de_enigma(msg : str, P : np.array, E : np.array) que recupera uma mensagem cifrada como enigma assumindo que ela foi cifrada com o usando o cifrador P e o cifrador auxiliar E, ambos representados como matrizes de permutação.
def de_enigma(msg: str, P : np.array, E : np.array):
    tamanho = len(msg)
    msg = para_one_hot(msg)
    lista = list()
    e_ = np.linalg.inv(E)
    p_ = np.linalg.inv(P)
    for i in range(tamanho):
        j = msg[:,i].transpose()
        for _ in range(i+1):
            j = e_@j
        a = p_@j
        lista.append(a)
    de_enigma = np.array(lista).T
    return para_string(de_enigma)