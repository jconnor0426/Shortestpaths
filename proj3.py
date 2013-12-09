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
	file = sys.argv[1]
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
	
	#Create the Adjacency List

	#Run Dijkstras

	#Run Shortest Reliable Path

if __name__ == "__main__" : main()
