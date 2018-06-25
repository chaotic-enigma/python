def give_most_repeated(some):
	some = str(some)
	some_list = list(set(some))
	count_catch = []
	for i in some:
		for j in some_list:
			if j == i:
				count_catch.append({j : some.count(i)})
	clean_refine = []
	for each in count_catch:
		if each not in clean_refine:
			clean_refine.append(each)
	print(clean_refine)
	vals = []
	kys = []
	for i in clean_refine:
		for k, v in i.items():
			kys.append(k)
			vals.append(v)
	most_repeated = max(vals)
	for i in clean_refine:
		for k, v in i.items():
			if v == most_repeated:
				return k + ' --> ' + str(v)
print(give_most_repeated(132441231212121))
print(give_most_repeated('121ddedsw2dsdd3dd221ddd212f'))
print("\n")

def alkhwarizmi_product(m):
	try:
		if type(m) == list or type(m) == tuple:
			for num in m:
				if type(num) == int:
					if len(m) == 2:
						r0 = [m[0]]
						r1 = [m[1]]
						while True:
							m = [m[0]/2, m[1]*2]
							r0.append(m[0])
							r1.append(m[1])
							if m[0] == 1:
								break
						mul = zip(r0, r1)
						print(mul)
						for pair in mul:
							if pair[0] % 2 == 0:
								mul.remove(pair)
						print(mul)
						result = 0
						for res in mul:
							result += res[1]
						return result
					else:
						return ' > 2, cannot multiply'
				else:
					return m[0] * m[1]
		return 'value not in range'
	except TypeError as e:
		return str(e)
print(alkhwarizmi_product([32412, 324323]))
print(32412 * 324323)
print(alkhwarizmi_product([21, 9]))
print(alkhwarizmi_product((21.43, 2)))
print(alkhwarizmi_product(21))
print("\n")

# different multiplication algos
def naive(a, b):
	x = a; y = b;	z = 0
	while x > 0:
		z += y; x -= 1
	return z
def calculate_naive_runtime(a, b): # time complexity is heavier
	z = 1
	while z > 0:
		x = a; y = b
		print(naive(x, y))
		a = a ** 2
		b = b ** 2
# calculate_naive_runtime(2, 2)

def russian_peasants(a, b):
	x = a; y = b;	z = 0 
	while x > 0:
		if x % 2 == 1:
			z += y
		y = y << 1
		x = x >> 1
	return z
def calculate_russian_time(a, b): # time complexity is low
	z = 1
	while z > 0:
		x = a; y = b
		print(russian_peasants(x, y))
		a = a ** 2
		b = b ** 2
# calculate_russian_time(2, 2)

# Eulerian tour
def create_tour(nodes):
	tour = []
	for i in range(len(nodes)-1):
		tour.append((nodes[i], nodes[i+1]))
	tour.append((nodes[0], nodes[len(nodes)-1]))
	for i in tour:
		if i[1] not in nodes:
			tour.remove(i)
	return tour
print(create_tour([1,2,3,4,5,6]))
print(create_tour([20, 21, 22, 23, 24, 25]))
print("\n")

def find_eulerian_tour(graph):
	e_tour = []
	for i in graph:
		e_tour.append(i[0])
		e_tour.append(i[1])
	refine = []
	for i in e_tour:
		if i not in refine:
			refine.append(i)
	refine.append(graph[0][0])
	return refine
print(find_eulerian_tour([(1, 2), (2, 3), (3, 4), (6, 1)]))
print("\n")

def make_link(g, node1, node2):
	if node1 not in g:
		g[node1] = {}
	(g[node1])[node2] = 1
	if node2 not in g:
		g[node2] = {}
	(g[node2])[node1] = 1
	return g
a_ring = {}
n = 5
for i in range(n):
	make_link(a_ring, i, (i+1)%n)
print(a_ring)
# print(len(a_ring)) # 5
print(sum(len([a_ring[node]]) for node in a_ring.keys()))
print("\n")

# kinda slow when n tends to infinite
def complete_graph(n): # n*(n-1)/2
	if n == 0 or n == 1:
		return 0
	if n > 1:
		edges = []
		while True:
			c = n - 1
			edges.append(c)
			n -= 1
			if c == 1:
				break
		return sum(edges)
print(complete_graph(109))
print("\n")

