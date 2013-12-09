import sys 

#Create Adjacency List to be used in the DFS
def createAdjacencyList( edgeList ):
	adjList = dict()
	
	for each in edgeList:
		adjList[ each[0] ] = []
		adjList[ each[1] ] = []
	for each in edgeList:
		adjList[ each[0] ].append( each[1] )

	return adjList

##########################################
#STRONGLY CONNECTED COMPONENTS           #
##########################################
def getSCC( adjacencyList, transposed ):
	visited = dict()
	times = dict()
	for key in adjacencyList: 
		visited[ key ] = False
		times[ key ] = [0,0]
	time = 0
	DFS_Stack = []			#used for keeping track of nodes
	Finished_Stack=[]
	#loop through all the vertices
	for key in visited:
		if not visited[key] : DFS_Stack.append( key )
		while len( DFS_Stack ) != 0 :
			curTop = DFS_Stack[ len( DFS_Stack) -1 ] 
			if not visited[ curTop ] : 
				time += 1
				times[ curTop ][0] = time
				visited[ curTop] = True
			for node in adjacencyList[ curTop ]:
				if not visited[ node ] : DFS_Stack.append( node ) 
			if curTop == DFS_Stack[ len( DFS_Stack) -1 ]: 
				if times[curTop][1] == 0:
					time += 1
					times[curTop][1] = time
					Finished_Stack.append( curTop )
				DFS_Stack.pop()

	#Stack with last finishing on top is now done
	SCC = dict()
	for key in adjacencyList: 
		visited[ key ] = False
		times[ key ] = [0,0]
	time = 0
	DFS_Stack = []			#used for keeping track of nodes
	#loop through all the vertices
	for key in Finished_Stack[::-1]:
		if not visited[key] : 
			DFS_Stack.append( key )
			SCC[ key ] = []
		while len( DFS_Stack ) != 0 :
			curTop = DFS_Stack[ len( DFS_Stack) -1 ] 
			if not visited[ curTop ] : 
				time += 1
				times[ curTop ][0] = time
				visited[ curTop] = True
			for node in transposed[ curTop ]:
				if not visited[ node ] : DFS_Stack.append( node ) 
			if curTop == DFS_Stack[ len( DFS_Stack) -1 ]: 
				if times[curTop][1] == 0:
					time += 1
					times[curTop][1] = time
					SCC[key].append( curTop )
				DFS_Stack.pop()
	
	return SCC

#Find largest SCC
def getBiggestSCC( components, adjacencyList ):
	numNodes = 0
	numEdges = 0
	maxKey = 0
	for each in components :
		if len(components[each]) > numNodes: 
			numNodes = len( components[each])
			numEdges = 0
			maxKey = each

	setVersion = set(components[maxKey] )
	for node in setVersion:
		for edge in adjacencyList[ node ]:
			if edge in setVersion : numEdges += 1 
	return numNodes, numEdges

#Takes a filename creates a list of couples
def createEdgeList( filename ):
	file = open( filename )
	lines = file.readlines()	#open and store the file into lines 
	type = lines[1].split()		#The second line has the type of graph 
										#Directed / Undirected: D / UD
	
	lines = lines[2:]				#only care about the lines that have the actual graph
	edgeList = []					#Edgelist will be a list of couples
	weights = dict()				#Weightlist will be a dictionary mapping vertex pairs to weights

	for each in lines:			#line format: Start_Vertex End_Vertex Weight
		tup = each.split()
		edgeList.append( (tup[0], tup[1])  )
		weights[ (tup[0], tup[1] ) ] = tup[2]
	return type, edgeList, weights

#Takes a list of couples representing edges
#returns a dictionary with vertices as a key, and a pair
	#( num edges, [list ofnodes] )
def getWCC( edgeList ):
	sets = dict()

	#initialize the sets
	for each in edgeList:
		sets[each[0]] = [ 0, [ each[0], ] ]
		sets[each[1]] = [ 0, [ each[1], ] ]

	#Loop Through Edge List
	for each in edgeList:	
		#if the two vertices are in the same set, increase edge count
		if sets[ each[0] ] is sets[ each[1] ]:
			sets[ each[0] ][0] += 1	
		else:
			#Find which is bigger
			if len( sets[ each[0] ][1] ) > len( sets[ each[1] ][1] ) :
				big, little = 0, 1
			else:
				big, little = 1, 0
			#Merge The two lists
			sets[ each[big] ][0] += 1 + sets[ each[little] ][0]
			sets[ each[big] ][1].extend( sets[ each[little] ][1] )
			for node in sets[ each[little] ][1]:		#Maintain list of old pointers
				sets[ node] = sets[ each[big] ]
	return sets

def getBiggestWCC( components ):
	edges = 0
	nodes = 0
	
	for key in components:
		if len( components[ key ][1] ) > nodes: 
			nodes = len( components[ key ][1] )
			edges = components[ key ][0]
	return (edges, nodes )

def main():
	if len( sys.argv ) < 4:  
		print( "[!]Please enter input file followed by source node, and an integer k")
		print( "[!]See Readme for more help")
		exit(1)
	file = sys.argv[1]
	type, edgelist, weights = createEdgeList( file )
	
	#Handle Undirected Graphs by adding an edge in the reverse
	#direction for each edge in the edgelist. Account for that
	#in the weights dictionary as well
	print( "[!]DEBUG {}".format( type ) )
	if type[0] == 'UD':
		print( "[!]DEBUG {}".format( type ) )
		reversed = []
		for each in edgelist: 
			reversed.append( ( each[1], each[0] ) )
			weights[ ( each[1], each[0] ) ] = weights[ each ]
		edgelist.extend( reversed )

	print( edgelist )
	for key in weights: print( "{} => {}".format( key, weights[key]) )


if __name__ == "__main__" : main()
