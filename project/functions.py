# Retorna posición inicial aleatoria (distribución normal)
def random_coordinates(mean, sigma):
  x = np.random.normal(mean, sigma)  
  y = np.random.normal(mean, sigma) 
  z = 0.05 * np.random.normal(mean, sigma) 
  return (x, y, z)

# Retorna distancia promedio entre un punto y los demas puntos
def mean_distance(points, current_point): 
  total_distance = 0
  x = current_point[0]
  y = current_point[1]

  for point in points:
    distance = math.sqrt((point[0] - x)**2 + (point[1] - y)**2)
    total_distance += distance

  current_mean_distance = total_distance/len(points)
  return current_mean_distance

# Retorna la distancia promedio entre todos los puntos
def total_mean_distance(points):
  total_mean_distance = 0
  for ii in points:
    total_mean_distance += mean_distance(points, ii)
  
  return total_mean_distance/len(points)


def random_pos(num_puntos):
    points = []
    points.append((0, 0, 0))  # Agregamos el primer punto en el origen
    
    while len(points) < num_puntos:
        # Si la distancia promedio cumple con el criterio, agregamos el punto a la lista
        if len(points) <= 650:
          punto = random_coordinates(0, 400)
          current_mean_distance = mean_distance(points, punto)
          points.append(punto)
        else:
          punto = random_coordinates(0, 1000)
          current_mean_distance = mean_distance(points, punto)
          points.append(punto)
    
    return points

# Ejemplo de uso
# num_puntos= 1000

# pos_ini = random_pos(num_puntos)
# print(total_mean_distance(pos_ini))

# x = [p[0] for p in pos_ini]
# y = [p[1] for p in pos_ini]

# plt.scatter(x, y, marker = '.')
# plt.xlim(-4000, 4000)
# plt.ylim(-4000, 4000)
# plt.show()