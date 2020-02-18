# Find the minimum number of cuts to  
# pay the worker. 
  
import math 
 
def pay(n): 
      
    # Nearest Integer to the Log value of the number n 
    cuts = int(math.log(n, 2))   
    return cuts 
      
if __name__ == "__main__":  #still learning this as a necessity
    n = 9
    cuts = pay(n) 
    print(cuts) 
    
    # 2 examples
    n = 29
    cuts = pay(n) 
    print(cuts)
