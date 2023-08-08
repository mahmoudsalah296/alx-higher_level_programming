#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node -  inserts a number into a sorted singly linked list
 * @head: pointer to head of the list
 * @number: number to be added
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode = malloc(sizeof(listint_t));
	listint_t *current = *head;

	if (newnode == NULL)
		return (NULL);
	newnode->n = number;
	newnode->next = NULL;
	if (*head == NULL)
	{
		*head = newnode;
		return (newnode);
	}
	if (current->n > number)
	{
		newnode->next = current;
		*head = newnode;
		return (newnode);
	}
	while (current->next != NULL)
	{
		if (current->next->n > number)
		{
			newnode->next = current->next;
			current->next = newnode;
			return (newnode);
		}
		current = current->next;
	}
	current->next = newnode;
	return (newnode);
}
