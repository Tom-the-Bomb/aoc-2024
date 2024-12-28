"""
Day 23: LAN Party

https://adventofcode.com/2024/day/23
"""
__all__ = ('Day23',)

from typing import ClassVar
from collections import defaultdict

from ..solution import Solution

class Day23(Solution):
    NAME: ClassVar[str] = 'LAN Party'

    def _get_graph(self, inp: str) -> dict[str, set[str]]:
        graph = defaultdict[str, set[str]](set)

        for edge in inp.splitlines():
            a, b = edge.split('-', maxsplit=1)

            graph[a].add(b)
            graph[b].add(a)
        return graph

    def _find_clique(
        self,
        graph: dict[str, set[str]],
        node: str,
        clique: set[str],
    ) -> set[str]:
        # go through each child node to see if they are part of the clique
        for child in graph[node]:
            # check if `child` is connected to all nodes the current `clique`: then it is part of the clique
            if clique.issubset(graph[child]):
                clique.add(child)

                # recursively repeat for each `child` node's children
                self._find_clique(graph, child, clique)
        return clique

    def part_one(self, inp: str) -> int:
        graph = self._get_graph(inp)

        total = 0
        seen = set()

        for a, a_children in graph.items():
            # `b` is connected to `a`
            for b in a_children:
                # `c` is connected to `b`
                for c in graph[b]:
                    if (
                        # `c` is connected to `a`
                        # => found clique: `{a, b, c}`
                        a in graph[c]
                        and (triplet := frozenset({a, b, c})) not in seen
                        and (a.startswith('t') or b.startswith('t') or c.startswith('t'))
                    ):
                        total += 1
                        seen.add(triplet)
        return total

    def part_two(self, inp: str) -> str:
        graph = self._get_graph(inp)

        max_clique_size = 0
        max_clique = set()

        for node in graph:
            # Find potential clique for each node in the graph
            clique = self._find_clique(graph, node, {node})

            if (clique_size := len(clique)) > max_clique_size:
                max_clique = clique
                max_clique_size = clique_size

        return ','.join(sorted(max_clique))

    def run(self, inp: str) -> None:
        print('Part 1:', p1 := self.part_one(inp))
        print('Part 2:', p2 := self.part_two(inp))

        assert p1 == 1330
        assert p2 == 'hl,io,ku,pk,ps,qq,sh,tx,ty,wq,xi,xj,yp'