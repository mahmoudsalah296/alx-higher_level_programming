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
	int len = 0, i, idx = 0;
	listint_t *last = *head, *beg = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (last->next)
	{
		len++;
		last = last->next;
	}
	if (last->n != beg->n)
	{
		return (0);
	}
	else
	{
		idx++;
		len--;
		while (len > idx)
		{
			beg = beg->next;
			last = beg;
			for (i = idx; i < len; i++)
				last = last->next;
			if (beg->n == last->n)
			{
				idx++;
				len--;
				continue;
			}
			else
				return (0);
		}
	}
	return (1);
}
