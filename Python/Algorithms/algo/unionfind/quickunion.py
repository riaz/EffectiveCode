from algo.unionfind.uf import UF

class QuickUnion(UF):
    def __init__(self, n: int):
        super().__init__(n)
    
    def connected(self, p: int, q: int) -> bool:
        """
        If the two nodes have the same root, they are connected
        since that is the condition for the union
        """
        return self.__root(p) == self.__root(q)
    
    def union(self, p: int, q: int) -> None:
        """
        This is the quick union function
        We set the root of p to the root of q
        """
        root_p = self.__root(p)
        root_q = self.__root(q)
        self.arr[root_p] = root_q
    
    def num_of_components(self) -> int:
        return len({self.__root(node) for node in self.arr})        
    
    def __root(self, id: int) -> int:
        """
        This method finds the root of a node 
        """
        while id != self.arr[id]:
            id = self.arr[id]
        return id
    