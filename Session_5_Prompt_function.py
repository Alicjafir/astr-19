import numpy as np 
from astropy.table import Table
from astropy.io import ascii
from astropy.io import fits


#mytable = Table()

#print(data_in)

def main():
    x = np.linspace(0, 2*np.pi, 1000)            # x = sin(x)
    y = np.sin(x) # create y=[0..2*np.pi] in 1/1000 increments
    
    mytable = Table()
    mytable['x'] = x
    mytable['sin x'] = y
    print(mytable)
    #data = Table([x,y],names=['x','sin x'])
    #print(data)
    #ascii.write(data, 'table.txt', format='comment_header')
    #data_in = ascii.read('table.txt')

if __name__ == "__main__":
    main()

#plt.plot(x,y)            # make a plot
#plt.xlabel('sin(x)')          # label the x axis
#plt.ylabel('x')     # label the y axis
#plt.xlim([0,2*np.pi])
#plt.ylim([-1,1])
#plt.show()               # show the plot on the screen 

#fix the axis ratio
#here are two possible options 
#axarr[0].set_aspect('equal')   #make the ratio of the tick units equal, a bit counter intuitive



