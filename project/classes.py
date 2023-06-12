import numpy as np

class body():
    
    def __init__(self, mass, position, velocity): 
        self.mass = mass
        self.diamether = mass**(1/3)
        self.position = np.array(position)
        self.velocity = np.array(velocity)
        
        return None
    
    #When two bodies merge
    def __add__(self, other):
        mass = self.mass + other.mass
        return body(mass, (self.mass*self.position + other.mass*other.position)/mass, (self.mass*self.velocity + other.mass*other.velocity)/mass)
    
    #Print    
    def __repr__(self):
        return r"m=%.2f, r=[%.2f, %.2f, %.2f], v=[%.2f, %.2f, %.2f]"%(self.mass, self.position[0], self.position[1], self.position[2], self.velocity[0], self.velocity[1], self.velocity[2])

    def speed(self):
        return np.linalg.norm(self.velocity)


class universe():

    def __init__(self, bodys, G, dt):
        self.bodys = bodys
        self.G = G
        self.dt = dt
        self.time = 0

    #Print
    def __repr__(self):

        data = ""
        
        for body in self.bodys:
            data += "{}, {}, {}, {}, {}, {}, {}\n".format(body.mass, body.position[0], body.position[1], body.position[2], body.velocity[0], body.velocity[1], body.velocity[2])

        return data

    #Create a dictionary with the universe data
    def data(self):

        return {'mass':[body.mass for body in self.bodys], 'x':[body.position[0] for body in self.bodys], 'y':[body.position[1] for body in self.bodys], 'z':[body.position[2] for body in self.bodys], 'vx':[body.velocity[0] for body in self.bodys], 'vy':[body.velocity[1] for body in self.bodys], 'vz':[body.velocity[2] for body in self.bodys]}

    #Put a new body in the universe
    def put(self, body):
        self.bodys.append(body)
