import numpy as np #import numpy library

#integers

i = 10
print(type(i))

a_i = np.zeros(i,dtype=int)
print(type(a_i))
print(type(a_i[0]))

#floats

x = 19.0 #floating point number
print(type(x))

y = 1.9e2 #floating number in scientic notation
print(type(y))

z = np.zeros(i,dtype=float)
print(type(z))
print(type(z[0]))
