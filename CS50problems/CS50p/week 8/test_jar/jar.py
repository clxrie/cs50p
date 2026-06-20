class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity error!")
        self.capacity = capacity
        self.size = 0


    def __str__(self):
        return "🍪"* self._size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Cant deposit more!")
        self.size = self.size + n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Cant withdraw more!")
        self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity error!")
        self._capacity = capacity

    @property
    def size(self):
        return self._size 
    
    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("Size can't exceed capacity")
        self._size = size


def main():
    jar = Jar()
    print(jar)
    jar.deposit(11)
    print(jar)
    jar.withdraw(3)
    print(jar)
    jar.withdraw(5)
    print(jar)

if __name__ == "__main__":
    main()