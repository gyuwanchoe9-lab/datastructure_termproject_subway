from collections import defaultdict


class SubwayGraph:
    """
    인접 리스트 기반 가중 무방향 그래프.

    노드 : (호선 번호, 역 이름)  예) (1, "신도림")
    간선 : 인접역 이동 또는 환승, 기본 가중치 2분
    """

    def __init__(self):
        self.adj   = defaultdict(list)  # {node: [(neighbor, weight), ...]}
        self.nodes = set()

    def add_edge(self, u, v, w=2):
        """양방향 간선 추가"""
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))
        self.nodes.add(u)
        self.nodes.add(v)

    def get_neighbors(self, node):
        """node의 인접 노드 리스트 반환"""
        return self.adj[node]

    def find_nodes(self, station_name):
        """역 이름으로 해당 역의 모든 노드(여러 호선) 반환"""
        return [n for n in self.nodes if n[1] == station_name]

    def node_count(self):
        return len(self.nodes)

    def edge_count(self):
        return sum(len(v) for v in self.adj.values()) // 2
