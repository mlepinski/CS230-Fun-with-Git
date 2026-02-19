class Object:
    _id = 0
    def __init__(self, name, count=0):
        self._id = Object._id
        Object._id += 1
        self._name = name
        self._count = count
    
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, v):
        self._id = v
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, v):
        self._name = v
    
    @property
    def count(self):
        return self._count
    @count.setter
    def count(self, v):
        self._count = v
    
    def __str__(self):
        return f"{self.name} [{self.id}]: {self.count}"

def func():
    obj = Object("Name", 123)
    print(obj)