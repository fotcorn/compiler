#include <stdio.h>

int main() {
	int a = 2000000000;
	int b = 2000000000;
	long long v = ((long long)a) * b;
    printf("%lld\n", v);
	return 0;
}
