__author__ = 'ondra_000'

class Cuboid:
    def __init__(self, a=0, b=0, c=0):
        self.a=a
        self.b=b
        self.c=c

        if self.b ==0:
            self.b=a
        if self.c ==0:
            self.c=a
    def compute_volume(self):
        return(self.a*self.b*self.c)

    def make_scaled_copy(self,scale):
        new_a=scale*Cuboid.a
        new_b=scale*Cuboid.b
        new_c=scale*Cuboid.c
        return Cuboid(new_a,new_b,new_c)

if __name__=="__main__":
    c1=Cuboid(1)
    c1.compute_volume()
    print(c1.compute_volume())