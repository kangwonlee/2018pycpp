#include <iostream>
#include <cstdio>

using namespace std;

int main(int argn, char * argv[]){
	int a = int(argv[0][0]);
	int b = int(argv[0][1]);

	printf("argv[0] = %s\n", argv[0]);	
	printf("a, b = %d, %d\n", a, b);

	b++;
	puts("b++\n");
	printf("a, b = %d, %d\n", a, b);

	b+=a;
	puts("b+=a\n");
	printf("a, b = %d, %d\n", a, b);

	b = a + b;
	puts("b = a + b\n");
	printf("a, b = %d, %d\n", a, b);

	return 0;
}
