# Patryk Tomaszewski, 302930

from typing import List, Set, Dict
from enum import Enum, auto
from typing import NamedTuple
import collections

class Color(Enum):
    white = auto()
    grey = auto()
    black = auto()

class tuple_vertex(NamedTuple):
    vertex_label: int
    d: int



VertexID = int


AdjMatrix = List[List[int]]


AdjList = Dict[VertexID, List[VertexID]]

Distance = int



def neighbors(adjlist: AdjList, start_vertex_id: VertexID, max_distance: Distance) -> Set[VertexID]:

    visited = set()
    queue = []
    colors = {}
    first_tuple = tuple_vertex(start_vertex_id,0)
    for u in adjlist:
        colors[u] = Color.white

    colors[first_tuple.vertex_label] = Color.grey
    queue.append(first_tuple)

    while queue:
        u = queue.pop()
        if u.vertex_label != start_vertex_id and u.d <= max_distance:
            visited.add(u.vertex_label)


        if u.vertex_label in adjlist:
            for v in adjlist[u.vertex_label]:
                if v not in colors:
                    new = tuple_vertex(v,u.d+1)
                    queue.append(new)

                elif colors[v] == Color.white:
                    colors[v] = Color.grey
                    new = tuple_vertex(v, u.d + 1)
                    queue.append(new)

            colors[u] = Color.black

    return visited





