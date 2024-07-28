// C++ code to demonstrate the working of erase() 
#include<iostream> 
#include<set> // for set operations 
using namespace std; 

int main() 
{ 
	// declaring set 
	set<int> st; 

	// declaring iterators 
	set<int>::iterator it; 
	set<int>::iterator it1; 
	set<int>::iterator it2; 

	// declaring pair for return value of set containing 
	// set iterator and bool 
	pair< set<int>::iterator,bool> ptr; 

	// inserting values in set 
	for (int i=1; i<10; i++) 
		st.insert(i*5); 

	// printing initial set elements 
	cout << "The set elements after insertion are : "; 
	for (it1 = st.begin(); it1!=st.end(); ++it1) 
		cout << *it1 << " "; 

	it = st.begin(); 

	cout << endl; 

	// erasing element using iterator 
	// erases 2nd element i.e., 10 
	++it; 
	st.erase(it); 

	// printing set elements after deletion 
	cout << "The set elements after 1st deletion are : "; 
	for (it1 = st.begin(); it1!=st.end(); ++it1) 
		cout << *it1 << " "; 

	// erasing element using value 
	st.erase(40); 

	// printing set elements after deletion 
	cout << "\nThe set elements after 2nd deletion are : "; 
	for (it1 = st.begin(); it1!=st.end(); ++it1) 
		cout << *it1 << " "; 

	++it; 
	++it; 
	++it; 
	++it; 

	// erasing element using range iterator 
	// deletes 25 - last(45) 
	st.erase(it, st.end()); 

	// printing set elements 3rd deletion 
	cout << "\nThe set elements after 3rd deletion are : "; 
	for (it1 = st.begin(); it1!=st.end(); ++it1) 
		cout << *it1 << " "; 

	cout << endl; 
} 
