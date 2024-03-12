#include <stdio.h>
#define LIMIT 15 // the limit for the loops

/* Prints the Fibonacci sequence, starting with 1 and ending with 987. 
* Author: Angelle Leger */
int numbers[LIMIT];

int fibonacci(int n, int numbers[]){
	for (int i = 3; i < LIMIT; i++){
		n = numbers[i-1] + numbers[i-2];
		numbers[i] = n;
			} 
	return n;
}
int main(){
  numbers[0] = 1; // 1st number
	numbers[1] = 2; // 2nd number
	numbers[2] = numbers[0] + numbers[1]; // 3rd number - establishing the pattern
	fibonacci(numbers[2], numbers);
	for (int i = 0; i < LIMIT; i++){
		printf("%d\n", numbers[i]);
				}
	return 0;
}
