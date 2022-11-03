from threading import Thread
import sys

def receive(p,f,c1,l1,pn1,t1,e1):
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
            for linha in f2:
                if p2 in linha:
                    line += 1
                    print(linha)
                    n += 1
        if c2 == True:
            print(str(n) + " ocorrencias da palavra pesquisada") #bug de 2 ocorrencias na mesma linha
        if l2 == True:
            print(str(l) + " linhas tiveram ocorrencia da palavra pesquisada")
#-----------------------------------------------------------------------------------------
    if pn == False:
        for f1 in f:
            ler(p,f1,c11,l11)
    else:
        if t1 == True:
            for f1 in f: #no clue how to make multi threading in a way that actually uses multiple files and joins them correctly (pn)
                newT = Thread(target = ler,args =(p,f1,c11,l11)) #pn é quantas threads ao mesmo tempo ou total ??????
                newT.start()
                newT.join()
        else:
            for _ in f: #substitui para f2
                pass
                #fazer o fork para processos

#receive("cai",["teste.txt","teste2.txt"])

if __name__ == '__main__':
    tudo = list(sys.argv)
    if "-c" in tudo:
        c = True
    else:
        c = False
    if "-l" in tudo:
        l = True
    else: 
        l = False
    if "-p" in tudo:
        for i in tudo:
            if i == "-p":
                pn = int(tudo[i+1])
    else:
        pn = False
    if "-t" in tudo:
        t = True
    else: 
        t = False
    if "-e" in tudo:
        e = True
    else: 
        e = False
    receive(sys.argv[-2],sys.argv[-1],c,l,pn,t,e)
