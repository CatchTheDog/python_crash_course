motocycles = ['honda','yamaha','suzuki']
print(motocycles)
motocycles[0] = 'ducati'
print(motocycles)
motocycles.append('feige')
print(motocycles)
motocycles.insert(1,'moby')
print(motocycles)

del motocycles[0]
print(motocycles)

poped_motocycle = motocycles.pop()
print(poped_motocycle)
print(motocycles)

poped_motocycle = motocycles.pop(0)
print(poped_motocycle)
print(motocycles)

motocycles.remove('yamaha')
print(motocycles)
# motocycles.remove('yamaha')
# print(motocycles)