#include <stdio.h>

int main()
{
	int a[10001], testcase, x, ret;

	for (ret = 0; ret < 10001; ret++)
	{
		a[ret] = -1;
	}
	
	scanf("%d %d", &testcase, &x);

	for (ret = 0; ret < testcase; ret++)
	scanf("%d", &a[ret]);

	for (ret = 0; ret < testcase; ret++)
	{
		if (a[ret] < x && 0 <= a[ret])
			printf("%d ", a[ret]);
	}
}
