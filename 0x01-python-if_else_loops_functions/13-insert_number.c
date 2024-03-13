#include "lists.h"


/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: A double pointer to the head of the list.
 * @number: The number to insert.
 *
 * Return: A poitner to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev, *next, *node;

	if (!*head)
		return (add_nodeint_end(head, number));

	prev = *head;
	next = prev->next;
	while (next && next->n <= number)
	{
		prev = next;
		next = prev->next;
	}

	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);

	node->n = number;
	/**
	 * If the new node is the smallest.
	 */
	if (prev->n > number)
	{
		*head = node;
		node->next = prev;
	}
	else
	{
		prev->next = node;
		node->next = next;
	}

	return (node);
}
