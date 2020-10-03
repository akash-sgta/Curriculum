import sys
MAXINT = sys.maxsize

class Graph(object):

	def __init__(self, nodes=10):
		self._nodes = nodes
		self.graph = dict()
		for i in range(self.nodes):
			self.graph[str(i)] = list()

	@property
	def nodes(self):
		return self._nodes

	def __str__(self):
		graph_ = ''
		for node in self.graph.keys():
			graph_ += f'{node} - {self.graph[node]}\n'
		return graph_

	def set_edges(self):
		pass
	def traversal_bfs(self):
		pass
	def traversal_dfs(self):
		pass

class Graph_Unweighted(Graph):

	def __init__(self, nodes=10):
		super().__init__(nodes)

	def set_edge(self, edges):
		for i in range(len(edges)):
			node_from, node_to = edges[i]
			if node_to not in self.graph[str(node_from)]:
				self.graph[str(node_from)].append(node_to)

	def bfs_util(self, node, visited, route):
		visited[node] = True
		route.append(node)
		queue = list()

		while len(route) < self.nodes:
			for neighbour in self.graph[str(node)]:
				if visited[neighbour] == False:
					if neighbour not in queue:
						queue.append(neighbour)
			node = queue.pop(0)
			route.append(node)
			visited[node] = True

		return route

	def traversal_bfs(self, start_node=0):
		visited = [False for i in range(self.nodes)]
		return self.bfs_util(start_node, visited, list())
	
	def dfs_util(self, node, visited, route):
		visited[node] = True
		route.append(node)
		
		for neighbour in self.graph[str(node)]:
			if visited[neighbour] == False:
				self.dfs_util(neighbour, visited, route)
		
		return route
	
	def traversal_dfs(self, start_node=0):
		visited = [False for i in range(self.nodes)]
		return self.dfs_util(start_node, visited, list())

class Graph_Weighted(Graph):

	def __init__(self, nodes=10):
		super().__init__(nodes)

	def set_edge(self, edges):
		for i in range(len(edges)):
			node_from, node_to, weight = edges[i]
			if (node_to,weight) not in self.graph[str(node_from)]:
				self.graph[str(node_from)].append((node_to, weight))

	def bfs_util(self, node, visited, route):
		visited[node] = True
		route.append(node)
		queue = list()

		while len(route) < self.nodes:
			for neighbour in self.graph[str(node)]:
				if visited[neighbour[0]] == False:
					if neighbour[0] not in queue:
						queue.append(neighbour[0])
			node = queue.pop(0)
			route.append(node)
			visited[node] = True

		return route

	def traversal_bfs(self, start_node=0):
		visited = [False for i in range(self.nodes)]
		return self.bfs_util(start_node, visited, list())
	
	def dfs_util(self, node, visited, route):
		visited[node] = True
		route.append(node)
		
		for neighbour in self.graph[str(node)]:
			if visited[neighbour[0]] == False:
				self.dfs_util(neighbour[0], visited, route)
		
		return route
	
	def traversal_dfs(self, start_node=0):
		visited = [False for i in range(self.nodes)]
		return self.dfs_util(start_node, visited, list())
	
	def spanning_tree_prim(self, start_node=0):

		nodes_in_tree = [start_node]
		weight = 0
		order_of_addition = list()

		while len(nodes_in_tree) < self.nodes:
			min_ = (start_node,start_node,MAXINT)
			i = 0
			while i < len(nodes_in_tree):
				u = nodes_in_tree[i]
				for v in self.graph[str(u)]:
					if v[0] not in nodes_in_tree and min_[2] >= v[1]:
						min_ = (u,v[0],v[1])
				
				i += 1
		
			if min_[1] != start_node or min_[0] != start_node:
				order_of_addition.append(min_)
				nodes_in_tree.append(min_[1])
				weight += min_[2]
			else:
				break # in case of a disjoint graph
				
		return order_of_addition, weight
	
	def sort_edges_kruskal(self, array):
		for i in range(1, len(array)):
			key = array[i]

			j = i-1
			while j>=0 and key[2] < array[j][2]:
				array[j+1] = array[j]
				j -= 1

			array[j+1] = key

	def spanning_tree_kruskal(self, start_node=0):

		sorted_edges = list()
		order_of_addition = list()
		weight = 0
		node_set = list([set([i]) for i in range(self.nodes)])

		for key,values in self.graph.items():
			for value in values:
				sorted_edges.append((int(key),value[0],value[1]))
		
		self.sort_edges_kruskal(sorted_edges)

		for edge in sorted_edges:
			u,v = -1, -1
			for v_set in tuple(node_set):
				if edge[0] in v_set:
					u = v_set
				if edge[1] in v_set:
					v = v_set
			if u != v:
				order_of_addition.append(edge)
				weight += edge[2]

				node_set.remove(u)
				node_set.remove(v)
				node_set.append(set(set(u)|set(v)))
			# print(node_set)
			if len(list(node_set[0])) == self.nodes:
				break
		return order_of_addition, weight
	
	def shortest_path_dijkstra(self, start, end):
		
		if end == start:
			return 0
		if end < start:
			start, end = end, start
		
		distance = list()
		previous = list()
		q = list([start])
		for _ in range(self.nodes):
			distance.append(MAXINT)
			previous.append(None)
		distance[start] = 0
		
		visited = [False for _ in range(self.nodes)]
		n = 0
		while visited.count(False) > 0:
			for node_ in self.graph[str(q[n])]:
				if visited[node_[0]] == False:
					if node_[0] not in q:
						q.append(node_[0])
					visited[node_[0]] = True
			n += 1

		u = start
		while len(q) > 0:
			u = q.pop(0)
			for v in self.graph[str(u)]:
				temp = distance[u] + v[1]
				if temp < distance[v[0]]:
					distance[v[0]] = temp
					previous[v[0]] = u
		
		return distance[end]


		
def main():
	
	# graph = Graph_Unweighted(9)
	# edges = ((0,1),(0,7), (1,2),(1,7), (2,1),(2,3),(2,5),(2,8), (3,2),(3,4),(3,5), (4,3),(4,5), (5,2),(5,3),(5,4),(5,6), (6,5),(6,7),(6,8), (7,0),(7,1),(7,6),(7,8), (8,2),(8,6),(8,7))
	# graph.set_edge(edges)
	# print(graph)
	# print(graph.traversal_bfs())
	# print(graph.traversal_dfs())

	graph = Graph_Weighted(9)
	edges = ((0,1,4),(0,7,8), (1,0,4),(1,2,8),(1,7,11), (2,1,8),(2,3,7),(2,5,4),(2,8,2), (3,2,7),(3,4,9),(3,5,14), (4,3,9),(4,5,10), (5,2,4),(5,3,14),(5,4,10),(5,6,2), (6,5,2),(6,7,1),(6,8,6), (7,0,8),(7,1,11),(7,6,1),(7,8,7), (8,2,2),(8,6,6),(8,7,7))
	graph.set_edge(edges)
	print(graph)
	print(graph.traversal_bfs())
	print(graph.traversal_dfs())
	print(graph.spanning_tree_prim(8))
	print(graph.spanning_tree_kruskal())
	print(graph.shortest_path_dijkstra(7,3))
	# https://www.geeksforgeeks.org/wp-content/uploads/Fig-11.jpg

# main()