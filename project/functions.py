###################################################################### POSICION INICIAL
# Retorna posición inicial aleatoria (distribución normal)
def random_coordinates(mean, sigma):
  x = np.random.normal(mean, sigma)  
  y = np.random.normal(mean, sigma) 
  z = 0.05 * np.random.normal(mean, sigma) 
  return (x, y, z)

# Retorna distancia promedio entre un punto y los demas puntos. El punto por defecto es el centro de gravedad (0,0,0) (aproximado)
def mean_distance(points, current_point = (0, 0, 0)):
  total_distance = 0
  x = current_point[0]
  y = current_point[1]
  z = current_point[2]

  for point in points:
    distance = math.sqrt((point[0] - x)**2 + (point[1] - y)**2 + (point[2] - z)**2)
    total_distance += distance

  current_mean_distance = total_distance/len(points)
  return current_mean_distance

# Retorna la distancia promedio entre todos los puntos. SE USA SOLO EN LA PRUEBA PARA CALCULAR LA DISTANCIA PROMEDIO ENTRE LOS CUERPOS
def total_mean_distance(points):
  total_mean_distance = 0
  for ii in points:
    total_mean_distance += mean_distance(points, ii)
  
  return total_mean_distance/len(points)

# Retorna una lista de tuplas con las coordenadas iniciales de los 1000 cuerpos
def random_pos(num_puntos):
    points = []
    points.append(random_coordinates(0, 400))  # Agregamos el primer punto en el origen

    while len(points) < num_puntos:
        # Agrega primero 650 puntos en torno al centro
        if len(points) < 650:
          punto = random_coordinates(0, 400)
          current_mean_distance = mean_distance(points, punto) # SE USA SOLO EN LA PRUEBA PARA CALCULAR LA DISTANCIA PROMEDIO ENTRE LOS CUERPOS
          points.append(punto)

        # Los demas puntos orbitan alrededor del centro
        else:
          punto = random_coordinates(0, 1000)
          current_mean_distance = mean_distance(points, punto) # SE USA SOLO EN LA PRUEBA PARA CALCULAR LA DISTANCIA PROMEDIO ENTRE LOS CUERPOS
          points.append(punto)

    return points

# PRUEBA DE QUE SI FUNCIONA
# num_puntos= 1000

# pos_ini = random_pos(num_puntos)
# print(total_mean_distance(pos_ini))

# x = [p[0] for p in pos_ini]
# y = [p[1] for p in pos_ini]

# plt.scatter(x, y, marker = '.')
# plt.xlim(-4000, 4000)
# plt.ylim(-4000, 4000)
# plt.show()

###################################################################### VELOCIDAD INICIAL
from scipy.interpolate import interp1d as interp
from scipy.special import erf

# np.random.seed(69)

def MB_CDF(v,m,T):
    """ Cumulative Distribution function of the Maxwell-Boltzmann speed distribution """
    kB = 1.38e-23
    a = np.sqrt(kB*T/m)
    return erf(v/(np.sqrt(2)*a)) - np.sqrt(2/np.pi)* v* np.exp(-v**2/(2*a**2))/a

mass = 1
T = (0.8)**2/1.38e-23

# create CDF
vs = np.arange(0,2500,0.1)
cdf = MB_CDF(vs,mass,T) # essentially y = f(x)

#create interpolation function to CDF
inv_cdf = interp(cdf,vs) # essentially what we have done is made x = g(y) from y = f(x)

# Return a tuples arrangement with the 3 velocities components per bodie, where |v| = 1 and vz aproxx 0
def generate_velocities(n):
    """ generate a set of velocity vectors in 3D from the MB inverse CDF function """
    rand_nums = np.random.random(n)
    speeds = inv_cdf(rand_nums)
    
    # spherical polar coords - generate random angle for velocity vector, uniformly distributed over the surface of a sphere
    theta = np.arccos(np.random.uniform(-1,1,n))
    phi = np.random.uniform(0,2*np.pi,n)
    
    # convert to cartesian units
    vx = speeds * np.sin(theta) * np.cos(phi) 
    vy = speeds * np.sin(theta) * np.sin(phi)
    vz = speeds * np.cos(theta) * 0.1         # z component 10 times lower 

    return list(zip(vx, vy, vz))
     

# PRUEBA DE QUE SI FUNCIONA
# spd, vel_ini = generate_velocities(100000)

# vx = [p[0] for p in vel_ini]
# vy = [p[1] for p in vel_ini]
# vz = [p[2] for p in vel_ini]

# fig = plt.figure()
# ax = fig.add_subplot(111)

# # generate histogram of velocities
# ax.hist(spd,bins=50,fc='b',alpha=0.4,lw=0.2)

# # verify that the average velocity norm is close to zero
# speed = 0
# for i in range(100000):
#   speed += np.sqrt(vx[i]**2+vy[i]**2+vz[i]**2)

# print(speed/100000)

############################################ PROPERTIES FOR THE 3 FIGURE
# mean distance to the center gravity
# def mean_distance_CG():

# mean velocity to the center gravity
# def mean_vel_CG():