def erdos_renyi_graph(n, prob):
	return complete_graph(n) * prob
print(erdos_renyi_graph(256, 0.25))
print("\n")

def create_combo_lock(nodes):
	chain = []
	for i in range(len(nodes)-1):
		chain.append((nodes[i], nodes[i+1]))
	for i in chain:
		if i[1] not in nodes:
			chain.remove(i)
	star = []
	for i in nodes:
		if i != nodes[1] and i != nodes[0]:
			star.append((nodes[0], i))
	combo = {}
	combo['chain'] = chain
	combo['star'] = star
	return combo
print(create_combo_lock([21,32,12,43,44,65,76]))
print(create_combo_lock([32,13,43,54,34,65,444,55]))
print("\n")

def cluster_coefficient(nodes):
	faces = nodes
	#############################
	whole = [j for i in faces for j in i]
	reducing = list(set(whole))
	most = [{j: whole.count(j)} for i in whole for j in reducing]
	clean = []
	for i in most:
		if i not in clean:
			clean.append(i)
	vals = []
	for element in clean:
		for k, v in element.items():
			vals.append(v)
	repeated = max(vals)
	for element in clean:
		for k, v in element.items():
			if v == repeated:
				common = k
	common = str(common)
	#############################
	degree = []
	num_links = []
	for face in faces:
		if face[0] == common:
			degree.append(face)
		if not face[0] == common:
			for node in degree:
				if face[0] and face[1] in node:
					num_links.append(face)
	alone = []
	for node in degree:
		alone.append(node[1])
	for link in num_links:
		if link[0] or link[1] not in alone:
			num_links.remove(link)
	num_v = len(num_links[0])
	measure_d = len(degree)
	result = ((2.0*num_v)/(measure_d*(measure_d-1)))
	#############################
	return result
print(cluster_coefficient([("ORD", "SEA"), ("ORD", "LAX"), ('ORD', 'DFW'), ('ORD', 'PIT'),
													('SEA', 'LAX'), ('LAX', 'DFW'), ('ATL', 'PIT'), ('ATL', 'RDU'),
													('RDU', 'PHL'), ('PIT', 'PHL'), ('PHL', 'PVD')]))
print(cluster_coefficient([('1', '2'), ('1', '3'), ('1', '4'), ('2', '3'), ('0', '4'), ('6', '5')]))
print("\n")

def form_chain_tree():
	chain_tree = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('e', 'f')]
	main_node = 'a'
	chain_tree_structure = []
	s = 0
	while s <= len(chain_tree):
		unique_node = main_node
		end_path = []
		for branch in chain_tree:
			if unique_node in branch:
				for stems in branch:
					if stems != unique_node:
						end_path.append(stems)
						chain_tree_structure.append({unique_node : end_path})
						main_node = stems
		s += 1
	clean_tree = []
	for structure in chain_tree_structure:
		if structure not in clean_tree:
			clean_tree.append(structure)
	return clean_tree
print(form_chain_tree())
print("\n")

def tree_hierarchy():
	tree = [('a', 'b'), ('a', 'c'), ('b', 'd'), ('b', 'e'), ('c', 'f'), ('c', 'g'), ('e', 'h')]
	family = sorted(list(set([j for i in tree for j in i])))
	s = 0
	family_tree = []
	while s <= len(tree):
		for item in family:
			unique_branches = []
			for branches in tree:
				for node in branches:
					if node == item:
						unique_branches.append(branches)
			unique_branches = list(set([j for i in unique_branches for j in i]))
			family_tree.append({item : unique_branches})
		s += 1
	family_clean = []
	for bunch in family_tree:
		if bunch not in family_clean:
			family_clean.append(bunch)
	for banyan in family_clean:
		for vegy, fruits in banyan.items():
			if vegy in fruits:
				fruits.remove(vegy)
	return family_clean
print(tree_hierarchy())

def DFS():
	tree = [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('e', 'f')]
	main = 'c'
	ends = [main]
	s = 0
	while s <= len(tree):
		stem = main
		for branch in tree:
			if stem in branch:
				for all_stems in branch:
					if all_stems != stem:
						if all_stems not in ends:
							print("marked")
							ends.append(all_stems)
							print(ends)
							print("\n")
							main = all_stems
		s += 1

