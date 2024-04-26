class Vertex:
    """顶点类"""

    def __init__(self, val: int):
        self.val = val


def vals_to_vets(vals: list[int]) -> list["Vertex"]:
    """输入值列表 vals ，返回顶点列表 vets"""
    return [Vertex(val) for val in vals]


def vets_to_vals(vets: list["Vertex"]) -> list[int]:
    """输入顶点列表 vets ，返回值列表 vals"""
    return [vet.val for vet in vets]


class GraphAdjList:
    def __init__(self, edges: list[list[Vertex]]) -> None:

        # initialize a dictionary to store the map between the connected vertex
        self.adj_list = dict[Vertex, list[Vertex]]()

        # add the vertex and edges
        for edge in edges:
            self.add_vertex(edge[0])
            self.add_vertex(edge[1])
            self.add_edge(edge[0], edge[1])

    def size(self) -> int:
        return len(self.adj_list)
    
    def add_vertex(self, vet: Vertex):
        if vet in self.adj_list:
            return
        
        self.adj_list[vet] = [ ]
        return
    
    def remove_vertex(self, vet: Vertex):
        if vet not in self.adj_list:
            raise ValueError()
        
        self.adj_list.pop(vet)
        # 遍历其他顶点的链表，删除所有包含 vet 的边
        for vertex in self.adj_list:
            if vet in self.adj_list[vertex]:
                self.adj_list[vertex].remove(vet)
        
    def add_edges(self, vet1: Vertex, vet2: Vertex):
        if vet1 not in self.adj_list or vet2 not in self.adj_list or vet1 == vet2:
            raise ValueError()
        
        self.adj_list[vet1].append(vet2)
        self.adj_list[vet2].append(vet1)
        return
    
    def remove_edges(self, vet1: Vertex, vet2: Vertex):
        if vet1 not in self.adj_list or vet2 not in self.adj_list or vet1 == vet2:
            raise ValueError()
        
        self.adj_list[vet1].remove(vet2)
        self.adj_list[vet2].remove(vet1)
        return

    