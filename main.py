import tkinter
import pypokedex
import numpy as np

p = pypokedex.get(name="swampert")

print (p.moves)

for item in range(0, len(p.moves['omega-ruby'])):
    print (p.moves['omega-ruby'][item])


print(np.sum(np.array(p.base_stats)))

