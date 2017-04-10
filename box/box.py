    # Create a class that represents a cuboid:
    # It should take its three dimensions as constructor parameters (numbers)
    # It should have a method called `get_surface` that returns the cuboid's surface
    # It should have a method called `get_volume` that returns the cuboid's volume

class Cuboid(object):
    def __init__(self, width=0, deepth=0, height=0):
        self.width = width
        self.deepth = deepth
        self.height = height

    def get_surface(self, width=0, deepth=0, height=0):
        return (2 *(self.width * self.deepth + self.width * self.height + self.deepth * self.height))

    def get_volume(self, width=0, deepth=0, height=0):
        return (self.width * self.deepth * self.height)

box = Cuboid(10, 20, 30)
print(box.get_surface()) # should print 2200
print(box.get_volume()) # should print 6000
