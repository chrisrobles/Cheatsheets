/*Graph
an ordered pair of G = (V, E) comprising 
a set V of vertices or nodes together with 
a set E of edges or arcs, which are 2-element subsets of V 
(i.e. an edge is associated with two vertices, and that association takes the form of the unordered pair comprising those two vertices)

Undirected Graph: a graph in which the adjacency relation is symmetric. 
So if there exists an edge from node u to node v (u -> v), then it is also the case that there exists an edge from node v to node u (v -> u)

Directed Graph: a graph in which the adjacency relation is not symmetric. 
So if there exists an edge from node u to node v (u -> v), this does not imply that there exists an edge from node v to node u (v -> u)
*/
// A simple representation of graph using STL 
#include<bits/stdc++.h> 
using namespace std; 

// A utility function to add an edge in an 
// undirected graph. 
void addEdge(vector<int> adj[], int u, int v) 
{ 
	adj[u].push_back(v); 
	adj[v].push_back(u); 
} 

// A utility function to print the adjacency list 
// representation of graph 
void printGraph(vector<int> adj[], int V) 
{ 
	for (int i = 0; i < V; ++i) 
	{ 
		cout << "\n Adjacency list of vertex "
			<< i << "\n head "; 
		for (auto x : adj[i]) 
		cout << "-> " << x; 
		printf("\n"); 
	} 
} 

// Driver code 
int main() 
{ 
	int V = 5; 
	vector<int> adj[V]; 
	addEdge(adj, 0, 1); 
	addEdge(adj, 0, 4); 
	addEdge(adj, 1, 2); 
	addEdge(adj, 1, 3); 
	addEdge(adj, 1, 4); 
	addEdge(adj, 2, 3); 
	addEdge(adj, 3, 4); 
	printGraph(adj, V); 
	return 0; 
} 
