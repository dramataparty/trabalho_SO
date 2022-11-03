import fileinput
from threading import Thread
import sys,os

def receive(p,f,c1,l1,pn1,e1):
    global linhas = []
    global ocorrencias = []
    global nlinhas = []
    if c1 == True:
        c11 = True
    else:
        c11 = False

    if l1 == True:
        l11 = True
    else:
        l11 = False
#------------------------------------------------------------------------------------------
    def ler(p2,f2,c2,l2):
        with open(f, 'r', encoding='utf_8') as f2:
            n = 0
            line = 0
            lines = []
            for linha in f2:
                if p2 in linha:
                    line += 1
                    lines = lines + [linha]
                    n += 1
            linhas = linhas + [lines]
            if c2 == True:
                ocorrencias = ocorrencias + [n]
            if l2 == True:
                nlinhas = nlinhas + [line]
#-----------------------------------------------------------------------------------------
    if pn == 1:
        for f1 in f:
            ler(p,f1,c11,l11)
    else:
            pass
            #for f1 in f: 
                
                #no clue how to make multi threading in a way that actually uses multiple files and joins them correctly (pn)
                #glob??? será q funciona???
                #newT = Thread(target = ler,args =(p,f1,c11,l11,)) #pn é nº de threads a fazer a paralelizaçao, em geral o nº total e simultaneo sao iguais
                #newT.start()
                #newT.join()
    for i in range(len(f)):
        i2 = i + 1
        print("o ficheiro nº " + i2 + " contem as seguintes linhas:")
        print(linhas[i])
        print("o numero total de ocorrencias da palavra neste ficheiro foram " + ocorrencias[i])
        print("o numero total de linhas com esta palavra neste ficheiro foram " + nlinhas[i])
        
#receive("cai",["teste.txt","teste2.txt"])

if __name__ == '__main__':
    tudo = list(sys.argv)
    c = False
    l = False
    pn = 1
    t = False
    e = False
    if "-c" in tudo:
        c = True
    if "-l" in tudo:
        l = True
    if "-p" in tudo:
        for i in tudo:
            if i == "-p":
                pn = int(tudo[i+1])
    if "-e" in tudo:
        e = True
        #suposto dividir o ficheiro e fazer multi/paralelização a cada uma das partes individualmente
        #ver os.stat() e file.readlines()    
        #dividir por linhas ou em mini ficheiros??????
    receive(sys.argv[-2],sys.argv[-1],c,l,pn,e)



#Testes da metodos de split
#for count,line in f1:
    #enumerate(f1)

#count = count+1

