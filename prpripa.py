with open('input.txt','r')as f:
    x=list(eval(f.readline()))
with open('output.txt','w')as f:
    f.write('lista1:'+str(x)+'\n')
    y=sorted(x)
    f.write('lista2:'+str(y)+'\n')
    z=sorted(x, reverse=True)
    f.write('lista3:'+str(z)+'\n')
    len=len(x)
    f.write('lungimea:'+str(len)+'\n')
    min=min(x)
    f.write('MIN: '+str(min)+'\n')
    max=max(x)
    f.write('MAX: '+str(max)+'\n')
    f.write('lista4: '+str(x+[111])+'\n')
    x[1]=222
    f.write('lista5: '+str(x))


 