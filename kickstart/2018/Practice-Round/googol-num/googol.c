#include <stdio.h>

#define ISODD(num) (0x1 & num)

long nearlest_multiple(long num)
{
	if(num == 0)
		return 0;
	long count = 0;
	while(num != 1){
		num = num >> 1;
		count++;
	}
	return (long)1 << count;
}

int main(int argc, char const *argv[])
{
	int T;
	scanf("%d", &T);
	for(int i = 1; i <= T; i++)
	{
		long K;
		long nearest;
		scanf("%ld", &K);
		int count = 0;
		nearest = nearlest_multiple(K);
		while(K != nearest)
		{
			count++;
			K = (nearest << 1) - K;
			nearest = nearlest_multiple(K); 
		}
		printf("Case #%d: %d\n", i, ISODD(count));
	}
	return 0;
}
