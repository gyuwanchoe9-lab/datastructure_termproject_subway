import heapq


def dijkstra(graph, starts, ends):
    """
    Multi-source Dijkstra's Algorithm.

    여러 출발 노드에서 동시에 탐색을 시작해
    ends 집합 중 하나에 최소 비용으로 도달하는 경로를 반환한다.

    Parameters
    ----------
    graph  : SubwayGraph
    starts : list  — 출발 노드 목록  [(line, station), ...]
    ends   : set   — 도착 노드 집합  {(line, station), ...}

    Returns
    -------
    (cost, path) : (int, list)
        cost — 최소 소요 시간(분)
        path — 출발 → 도착 노드 순서의 리스트
        경로가 없으면 (inf, []) 반환
    """
    dist    = {}
    parent  = {}
    counter = 0          # 같은 비용일 때 노드 비교를 피하기 위한 고유 카운터
    pq      = []

    # 모든 출발 노드를 비용 0으로 힙에 삽입
    for s in starts:
        dist[s]   = 0
        parent[s] = None
        heapq.heappush(pq, (0, counter, s))
        counter  += 1

    while pq:
        cost, _, u = heapq.heappop(pq)

        # 이미 더 짧은 경로로 처리된 노드는 건너뜀
        if dist.get(u, float('inf')) < cost:
            continue

        # 목적지 도달 → 경로 역추적
        if u in ends:
            path, cur = [], u
            while cur is not None:
                path.append(cur)
                cur = parent[cur]
            return cost, path[::-1]

        # 인접 노드 탐색
        for v, w in graph.get_neighbors(u):
            new_cost = cost + w
            if new_cost < dist.get(v, float('inf')):
                dist[v]   = new_cost
                parent[v] = u
                heapq.heappush(pq, (new_cost, counter, v))
                counter  += 1

    return float('inf'), []
