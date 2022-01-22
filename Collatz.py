import numpy as np
import matplotlib.pyplot as plt

llista=[]
llistes=[]
max_elements=0
valor_maxim=0
valor_del_maxim=0

#informacio[0]=valorMaxim, informacio[1]=element que l'ha generat
informacio=[0,0]       

iteracions=[]

# Funció de Collatz (definició recursiva)
def f(x,llista,informacio):
    llista.append(x)
    x_even=x/2;
    x_odd=3*x+1
    if (x>=informacio[0]):
        informacio[0]=x
        informacio[1]=llista[0]
        
    if (x==1):
        return
    else:
        if (x % 2 != 0):
            f(x_odd,llista,informacio)
        else:
            f(x_even,llista,informacio)
            
# Calculem un rang de valors            
def rangF(minim,maxim,llista,llistes,informacio):            
    for x in range(minim,maxim):
        f(x,llista,informacio)
        iteracions.append(len(llista))
        llistes.append(llista)
        llista=[]
        
# Dibuixem un rang de valors
def drawRang():
    f, axes = plt.subplots()
    for i in range(len(llistes)):
       axes.plot(llistes[i])
    
    f, axes = plt.subplots()   

    axes.plot(iteracions,linestyle="",marker=".")
    plt.show()


rangF(1,16383,llista,llistes,informacio)
drawRang()
f(3071,llista,informacio)
# Imprimim informació
print("Valor màxim:"+str(informacio[0])
      +" assolit per x="+str(informacio[1])
      +" en "
      + str(len(llista))
      +" iteracions:\n"+str(llista))



