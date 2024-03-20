#include <stdio.h>

/* The user may enter a number (n) to find the nth number in the Fibonacci sequence. This is an example of a recursive function. 
 * Angelle Leger */

int fibonacci(int n){
	if (n == 0){
		return 0; // First term in sequence
	} else if (n == 1){
		return 1; // Second and third terms in sequence
	} else {
	return fibonacci(n-1) + fibonacci(n-2); // nth terms in sequence
	}
}


int main(){
	int n;
	printf("Enter an integer to get the number at that place in the Fibonacci sequence.\n");
	scanf("%d", &n); 
	printf("The number is: %d\n", fibonacci(n)); // Call recursive function
	return 0;
}
