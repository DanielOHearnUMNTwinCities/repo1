

import math


def poiseuille(L,r,η):

    
             
          L=float(L)
          r=float(r)
          η=float(η)
         
          
          if float(L)>0 and float(r)>0 and float(η)>0 : 
            
              #π = ~3.1415926535897932384626433832795
              π = math.pi
              R = (8*η*L)/(π*r**4)
              return R
             
            
          else: 
              print("Please enter a positive value for each variable")
              
def main():
    
        L= float(input("Please enter the length: "))
        r= float(input("Please enter the radius: "))
        η= float(input("Please enter the viscosity: "))
       
        if float(L)>0 and float(r)>0 and float(η)>0 : 
        
             R=poiseuille(L,r,η)
             print(R,"is the resulting resistance") 
        else: 
             print("\nFailed due to input error. Please make sure your inputs are all positive. Exiting program.")
             
             return
                 
main()
            
        
#R is the resistance 
#r is the tube radius
#η is the viscosity
#L in the tube length 
    

     

