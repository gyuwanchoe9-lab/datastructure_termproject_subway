# Seoul Subway Shortest Path Finder

Finds the shortest path between any two stations on Seoul Metro Lines 1–5 using Dijkstra's Algorithm.

---

## How to Run

```bash
python main.py
```

Enter the start and end station names in Korean when prompted.

```
출발역: 강남
도착역: 종로3가
```

Type `q` to quit.

---

## Graph Model

Each node is a `(line, station)` tuple.

| Type | Example | Weight |
|------|---------|--------|
| Adjacent stations | `(1, 신도림)` ↔ `(1, 영등포)` | 2 min |
| Transfer | `(1, 신도림)` ↔ `(2, 신도림)` | 2 min |

---

## Algorithm

**Multi-source Dijkstra** — all nodes for the start station name (across different lines) are inserted into the priority queue with cost 0 simultaneously, so the algorithm finds the optimal line choice automatically.

Time complexity: **O((V + E) log V)**

---

## Example Output

```
출발역: 신도림
도착역: 왕십리

  총 소요 시간 : 16분
  경유 역 수   : 9역

  [2호선] 신도림 → 문래 → 영등포구청 → 당산 → 합정 → 홍대입구 → 신촌 → 이대 → 아현 → 충정로
  [5호선] 충정로 → 애오개 → 공덕 → 마포 → 여의나루 → 여의도 ...
```

---

## File Structure

```
main.py                 entry point
graph/subway_graph.py   adjacency-list weighted graph
algorithms/dijkstra.py  Dijkstra's algorithm
data/lines.py           station lists for lines 1–5
data/builder.py         graph construction
utils/display.py        output formatting
```

---

## Coverage

- Line 1: Soyosan ↔ Sinchang / Gwangmyeong / Seodongtan branches
- Line 2: circular + Seongsu / Sinjeong branches
- Line 3: Daehwa ↔ Ogeum
- Line 4: Jinjeop ↔ Oido
- Line 5: Banghwa ↔ Macheon / Hanam branches
