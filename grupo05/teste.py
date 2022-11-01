from threading import Thread

def ler(p,f):
    with open(f, 'r', encoding='utf_8') as f1:
        n = 0
        for linha in f1:
            if p in linha:
                print(linha)
                n +=1
    print(str(n) + " linhas tiveram a palavra pesquisada")




def receive(p,f):
    for i in f:
        newT = Thread(target = ler,args = (p,i))
        newT.start()
        newT.join()

receive("cai",["teste.txt","teste2.txt"])
