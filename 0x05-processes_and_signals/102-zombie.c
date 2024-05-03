#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
/**
 * infinite_while - Run an infinite while loop.
 *
 * Return:  0.
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
 * main - five zombie processes created
 *
 * Return: 0
 */
int main(void)
{
pid_t Pid_zb;
int x;

for (x = 0; x < 5; x++)
{
Pid_zb = fork();
if (Pid_zb > 0)
{
printf("Zombie process created, PID: %d\n", Pid_zb);
}
else
{
exit(0);
}
}
infinite_while();
return (0);
}
