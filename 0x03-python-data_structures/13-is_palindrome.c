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

	if (*head == NULL || (*head)->next == NULL)
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
		while (idx < len)
		{
			int i;

			beg = beg->next;
			last = beg;

			for (i = idx; i < len - 1; i++)
				last = last->next;
			idx++;
			len--;
			if (last->n != beg->n)
				return (0);
		}
		return (1);
	}
	return (0);
}
