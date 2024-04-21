from algo.unionfind.uf import UF

class QuickFind(UF):
    def __init__(self, n: int):
        """
        Initializing the array where each element forms its own connected component
        """
        super().__init__(n)
            
    def connected(self, p: int, q: int) -> bool:
        """
        Returns true if p and q are in the same connected component
        """
        return self.arr[p] == self.arr[q]
    
    def union(self, p:int , q: int) -> None:
        """
        This will set all the values in p to q.
        """
        pid = self.arr[p]
        qid = self.arr[q]

        for idx in range(len(self.arr)):
            if self.arr[idx] == pid:
                self.arr[idx] = qid

    def num_of_components(self) -> int:
        """
        This function returns the number of connected components
        This is equal to the dintinct values in the array
        """
        return len(set(self.arr))
