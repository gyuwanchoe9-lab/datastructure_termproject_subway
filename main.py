"""
Term Project — 서울 지하철 1~5호선 최단 경로 탐색기

실행 방법:
    python main.py          (Term_project/ 폴더 안에서 실행)

파일 구조:
    main.py                 ← 진입점 (이 파일)
    graph/subway_graph.py   ← SubwayGraph 자료구조
    algorithms/dijkstra.py  ← Dijkstra 알고리즘
    data/lines.py           ← 1~5호선 역 목록 & 환승 정보
    data/builder.py         ← 그래프 구축 함수
    utils/display.py        ← 출력 헬퍼 함수
"""

import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

# Term_project/ 를 모듈 검색 경로에 추가
sys.path.insert(0, os.path.dirname(__file__))

from data.builder      import build_subway
from algorithms.dijkstra import dijkstra
from utils.display     import print_header, print_route, print_error, SEP


def find_route(subway, start_name: str, end_name: str):
    """역 이름을 받아 최단 경로를 탐색한다."""
    starts = subway.find_nodes(start_name)
    ends   = set(subway.find_nodes(end_name))

    if not starts:
        return None, None, f"'{start_name}' 역을 찾을 수 없습니다."
    if not ends:
        return None, None, f"'{end_name}' 역을 찾을 수 없습니다."
    if start_name == end_name:
        return 0, [starts[0]], None

    cost, path = dijkstra(subway, starts, ends)
    if not path:
        return None, None, "경로를 찾을 수 없습니다."
    return cost, path, None


def run_demos(subway):
    demos = [
        ("소요산",  "인천"),
        ("방화",    "마천"),
        ("대화",    "오이도"),
        ("강남",    "종로3가"),
        ("신도림",  "왕십리"),
        ("천안",    "노원"),
    ]
    print("\n[Demo Routes]")
    for s, e in demos:
        print(f"\n  {s}  →  {e}")
        cost, path, err = find_route(subway, s, e)
        if err:
            print_error(err)
        else:
            print_route(path, cost)


def run_interactive(subway):
    print(SEP)
    print("  직접 검색  (종료: q)")
    print(SEP)
    while True:
        s = input("\n  출발역: ").strip()
        if s.lower() == 'q':
            break
        e = input("  도착역: ").strip()
        if e.lower() == 'q':
            break
        cost, path, err = find_route(subway, s, e)
        if err:
            print_error(err)
        else:
            print_route(path, cost)
    print("\n프로그램을 종료합니다.")


if __name__ == "__main__":
    print_header()
    subway = build_subway()
    run_interactive(subway)
