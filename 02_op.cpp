#include <iostream>
#include <cstdio>

using namespace std;

int main(int argn, char * argv[]){
	int a = int(argv[0][0]);
	int b = int(argv[0][1]);

	cout << "argv[0] = " << argv[0] << '\n';	
	cout << "a, b = " << a << ", " << b  << '\n';

	b++;
	cout << "b++" << '\n';
	cout << "a, b = " << a << ", " << b  << '\n';

	b+=a;
	cout << "b+=a" << '\n';
	cout << "a, b = " << a << ", " << b  << '\n';

	return 0;
}
