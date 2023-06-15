from classes import *
from matplotlib import pyplot as plt
import pandas as pd
import imageio

d = 100

def body_in_disk(R):
	r = R*(np.random.rand())
	theta = 2*np.pi*np.random.rand()
	return body(np.random.rand()*R/200, (r*np.cos(theta), r*np.sin(theta), np.random.rand()*R/10), (np.random.rand()*R/50-R/100, np.random.rand()*R/50-R/100, np.random.rand()*R/5000-R/10000))

def body_in_square(d):
	return body(np.random.rand()*d/100, (np.random.rand()*d-d/2, np.random.rand()*d-d/2, np.random.rand()*d/20), (np.random.rand()*d/100-d/200, np.random.rand()*d/100-d/200, np.random.rand()*d/10000-R/20000))


np.random.seed(2454)
bodies = [body_in_disk(d/2) for i in range(500)]

u1 = universe(bodies, 0.001, 0, 1)
print('created')

N=1000
step = 5

fig = plt.figure(figsize=(5,9))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

for i in range(N):

	if not i%step:
		data = u1.data()

		ax1.plot(data['x'], data['y'], ".")
		ax1.set_xlim(-d,d)
		ax1.set_ylim(-d,d)
		ax1.text(-d, -d, f'n={u1.size}')
		ax2.plot(data['x'], data['z'], ".")
		ax2.set_xlim(-d,d)
		ax2.set_ylim(-d/4,d/4)
		ax2.text(-d, -d/4, f'n={u1.size}')

		plt.savefig("frames/graph{}.png".format(u1.time))
		print("%05.2f"%((i+1)/N*100) + '%')

		ax1.cla()
		ax2.cla()
		
	u1.evolve() 

print(data)

with imageio.get_writer('gifs/mygif.gif', mode='I', duration=.01*step) as writer:
    for filename in ['frames/graph{}.png'.format(i) for i in range(0,N,step)]:
        image = imageio.imread(filename)
        writer.append_data(image)