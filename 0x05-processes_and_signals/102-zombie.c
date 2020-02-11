#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * infinite_while - put the parent on sleep.
 * Return: zero.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - main function.
 * Return: zero.
 */
int main(void)
{
	pid_t new_proc;
	int count = 0;

	while (count < 5)
	{
		new_proc = fork();
		if (new_proc == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
		count++;
	}
	infinite_while();
	return (0);
}
