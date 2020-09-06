#!/usr/bin/env python
# coding: utf-8

# In[61]:


def Factorial(n):
    #condiciones:
    if n<0:
        return('solo se permiten numeros positivos ó 0')
    if n!=int(n):
        return('el numero ingresado no es un entero')
    #funcion:
    k=1
    p=1

    while k<=n:
        p=k*p  #valor que guarda el numero anterior
        k=k+1  #contador y valor que aumenta
    return(p)


# In[62]:


def Binomial(n,k):
    #condiciones
    if n<0 or k<0:
        return('alguno de los datos ingresados es negativo')
    if n<k:
        return('datos ingresados de forma incorrecta')
    if n!=int(n) or k!=int(k):
        return('alguno de los numeros ingresados no es entero')
    #funcion
    b=Factorial(n)/(Factorial(k)*Factorial(n-k)) #formula
    
    return(int(b)) #retorna el numero como un entero


# In[60]:


def Pascal(n):
    # condiciones:
    if n<=0:
        return('solo se permiten numeros mayores a 1') # esto porque no tiene sentido 0 lineas, la linea n=0 corresponde a 1
    if n!=int(n):
        return('el numero ingresado no es un entero')
    # funcion:
    lista=[]   #lista donde van almacenados los archivos de pascal
    archivo=open("Pascal-n.txt","w")  #abre el archivo
    for i in range(0,n):
        vaca=[] #sublista que se reinicia para cada valor de n
        k=0 #contador
        #esctritura en el archivo 
        archivo.write("n = ") 
        archivo.write(str(i))
        archivo.write("   ")
        #este while es el contador de k para cada valor de n
        while k<=i:
            vaca.append(Binomial(i,k)) #sub lista 
            archivo.write(str(Binomial(i,k))) #escribe en el archivo el valor del binomial en forma de caracter
            if k!=i: #solo para estetica en el archivo
                archivo.write("  ") 
            k=k+1 # cpmtador
        archivo.write("\n\n") #estetica en el archivo
        lista.append(vaca) #lista de los valores del triangulo, esta compuesta por sublista "vaca"
    archivo.close() #cierra el archivo
    return
    
    


# In[ ]:




