from classes import *
from matplotlib import pyplot as plt
import pandas as pd
import imageio

meta_data = pd.read_csv('data_nico/meta_data.csv')
N_graphs = len(meta_data.index)

fig = plt.figure(figsize=(6,9))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)


#Se crean las figuras
for ii in range(N_graphs):

	data = pd.read_csv('data_carlos/frame%.d.csv'%(ii))

	ax1.plot(data['x'], data['y'], ".")
	ax1.set_xlim(-3000,3000)
	ax1.set_ylim(-3000,3000)
	ax1.set_xlabel('x')
	ax1.set_ylabel('y')
	ax1.text(-2500,-2500, "n=%.d"%(meta_data['n_bodies'][ii]))
	ax2.plot(data['x'], data['z'], ".")
	ax2.set_xlim(-3000,3000)
	ax2.set_ylim(-1000,1000)
	ax2.set_xlabel('x')
	ax2.set_ylabel('z')
	ax2.text(-2500, -500, "n=%.d"%(meta_data['n_bodies'][ii]))

	plt.savefig(f"frames/graph{ii}.png")
	print("%05.2f"%((ii+1)/N_graphs*100) + '%')

	ax1.cla()
	ax2.cla()


with imageio.get_writer('data_carlos/mygif.gif', mode='I', duration=1/10) as writer:
    for filename in ['frames/graph{}.png'.format(i) for i in range(N_graphs)]:
        image = imageio.imread(filename)
        writer.append_data(image)