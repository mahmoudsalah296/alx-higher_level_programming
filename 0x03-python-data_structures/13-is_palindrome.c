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
	listint_t *tail = *head, *tmp = *head;
	int len = 0, idx = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (tail->next)
	{
		len++;
		tail = tail->next;
	}
	if ((*head)->n != tail->n)
		return (0);
	idx += 1;
	len -= 1;
	while (len > idx)
	{
		tmp = tmp->next;
		tail = tmp;
		for (i = idx; i < len; i++)
		{
			tail = tail->next;
		}
		if (tmp->n != tail->n)
			return (0);
		idx++;
		len--;
	}
	return (1);
}
