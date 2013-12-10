import sys 

#Create Adjacency List to be used in the Algorithms
#Adjecency List also has node parent and node's d value
def createAdjacencyList( edgeList ):
	adjList = dict()
	
	for each in edgeList:
		adjList[ each[0] ] = [float('inf'), '',  [] ]
		adjList[ each[1] ] = [float('inf'), '',  [] ]
	for each in edgeList:
		adjList[ each[0] ][2].append( each[1] )

	return adjList

####################################################
#Dijkstra's Algorithm!
####################################################

#Initialization of the Graph
def initSingleSource( adjList, source ):
	#In the creation of the adjacency list, 
	#All verices d and p are set to default. 
	#Just set the source to be 0
	try:
		adjList[ source ][0] = 0
	except:
		print( "[!]Invalid source, not found in graph" )
		exit(0)

#Relaxing Method
def relax( u, v, weights, graph ):
	#Format of Graph Dictionary:
	#	graph[ u ] = [ distance, parent, adjacency list ]

	if graph[ v ][0] > ( graph[ u ][0] + weights[ (u, v) ] ):
		graph[ v ][0] = ( graph[ u ][0] + weights[ (u, v) ] )
		graph[ v ][1] = u

def dijkstra( adjList, weightList ):
	finishedSet = []		#Contains the elements that have been extracted from the queue
	
	#Create the queue from the graph   // Do this in O( V )
	pq = []
	for key in adjList: pq.append( (adjList[ key ][0 ] , key ) )
	pq = sorted( pq )
	while pq:	#This loop will be done V times
		print( "\t[!]DEBUG PRINT OF QUEUE [!]\n{}".format(pq ) )
		finishedSet.append( pq[0] ) 	#add it to S. Takes O( 1 )
		pq = pq[1:]							#extract the min. Takes O( V )
		#relax all the adjacent verices to the current vertex //This has to run O( E ) times 
		for neighbor in adjList[ finishedSet[-1][1] ][2] :
			relax( finishedSet[-1][1] , neighbor, weightList, adjList )
		for each in adjList: print( "{} => {}".format( each, adjList[each] ) )
			#for each adjacent vertex, find it in O(V).
			#update it but dont reorder 

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
		weights[ (tup[0], tup[1] ) ] = int( tup[2] )
	return type, edgeList, weights


def main():
	if len( sys.argv ) < 4:  
		print( "[!]Please enter input file followed by source node, and an integer k")
		print( "[!]See Readme for more help")
		exit(1)

	#Check that the file is good
	file = sys.argv[1]
	try:
		open( file, "r" )
	except:
		print( "[!]Error Reading File!" )
		exit(0)

	#check that k is a valid integer
	try:
		k_value = int( sys.argv[3] )
	except:
		print("[!]Invalid k entry, k must be an integer")
		exit( 0 )

	type, edgelist, weights = createEdgeList( file )
	
	#Handle Undirected Graphs by adding an edge in the reverse
	#direction for each edge in the edgelist. Account for that
	#in the weights dictionary as well
	if type[0] == 'UD':
		reversed = []
		for each in edgelist: 
			reversed.append( ( each[1], each[0] ) )
			weights[ ( each[1], each[0] ) ] = weights[ each ]
		edgelist.extend( reversed )
	
	#Check that the source is in the graph
	source = sys.argv[2]

	#Create the Adjacency List
	graph = createAdjacencyList( edgelist )
	
	#Check that given source exists
	initSingleSource( graph, source )

	#Run Dijkstras
	dijkstra( graph, weights)
	

	#Run Shortest Reliable Path

if __name__ == "__main__" : main()
