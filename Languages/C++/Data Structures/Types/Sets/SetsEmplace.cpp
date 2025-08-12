// C++ code to demonstrate the working of emplace() 
// and emplace_hint() 
#include<iostream> 
#include<set> // for set operations 
using namespace std; 

int main() 
{ 
	// declaring set 
	set<int> st; 

	// declaring iterators 
	set<int>::iterator it = st.begin(); 
	set<int>::iterator it1, it2; 

	// declaring pair for return value of set containing 
	// set iterator and bool 
	pair< set<int>::iterator,bool> ptr; 

	// using emplace() to insert single element 
	// inserting 24 
	ptr = st.emplace(24); 

	// checking if the element was already present or 
	// newly inserted returns true. newly inserted 
	if (ptr.second) 
		cout << "The element was newly inserted" ; 
	else cout << "The element was already present" ; 

	// printing set elements after insertion 
	cout << "\nThe set elements after 1st insertion are : "; 
	for (it1 = st.begin(); it1!=st.end(); ++it1) 
		cout << *it1 << " "; 

	// using emplace() to insert single element 
	// inserting 24 // not inserted this time 
	ptr = st.emplace(24); 

	// checking if the element was already present or 
	// newly inserted returns false. already inserted 
	if (ptr.second) 
		cout << "\nThe element was newly inserted" ; 
	else cout << "\nThe element was already present" ; 

	// printing set elements after insertion 
	cout << "\nThe set elements after 2nd insertion are : "; 
	for (it1 = st.begin(); it1!=st.end(); ++it1) 
		cout << *it1 << " "; 

	// inserting set elements using hint 
	st.emplace_hint(it,25); 

	// printing set elements after insertion 
	cout << "\nThe set elements after 3rd insertion are : "; 
	for (it1 = st.begin(); it1!=st.end(); ++it1) 
		cout << *it1 << " "; 
} 
