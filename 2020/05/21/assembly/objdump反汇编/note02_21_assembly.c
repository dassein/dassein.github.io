#include <stdio.h>
#include <stdlib.h>
int global = 100;
int main(int argc, char const *argv[])
{
	int stack;
	static int BSS = 100;
	int *p = (int *)malloc(2 * sizeof(int));
	p[1] = 100;
	p[0] = 0;
	printf("Good");
	return 0;
}