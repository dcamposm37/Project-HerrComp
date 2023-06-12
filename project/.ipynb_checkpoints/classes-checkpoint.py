import numpy as np

class body():
    
    def __init__(self, mass, position, velocity): 
        self.mass = mass
        self.diamether = mass**(1/3)
        self.position = np.array(position)
        self.velocity = np.array(velocity)
        
        return 0
    
    def __add__(self, other):
        mass = self.mass + other.mass
        return body(mass, (self.mass*self.position + self.mass*self.position)/mass, (self.mass*self.velocity + self.mass*self.velocity)/mass)
        