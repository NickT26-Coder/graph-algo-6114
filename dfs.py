'''
What is DFS / Topological Sort on a graph?

DFS:
Search "deeper" in the graph whenever possible. Uses a stack to explore the edges of
the most recently discovered node if they have more nodes to explore. Return back to the
original node that was searched once edges have been exhausted and move onto to the next
until all nodes are visited. DFS is used for cycle finding which is determined by presence of a back edge.

Topological Sorting / Ordering:
Topological sorting can only be used on s DAG which DFS is used to confirm whether or not
the graph is cyclical. Uses DFS as DFS keeps track of visited nodes it creates an order of precendence that is
used to order higher priority items first or reverse if needed.

Psuedo Code:

Runtime:

'''


# Implementation


# Test