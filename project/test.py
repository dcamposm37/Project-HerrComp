from classes import *
import pandas as pd

body1 = body(1, (0,0,0), (1,1,1))

body2 = body(2, (1,1,1), (0,0,0))

print(body1)
print(body2)
print(body1.speed(), body2.speed())
print(body1+body2, (body1+body2).speed())

u1 = universe([], 1, 1)

u1.put(body1)
u1.put(body2)
u1.put(body1+body2)

df = pd.DataFrame(u1.data())
df.to_csv("test/universe{}.csv".format(u1.time))

print(df)