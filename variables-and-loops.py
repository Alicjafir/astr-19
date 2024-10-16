import numpy as np

def main():
    i = 0 #integers can be decleared witha number
    n = 10 # here is another integer
    x = 19.0 # floating point numbers have a "."

    #we can use numpy todeclare arrays quickly
    y = np.zeros(n, dtype=float) #10 0's as floats
    
    # we can use for loops to iterate a variable
    for i in range(n): # i in range [0,n-1]
        y[i] = 2.0 * float(i) + 1. # y = 2i+2
        
    # we can also simply iterate through a variable 
    for y_element in y:
        print(y_element)
        
#execute a main function
if __name__=="__main__":
    main()
    