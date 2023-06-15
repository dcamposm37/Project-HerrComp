import numpy as np
from pandas import DataFrame

class body():
    
    def __init__(self, mass, position, velocity): 
        self.mass = mass
        self.diameter = mass**(1/3)
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

    def __init__(self, bodies, G, H, dt):
        self.bodies = bodies[::]
        self.G = G
        self.H = H
        self.dt = dt
        self.time = 0
        self.size = len(self.bodies)

    #Print 
    def __repr__(self):

        data = ""
        
        for body in self.bodies:
            data += "{}, {}, {}, {}, {}, {}, {}\n".format(body.mass, body.position[0], body.position[1], body.position[2], body.velocity[0], body.velocity[1], body.velocity[2])

        return data

    #Create a dictionary with the universe data
    def data(self):

        return DataFrame({'mass':[body.mass for body in self.bodies], 'x':[body.position[0] for body in self.bodies], 'y':[body.position[1] for body in self.bodies], 'z':[body.position[2] for body in self.bodies], 'vx':[body.velocity[0] for body in self.bodies], 'vy':[body.velocity[1] for body in self.bodies], 'vz':[body.velocity[2] for body in self.bodies]})

    #Put a new body in the universe
    def put(self, body):
            self.bodies.append(body)
            self.size += 1

    def destroy(self, body_index):
        self.bodies.pop(body_index)
        self.size -= 1

    #Time evolution
    def evolve(self):

        aux_bodies = self.bodies[::]
        index = np.arange(self.size)

        for ii, body in enumerate(self.bodies):

            #Sume of all forces in the body (Gravitacional froces)
            force = sum([(self.G*body.mass*aux_bodies[body_j].mass/(np.linalg.norm(body.position - aux_bodies[body_j].position)**1.5))*(aux_bodies[body_j].position - body.position) for body_j in index[index != ii]])
            
            #Update velocity and position
            body.velocity = ((1 + self.dt*self.H/2)*body.velocity + (self.dt/body.mass)*force)/(1 - self.dt*self.H/2)
            body.position = body.position + self.dt*body.velocity
        
        
        merged = []
        # When two bodies merge
        for body_i in index:
            for body_j in index[body_i+1::]:
                if (body_i not in merged) and (body_j not in merged) and np.linalg.norm(aux_bodies[body_i].position - aux_bodies[body_j].position) <= (aux_bodies[body_i].diameter + aux_bodies[body_j].diameter)/2:
                    
                    merged += [body_i, body_j]

        merged = np.array(merged)

        self.bodies = [x for ii, x in enumerate(self.bodies) if ii not in merged]

        self.size -= merged.size

        for ii in merged[::2]:
            self.put(aux_bodies[ii] + aux_bodies[ii+1])
        
        self.time += self.dt