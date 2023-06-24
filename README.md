# Simulación la expansión del universo y la formación de galaxias mediante algoritmos reversibles en el tiempo

## Introducción 
  Los componentes del Universo a menudo se agrupan en conjuntos de objetos, como sistemas planetarios y galaxias. Las galaxias con estrellas se formaron poco después del "Big Bang". Tanto los sistemas planetarios como las galaxias comparten una característica común: los objetos giran alrededor de un punto central llamado centro de gravedad. Sin embargo, una galaxia en rotación parece ser inestable a menos que contenga una masa significativamente mayor (materia oscura) que la proporcionada por la materia bariónica conocida en la galaxia [3].

El Universo se expande con una velocidad de Hubble [3], y esta puede afectar la dinámica de los objetos con fuerzas gravitacionales.
Una teoría alternativa para la dinámica de las galaxias, pero sin materia oscura, es la denominada dinámica newtoniana modificada (MOND, por sus siglas en inglés), en la que Milgrom supuso que la fuerza gravitatoria muy débil que experimenta una estrella en las regiones exteriores de una galaxia varía inversamente de forma lineal con la distancia, en contraposición al inverso del cuadrado de la distancia en la ley de gravedad de Newton [4]. La teoría MOND se ha probado extensamente y se ha comparado con el modelo de materia oscura fría de Lambda, mostrando preferencia por la teoría MOND [5, 6], sin embargo también se han encontrado deficiencias en simulaciones de la Galaxia Esferoidal Enana Carina orbitando la Vía Láctea [7]. Las simulaciones N-cuerpos se aplican a modelos de cuerpos celestes dentro de la galaxia de la Vía Láctea, donde estos objetos interactúan bajo la influencia exclusiva de fuerzas gravitatorias, tanto considerando la expansión del espacio conforme a la ley de Hubble como prescindiendo de ella.

En [1], principal referencia de nuestro trabajo, se introduce un algoritmo el cuál se extiende para incluir la expansión de Hubble del espacio. El algoritmo discreto es reversible en el tiempo y posee estabilidad durante miles de millones de pasos temporales sin necesidad de ajustes. Este algoritmo se utiliza para simular modelos sencillos de la Vía Láctea, considerando tanto la presencia como la ausencia de la expansión del Universo según la ley de Hubble. Dichos modelos galácticos se han simulado durante periodos de tiempo que superan el doble de la edad actual del Universo, y tanto las galaxias sin la expansión de Hubble como aquellas que la incluyen se mantienen estables. Toxvaerd sugiere, basandose en estas simulacionrs, que una explicación alternativa para la dinámica de las galaxias, sin necesidad de recurrir a la materia oscura, radica en la juventud del Universo en términos cosmológicos, donde una sola rotación de la galaxia equivale a una unidad de tiempo significativa. A pesar de que una galaxia tan antigua como la nuestra eventualmente perderá objetos ligados debido a la expansión de Hubble, las simulaciones demuestran que esto ocurrirá en un futuro distante.

### Universo en expansión
Una galaxia lejana en el Universo se aleja de la Tierra a una velocidad proporcional a su "distancia propia" a la tierra medida en el tiempo cosmológico t. Este comportamiento se explica por un Universo en expansión. La constante de Hubble $H$ es el coeficiente de expansión de la ley de Hubble para la velocidad de aumento de la distancia r(t) de la Tierra a la galaxia. La expansión de Hubble puede obtenerse mediante una expansión intensiva del espacio independientemente de la materia bariónica en el Universo 

### Algoritmo de diferencias centrales discretas de Newton con fusión de objetos gravitatorios
El algoritmo de diferencia central discreta para la fusión de objetos se deriva en [2]. Sean todos los objetos esféricamente simétricos, donde el diametro del i-ésimo cuerpo es

$\sigma_i = m_i^{1/3}$

y el diametro de colisión

$\sigma_{ij} = \frac{\sigma_i + \sigma_j}{2}$


