"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node: 
            return None
        
        head = node.val
        node_map = {}

        que = deque()
        visited = set()

        que.append(node)
        visited.add(node)

        while que:
            for _ in range(len(que)):
                item = que.popleft()
                if item.val not in node_map:
                    node_map[item.val] = Node(item.val, None)

                for n in item.neighbors:
                    if n.val in node_map:
                        neighbor_node = node_map[n.val]
                    else:
                        neighbor_node = Node(n.val, None)
                        node_map[n.val] = neighbor_node
                    
                    node_map[item.val].neighbors.append(neighbor_node)

                    if n in visited:
                        continue
                    que.append(n)
                    visited.add(n)
                    
        return node_map[head]
            
                
                
        
        
        
        