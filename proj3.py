import sys 

#Create Adjacency List to be used in the Algorithms
#Adjecency List also has node parent and node's d value
def createAdjacencyList( edgeList ):
	adjList = dict()
	
	for each in edgeList:
		adjList[ each[0] ] = (float('inf'), '',  [] )
		adjList[ each[1] ] = (float('inf'), '',  [] )
	for each in edgeList:
		adjList[ each[0] ][2].append( each[1] )

	return adjList


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
	found_Source = False
	for each in edgelist:
		if source in each: 
			found_Source = True
			break
	if found_Source == False:
		print( "[!]Error Source Vertex not found in input" )
		exit(0)

	#Create the Adjacency List
	graph = createAdjacencyList( edgelist )

	for key in graph: print( "{} => {} ".format( key, graph[key] ) )
	#Run Dijkstras

	#Run Shortest Reliable Path

if __name__ == "__main__" : main()
