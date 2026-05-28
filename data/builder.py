from graph.subway_graph import SubwayGraph
from data.lines import (
    LINE1_MAIN, LINE1_GWANGMYEONG, LINE1_SOUTH, LINE1_SEODONGTAN,
    LINE2,
    LINE3,
    LINE4,
    LINE5_MAIN, LINE5_SANGIL, LINE5_MACHEON,
    TRANSFER_STATIONS,
)


def build_subway() -> SubwayGraph:
    """
    노선 데이터를 읽어 SubwayGraph를 생성하고 반환한다.

    - 인접역 사이 간선 가중치: 2분
    - 환승 간선 가중치 : 2분
    """
    g = SubwayGraph()

    def add_line(line_num: int, stations: list):
        """연속된 역 쌍을 간선으로 추가"""
        for i in range(len(stations) - 1):
            g.add_edge((line_num, stations[i]), (line_num, stations[i + 1]), 2)

    # 1호선 (본선 + 지선 3개)
    add_line(1, LINE1_MAIN)
    add_line(1, LINE1_GWANGMYEONG)
    add_line(1, LINE1_SOUTH)
    add_line(1, LINE1_SEODONGTAN)

    # 2호선 (순환선: 마지막 역 충정로 → 첫 역 시청 연결)
    add_line(2, LINE2)
    g.add_edge((2, "충정로"), (2, "시청"), 2)

    # 3·4호선
    add_line(3, LINE3)
    add_line(4, LINE4)

    # 5호선 (본선 + 지선 2개)
    add_line(5, LINE5_MAIN)
    add_line(5, LINE5_SANGIL)
    add_line(5, LINE5_MACHEON)

    # 환승 간선 추가
    for name, lines in TRANSFER_STATIONS:
        for i in range(len(lines)):
            for j in range(i + 1, len(lines)):
                g.add_edge((lines[i], name), (lines[j], name), 2)

    return g
