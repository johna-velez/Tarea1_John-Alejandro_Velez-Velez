#!/usr/bin/env python
# coding: utf-8

# In[1]:


from funciones import *


# In[2]:


# a) tirado 100 veces salga 10 veces cara
n=100  # numero de veces que se lanza la moneda 
k=3   # numero de veces para que caiga cara  

p=Binomial(n,k)/2**n # expresion dada para la probabilidad

print('a) la probabilidad de que tirando la moneda',n,'veces, salga',k,'veces cara es de:',p )


# In[3]:


# b) 
t=0 # sera el contador para el numero de formas en las que puede caer cara
n=100  # numero de veces que se lanza la monda 
k=30 # limite inferior para el numero de formas en las que puede caer la moneda

for i in range(k+1,n+1): # contador que nos suma las posibles manera en la que sale 
    m=Binomial(n,i) # formas en las que puede salir i-veces cara tirandolo n veces 
    t=m+t #formas de que salga cara un numero mayor a k veces
pk=t/2**n #probabilidad en las que puede puede caer mas de k veces si se tira n veces

print('b )la probabilidad que caiga cara mas de',k,'veces, tirandolo',n,'veces, es de:',pk)


# In[4]:


#imprime en un archivo el triangulo de pascal con 4 filas, esto es hasta n=3, si se quiere variar cambiar el numero, solo cambiar n

n=4
Pascal(n)

