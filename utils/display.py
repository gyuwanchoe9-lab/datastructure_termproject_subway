SEP = "=" * 60


def print_header():
    print(SEP)
    print("  서울 지하철 1~5호선 최단 경로 탐색기")
    print("  Algorithm : Dijkstra's Algorithm")
    print("  Node      : (line#, station_name)")
    print("  Edge cost : 2 min (adjacent or transfer)")
    print(SEP)


def print_route(path: list, total_time: int):
    """
    경로 리스트를 호선별 구간으로 묶어 출력한다.

    path 예시: [(1,'신도림'), (2,'신도림'), (2,'강남')]
    """
    if not path:
        print("  경로 없음")
        return

    print(f"\n  총 소요 시간 : {total_time}분")
    print(f"  경유 역 수   : {len(path)}역\n")

    prev_line, segment = None, []

    def flush():
        if segment:
            print(f"  [{prev_line}호선] " + " → ".join(segment))

    for line_num, station in path:
        if line_num != prev_line:
            flush()
            prev_line = line_num
            segment   = [station]
        else:
            segment.append(station)
    flush()
    print()


def print_error(msg: str):
    print(f"  오류: {msg}")
