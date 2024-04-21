from algo.unionfind.uf import UF

class QuickUnion(UF):
    def __init__(self, n: int):
        super().__init__(n)
    
    def connected(self, p: int, q: int) -> bool:
        return False
    
    def union(self, p: int, q: int) -> None:
        return None
    
    def num_of_components(self) -> int:
        return len(set(self.arr))