from classes import *
from matplotlib import pyplot as plt
import pandas as pd
import imageio

meta_data = pd.read_csv('data/meta_data.csv')
N_graphs = len(meta_data.index)

fig = plt.figure(figsize=(5,9))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)


#Se crean las figuras
for ii in range(N_graphs):

	data = pd.read_csv('data/frame%.d.csv'%(ii))

	ax1.plot(data['x'], data['y'], ".")
	# ax1.set_xlim(-d,d)
	# ax1.set_ylim(-d,d)
	ax1.text(0, 0, "n=%.d"%(meta_data['n_bodies'][ii]))
	ax2.plot(data['x'], data['z'], ".")
	# ax2.set_xlim(-d,d)
	# ax2.set_ylim(-d/4,d/4)
	ax2.text(0, 0, "n=%.d"%(meta_data['n_bodies'][ii]))

	plt.savefig(f"frames/graph{ii}.png")
	print("%05.2f"%((ii+1)/N_graphs*100) + '%')

	ax1.cla()
	ax2.cla()


with imageio.get_writer('gifs/mygif.gif', mode='I', duration=.10/N_graphs) as writer:
    for filename in ['frames/graph{}.png'.format(i) for i in range(N_graphs)]:
        image = imageio.imread(filename)
        writer.append_data(image)