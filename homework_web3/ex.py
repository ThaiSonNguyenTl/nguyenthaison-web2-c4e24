import mlab
from models.river import River

mlab.connect()

print("ex2")
river_list = River.objects(continent__iexact = "Africa")
for river in river_list:
    print(river.name)

print("ex3")
river_list = River.objects(continent__iexact = "S. America" , length__lt = 1000)
for river in river_list:
    print(river.name,river.length)
