#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - function to check if a list is plaindrome
 * @head: pointer to head of the list
 * Return: 1 if it is plaindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *last = *head;
	listint_t *beg = *head;
	int len = 1, idx = 0;

	if (*head == NULL)
		return (1);
	while (last->next)
	{
		len++;
		last = last->next;
	}
	if (last->n == beg->n)
	{
		len--;
		idx++;
		while (idx < len && idx != len)
		{
			int i;

			last = beg;
			for (i = idx + 1; i < len; i++)
				last = last->next;
			if (last->n == beg->n)
			{
				idx++;
				len--;
				continue;
			}
			idx++;
			len--;
		}
		if (idx > len || idx == len)
			return (1);
	}
	return (0);
}
