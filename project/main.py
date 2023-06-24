import numpy as np
import pandas as pd
from classes import body, universe
from functions import generate_velocities, random_pos

G, H = 1, 5*10**(-8)

N_bodies = 500
N_steps = 1000
step_size = 10
dt = .1

data = {}
n_bodies = np.zeros(N_steps+1)
time = np.zeros(N_steps+1)

np.random.seed(6642)

positions = random_pos(N_bodies)
velocities = generate_velocities(N_bodies)
bodies = [body(1, positions[ii], velocities[ii]) for ii in range(N_bodies)]

u1 = universe(bodies, G, H, dt)

print('created')

for ii in range(N_steps*step_size+1):

	if not ii%step_size:
		u1.data().to_csv('data/frame%.d.csv'%(ii/step_size))
		n_bodies[int(ii/step_size)] = u1.size
		time[int(ii/step_size)] = u1.time
		print("%05.2f"%((ii+1)/(step_size*N_steps)*100) + '%' + ': %.d'%(u1.size)+ ' %.d'%(ii/step_size))
		if not int(ii/step_size+1)%10:
		
	u1.evolve()

pd.DataFrame({'n_bodies':n_bodies, 'time':time}).to_csv('data/meta_data.csv')
