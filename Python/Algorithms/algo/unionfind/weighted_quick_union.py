from algo.unionfind.uf import UF    

class WeightedQuickUnion(UF):
    def __init__(self, N: int):
        super().__init__(N)
        self.height = [1] * N # this is the height of each connected component initially
    
    def union(self, p: int, q:int) -> None:
        root_p = self.__root(p)
        root_q = self.__root(q)

        if self.height[root_p] > self.height[root_q]:
            # if p has a larger tree
            self.arr[root_q] = root_p # root at root of p
            self.height[root_p] += self.height[root_q] # add the height of q to p
        else:
            # do the opposite of what was done above
            self.arr[root_p] = root_q
            self.height[root_q] += self.height[root_p]

    def connected(self, p: int, q: int) -> bool:
        root_p = self.__root(p)
        root_q = self.__root(q)
        return root_p == root_q
    
    def num_of_components(self) -> int:
        return len({self.__root(node) for node in self.arr})

    def __root(self, id) -> int:
        while id  != self.arr[id]:
            id = self.arr[id]
        return id
