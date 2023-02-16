#include <stdio.h>
void main()
{
int n, array[033],key,i, j;
printf("Enter the no. of elements\n");
scanf("%d",&n);
printf("enter %d integers\n", n);
for (i = 0; i < n; i++)
{
	scanf("%d", & array[i]);
}
for (i = 1; i <= n - 1; i++)
{
       key = array[j];
       j = i-1;
	while (j > 0 && array[j] > key)
	{
	array[j   +1] = array[j];
	j--;
	}
}
printf("Sorted list in ascending ordeer:\n");
for (i = 0; i <= n-1; i++)
{
	printf("%d\n", array[i]);
}
getch();
}
