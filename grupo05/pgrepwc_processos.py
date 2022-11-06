### Grupo: SO-TI-05
### Aluno 1: Diogo Forte (fc56931)
### Aluno 2: Tiago Ramalho (fc58645)


import sys
import os

def main(Rword,Rfiles,Rc,Rl,Rpn,Re):
    linhas = []
    if Rc == True:
        ocorrencias = []           #Esta parte do codigo está encarregada de criar variaveis globais que vao ser utilizadas
    if Rl == True:                 #pelas threads para no final o processo pai imprimir cada valor ele proprio (é obrigatorio que apenas o processo pai imprima)
        nlinhas = []
    print('Programa: pgrepwc_processos.py')
    print('Argumentos: ',Rword,Rfiles,Rc,Rl,Rpn,Re)

#------------------------------------------------------------------------------------------

    def ler(Lword,Lfiles,Lc,Ll):
            for Lfile in Lfiles:
                with open(Lfile, 'r', encoding='utf_8') as file:
                    n = 0
                    nline = 0
                    lines = []
                    linhas = []
                    ocorrencias=[]
                    nlinhas=[]
                    for linha in file:
                        palavras = linha.split()
                        if Lword in palavras:                              #Função encarregada de ler varios ficheiros e adicionar as linhas encontradas
                            nline += 1                                     #na variavel global "Linhas" e adicionar as ocorrencias e Nº de linhas 
                            lines = lines + [linha]                        #nas suas respetivas variaveis globais. cada thread vai ter a sua lista de
                            for palavra in palavras:                       #ficheiros, e vai coloca la nesta funçao, por isso esta funçao ja le varios por default.
                                if palavra == Lword:
                                    n += 1
                    linhas = linhas + [lines]
                    if Lc == True:
                        ocorrencias = ocorrencias + [n]
                    if Ll == True:
                        nlinhas = nlinhas + [nline]
                    
   
    if Rpn == 1:                                   
            ler(Rword,Rfiles,Rc,Rl)
    else:
        ls = []                                   
        for _ in range(Rpn):                       
            ls = ls + [[]]                         
        nxt = 0                                     
        for f in Rfiles:                           
            ls[nxt] = ls[nxt] + [f]
            nxt = (nxt + 1) % Rpn
        for t in range(Rpn):
            newps = os.fork()                 
            if newps == 0:
                ler(Rword,ls[t],Rc,Rl)
            else:
                os.wait()
                    
            for _ in range(Rpn):                                                        
                os.execl()
                
    for i2 in range(len(Rfiles)-1):
        i3 = i2 + 1
        print("o ficheiro nº " + str(i3) + " contem as seguintes linhas:")                                      #esta parte esta encarregada de dar print a "tudo"
        print(linhas[i2])                                                                                   #mas se o utilizador nao colocar -c ou -l 
        if Rc == True:                                                                                     # ele automaticamente nao da print disso.
            print("o numero total de ocorrencias da palavra neste ficheiro foram " + str(ocorrencias[i2]))       #isto está organizado por ficheiro (cada ficheiro N
        if Rl == True:                                                                                     #da print das suas linhas, e depois o ficheiro N+1 faz o 
            print("o numero total de linhas com esta palavra neste ficheiro foram " + str(nlinhas[i2]))



if __name__ == "__main__":
    tudo = list(sys.argv)
    c = False
    l = False
    pn = 1
    e = False
    pal = ""
    if "-c" in tudo:                                            #esta parte está encarregada de receber os argumentos da consola, e verificar se eles estao la (True)
        c = True                                                #ou se nao estao (False)
    if "-l" in tudo:                                            #De momento existe uma questao/problema, que é se os ficheiros sao dados como um argumento(lista de 
        l = True                                                #strings) ou se sao dados como varias strings que nos é que temos de transformar numa lista, se for 
    if "-p" in tudo:                                            #um argumento lista, isto funciona bem, se nao, entao temos de criar a lista nós proprios, eu tenho
        for i in tudo:                                          #uma vaga ideia de como o fazer (procurar por todos os argumentos por os que contem ".txt" neles),
            if i == "-p":                                       #mas ainda estava a espera da resposta dos professores para ter a certeza se isto era ou nao necessario.
                pn = int(tudo[i+1])
    if "-e" in tudo:
        e = True
    ficheiros = []
    for x in tudo:                                              #para todos os argumentos, os que tiverem ".txt" sao os ficheiros
        if ".txt" in x:
            ficheiros = ficheiros + x  
        for x1 in range(len(tudo)):
            if ".txt" in tudo[x1]:
                pal = tudo[x1-1]
    main(pal,ficheiros,c,l,pn,e)