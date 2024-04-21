from abc import ABC, abstractmethod

class UF(ABC):
    def __init__(self, N: int):
        self.arr = list(range(N))
    
    @abstractmethod
    def union(self, p: int, q:int):
        pass

    @abstractmethod
    def connected(self, p: int, q: int) -> bool:
        pass

    @abstractmethod
    def num_of_components(self) -> int:
        pass