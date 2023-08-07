#include "lists.h"
/**
 * check_cycle - check if the list has a cycle
 * @list: the list to be checked
 * Return: 0 if no cycle, 1 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	slow = fast = list;
	while (fast && fast->next && slow->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