Si la distancia $r_{ij}(t)$ en el tiempo $t$ entre dos objetos es menor que $\sigma{ij}$, los dos objetos se fusionan en un solo objeto esférico simétrico con masa $m_{\alpha} = m_i + m_j$ y diametro $\sigma_\alpha = m_\alpha^{1/3}$. El nuevo objeto $\alpha$ tendra posición

$\mathbf{r}_\alpha(t) = \frac{m_i}{m_\alpha} \mathbf{r}_i(t) + \frac{m_j}{m_\alpha} \mathbf{r}_j(t)$

### El algoritmo de la mecánica clásica discreta en el Universo en expansión

Incluyendo la velocidad de Hubble en el algoritmo de Newton [2], y tras un reordenamiento, se obtiene el algoritmo para la mecánica clásica con una expansión de Hubble del espacio incluida en la dinámica newtoniana

$\mathbf{v}_{k}\left ( t+\delta t/2 \right )=$

$\frac{(1+\delta tH/2)\mathbf{v}_{k}\left ( t-\delta t/2 \right )+\delta t/m_{k}\mathbf{f}_{k}\left ( t \right )}{1-\delta tH/2}$

Las posiciones están determinadas por valores discretos como

$r_k(t + \delta t) = r_k(t) + \delta tv_k(t + \delta t/2)$

## Procedimientos y simulación
Una galaxia contiene cientos de miles de millones de estrellas y una cantidad considerable de gas bariónico. Por tal motivo, obtener directamente la dinámica newtoniana de una galaxia con esta cantidad de objetos no es posible. En su lugar, hemos simulado modelos de pequeñas 'galaxias' compuestas por cientos de objetos que orbitan alrededor de su centro de gravedad, en un espacio en expansión con diferentes fuerzas de expansión. En [2], nuestra segunda referencía principal, se describe cómo crear una colección de objetos con rotación alrededor de su centro de gravedad mediante simulaciones de dinámica molecula, obtenidas por una extensión del algoritmo discreto de Newton. En [1], el algoritmo se ha ampliado para incorporar la expansión de Hubble del espacio.

### Parametros de la simulación
Para la simulación se utilizaron los mismos parametro y condiciones iniciales que en [1], donde se inició a $t = 0$ con $N = 1000$ objetos con una distribución en forma de disco de sus posiciones iniciales que está, separados a una distancia media $\langle r_{ij}(0)\rangle \approx 1000$ y con una velocidades distribuidas Maxwell-Boltzmann con velocidad media $\langle |v_i(0)|\rangle \approx 1$ donde $v_z \approx 0$.

Las fuerzas gravitacionales se expresaron en unidades de la constante gravitacional $G = 1$ y la unidad de masa $m = m_i(0) = 1$, así como los diámetros de los objetos $\sigma_i(0) = 1$. El valor de la constante de Hubble en el sistema se obtuvo con la razón $H/\bar v$, donde $\bar v$ es la velocidad de rotación de la galaxia $\bar v$ $\approx 0.15$, Obteniendo $H = 5*10^{-8}$ Se simuló la evolución del sistema con un $\delta t = 0,05$ y $10000$ pasos.

# Referencias
[1] Toxvaerd, S. (2022). The stability of galaxies in an expanding Universe obtained by Newtonian dynamics. Classical
and Quantum Gravity, 39(22), 225006.

[2] Toxvaerd, S. (2022). An algorithm for coalescence of classical objects and formation of planetary systems. The European
Physical Journal Plus, 137(1), 99.

[3] de Martino I, Chakrabarty S S, Cesare V, Gallo A, Ostorero L, Diaferio A 2020 Universe 6 107.

[4] Milgrom M 1983 Astrophys. J. 270 371.

[5] Kroupa P 2015 Can. J. Phys. 93 1.

[6] Banik I and Zhao H 2022 Symmetry 14 1331.

[7] Angus G W, Gentile G, Diaferio A, Famaey B, van der Heyden K J 2014 Mon. Not. R. Astron. Soc. 440 746.

[8] Carrol B W and Ostlie D A 1996 An Introduction to Modern Astrophysics (Reading, MA: Addison-Wesley).

[9] Riess A G, et al 1998 Astron. J. 116 1009.

[10] Perlmutter S et al 1999 Astrophys. J. 517 565.4

