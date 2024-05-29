import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._graph = nx.Graph()
        self.idMap = {}

    def buildGraph(self, anno):
        self._graph.clear()
        nodi = DAO.getAllNodes(anno)
        for n in nodi:
            self.idMap[n.CCode] = n
        self._graph.add_nodes_from(nodi)
        archi = DAO.getAllEdges(anno, self.idMap)
        for a in archi:
            self._graph.add_edge(a.stato1, a.stato2)

    def getPartiConnesse(self):
        return nx.number_connected_components(self._graph)

    def getDFSNodes(self, source):
        edges = nx.dfs_edges(self._graph, source)
        visited = []
        for u, v in edges:
            visited.append(v)
        return visited
