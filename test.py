#!/usr/bin/env python
# coding: utf-8

# In[1]:


from funciones import *


# In[24]:


f0=Factorial(0)
f1=Factorial(1)
f4=Factorial(4)
b00=Binomial(0,0)
b10=Binomial(1,0)
b53=Binomial(5,3)

print('los valores fueron comparados con wolfram alpha, en la primer columna estan los valores de wolfram y en la segunda los valores de nuestra funcion')

print('\nfactorial:\n')
print('wolfram     valor funcion')
print('0!:',1,'         ',f0)
print('1!:',1,'         ',f1)
print('4!:',24,'        ',f4)
print('\nbinomial:\n')
print('wolfram     valor funcion')
print('B(0,0):',1,'        ',b00)
print('B(1,0):',1,'        ',b10)
print('B(5,3):',10,'       ',b53)

print('\npara el triangulo de pascal comparar el archivo pascal-n.txt, en este caso para 7 filas.')
Pascal(7)


# In[ ]:




