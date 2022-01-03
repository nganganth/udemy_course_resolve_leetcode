# Dijkstra's Algorithm - Graph Algorithm
# Used to find the shortest path between 2 nodes in a graph 
# Time complexity: O(|E|log|V|)

# https://leetcode.com/problems/network-delay-time/
# 743. Network Delay Time

from collections import defaultdict
import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(list)
        
        for u, v, cost in times:
            g[u].append((cost, v))

        min_heap = [(0, k)]

        visited = set()
        distance = {i: float('inf') for i in range(1, n + 1)}

        distance[k] = 0

        while min_heap:
            curr_distance, u = heapq.heappop(min_heap)
            if u in visited:
                continue
            visited.add(u)

            if len(visited) == n:
                return curr_distance
            
            for direct_distance, v in g[u]:
                if curr_distance + direct_distance < distance[v] and v not in visited:
                    distance[v] = curr_distance + direct_distance
                    heapq.heappush(min_heap, (distance[v], v))
        
        return -1 

# re-check collections.defaultdict
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)

print(d.items())
# it will print the below results
# dict_items([('yellow', [1, 3]), ('blue', [2, 4]), ('red', [1])])
