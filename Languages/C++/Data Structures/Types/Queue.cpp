/*
Queue
two principle operations: 
enqueue, which inserts an element into the queue 
dequeue, which removes an element from the queue

First in, first out data structure (FIFO): the oldest added object is the first to be removed

Time Complexity:
Access: O(n)
Search: O(n)
Insert: O(1)
Remove: O(1)
*/

#include <iostream> 
#include <queue> 

using namespace std; 

void showq(queue <int> gq) 
{ 
	queue <int> g = gq; 
	while (!g.empty()) 
	{ 
		cout << '\t' << g.front(); 
		g.pop(); 
	} 
	cout << '\n'; 
} 

int main() 
{ 
	queue <int> gquiz; 
	gquiz.push(10); 
	gquiz.push(20); 
	gquiz.push(30); 

	cout << "The queue gquiz is : "; 
	showq(gquiz); 

	cout << "\ngquiz.size() : " << gquiz.size(); 
	cout << "\ngquiz.front() : " << gquiz.front(); 
	cout << "\ngquiz.back() : " << gquiz.back(); 

	cout << "\ngquiz.pop() : "; 
	gquiz.pop(); 
	showq(gquiz); 

	return 0; 
} 
