import math as mt

class Vector2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def module(self):
        return mt.sqrt(mt.pow(self.x,2)+ mt.pow(self.y,2))
    
    def scalar_prod(self,param=1):
        self.x *= param
        self.y *= param
    
    def __str__(self):
        return self.x,self.y
    

    def sum(vec1,vec2):
        return vec1.x+vec2.x,vec1.y+vec2.y
    
    def subtract(vec1,vec2):
        return vec1.x-vec2.x,vec1.y-vec2.y
    
    def dot_product(vec1,vec2):
        return (vec1.x*vec2.x)+(vec1.y*vec2.y)
    
    def distance(vec1,vec2):
        return mt.pow(vec1.x-vec2.x,2)+mt.pow(vec1.y-vec2.y,2)

class Vector3D(Vector2D):

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __str__(self):
        return self.x,self.y,self.z
    
    def module(self):
        return mt.sqrt(mt.pow(self.x,2)+ mt.pow(self.y,2)+mt.pow(self.z,2))
    
    def scalar_prod(self,param=1):
        super().scalar_prod(param)
        self.z*= param


    def sum(vec1,vec2):
        return vec1.x+vec2.x,vec1.y+vec2.y,vec1.z+vec2.z
    
    def subtract(vec1,vec2):
        return vec1.x-vec2.x,vec1.y-vec2.y,vec1.z-vec2.z
    
    def dot_product(vec1,vec2):
        return (vec1.x*vec2.x)+(vec1.y*vec2.y)+(vec1.z*vec2.z)
    
    def distance(vec1,vec2):
        return mt.pow(vec1.x-vec2.x,2)+mt.pow(vec1.y-vec2.y,2)+mt.pow(vec1.z-vec2.z,2)
    