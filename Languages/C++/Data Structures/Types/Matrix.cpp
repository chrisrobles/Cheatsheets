#include<iostream>
using namespace std;

int main() {
   int mat[3][3]; // matrix can have max 3 rows and 3 cols
   int i, j;
   cout << "Enter the matrix elements row-wise :- " << endl;
   for ( i = 0; i < 3; i++ ) { // outer loop iterates over each row
      for ( j = 0; j < 3; j++ ) { // inter loop iterates over each column
         cout << "mat[" << i << "][" << j << "] : ";
         // i -> row no. and j -> col no.
         cin >> mat[i][j];
      }
   }
   // display the matrix
   cout << "You have entered the matrix :- " << endl;
   for ( i = 0; i < 3; i++ ) {
      for ( j = 0; j < 3; j++ ) {
         cout << mat[i][j] << " ";
      }
      cout << endl;
   }
   return 0;
}