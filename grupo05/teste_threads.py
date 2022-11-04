from threading import Thread
import sys
#------------------------------------------------------------------------------------------
def receive(Rword,Rfiles,Rc,Rl,Rpn,Re):
    linhas = []
    if Rc == True:
        ocorrencias = []
    if Rl == True:
        nlinhas = []
#------------------------------------------------------------------------------------------
    def ler(Lword,Lfiles,Lc,Ll):
        for Lfile in Lfiles:
            with open(Lfile, 'r', encoding='utf_8') as file:
                n = 0
                line = 0
                lines = []
                for linha in file:
                    if " " + Lword + " " in linha:
                        line += 1
                        lines = lines + [linha]
                        n += 1
                linhas = linhas + [lines]
                if Lc == True:
                    ocorrencias = ocorrencias + [n]
                if Ll == True:
                    nlinhas = nlinhas + [line]
#-----------------------------------------------------------------------------------------
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
            newT = Thread(target = ler,args =(Rword,ls[t],Rc,Rl,))
            newT.start()
        for _ in range(Rpn):
            newT.join()
#-----------------------------------------------------------------------------------------
    for i2 in range(len(Rfiles)):
        i3 = i2 + 1
        print("o ficheiro nº " + i3 + " contem as seguintes linhas:")
        print(linhas[i])
        if Rc == True:
            print("o numero total de ocorrencias da palavra neste ficheiro foram " + ocorrencias[i])
        if Rl == True:
            print("o numero total de linhas com esta palavra neste ficheiro foram " + nlinhas[i])
#------------------------------------------------------------------------------------------
if __name__ == '__main__':
    tudo = list(sys.argv)
    c = False
    l = False
    pn = 1
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
    receive(sys.argv[-2],sys.argv[-1],c,l,pn,e)
