class GraphAdjMat:
    def __init__(self, vertices: list[int], edges: list[list[int]]) -> None:
        """
        vertices: [1, 2, 3, 4, 5]
        edges: [(1,2), (1,3), (1,5), (2,3), (2,4), (2,5), (4,5)]

        edges represent the combination of the index of vertices
        """
        self.vertices: list[int] = [ ]
        self.adj_mat: list[list[int]] = [ ]

        for vertex in vertices:
            self.add_vertex(val=vertex)

        for edge in edges:
            self.add_edge(edge[0], edge[1])

    def size(self) -> int:
        return len(self.vertices)
    
    def add_vertex(self, val: int):
        n = self.size()

        self.vertices.append(val)

        self.adj_mat.append([0] * n)
        for row in self.adj_mat:
            row.append(0)

        return
    
    def remove_vertex(self, index: int):
        if index >= self.size():
            raise IndexError
        
        self.vertices.pop(index)
        self.adj_mat.pop(index)

        for row in self.adj_mat:
            row.pop(index)

        return
    
    def add_edge(self, i: int, j: int) -> None:
        if i < 0 or j < 0 or i >= self.size() or j >= self.size() or i == j:
            raise IndexError()
        
        self.adj_mat[i][j] = 1
        self.adj_mat[j][i] = 1
        
        return
    
    def remove_edge(self, i: int, j: int) -> None:
        if i < 0 or j < 0 or i >= self.size() or j >= self.size() or i == j:
            raise IndexError()
        
        self.adj_mat[i][j] = 0
        self.adj_mat[j][i] = 0
        
        return
    
if __name__ == "__main__":
    pass