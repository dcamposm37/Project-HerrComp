from classes import *
from matplotlib import pyplot as plt
import pandas as pd
import imageio

d = 1000
np.random.seed(0)
bodies = [body(np.random.rand()*3, (np.random.rand()*1000, np.random.rand()*1000, 0), (np.random.rand()*d/150-d/300, np.random.rand()*d/150-d/300, 0)) for i in range(100)]

u1 = universe(bodies, 0.01, 0.0001, 1)
print('created')

N=1000

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

for i in range(N):
	data = u1.data()

	ax.plot(data['x'], data['y'], "o")
	plt.xlim(-d//4,5*d//4)
	plt.ylim(-d//4,5*d//4)
	plt.text(0, 0, f'n={u1.size}')
	plt.savefig("frames/graph{}.png".format(u1.time))
	plt.cla()
	u1.evolve()

	print("%05.2f"%((i+1)/N*100) + '%') 


with imageio.get_writer('mygif.gif', mode='I') as writer:
    for filename in ['frames/graph{}.png'.format(i) for i in range(N)]:
        image = imageio.imread(filename)
        writer.append_data(image)