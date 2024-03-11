#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it.
 *
 * @list: A pointer to a node of the list.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	/**
	 * A new list to keep track of all
	 * visited nodes.
	 */
	listint_t *head = NULL;

	if (!list || !list->next)
		return (0);

	while (list)
	{
		if (is_member(head, list))
		{
			free_listint(head);
			return (1);
		}

		add_nodeint(&head, list->n);
		list = list->next;
	}

	free_listint(head);
	return (0);
}


/**
 * is_member - Checks if a given pointer is a member
 *             of a list.
 * @list: The list.
 * @node: The node to check.
 *
 * Return: 1 true otherwise, 0.
 */
int is_member(listint_t *list, listint_t *node)
{
	while (list)
	{
		if (list->n == node->n)
			return (1);
		list = list->next;
	}

	return (0);
}


/**
 * add_nodeptr - Adds a new node pointer add the end the a list.
 * @list: A pinter to the head of the list.
 * @node: The node to add.
 */
void add_nodeptr(listint_t *list, listint_t *node)
{
	while (list->next)
	{
		list = list->next;
	}

	list->next = node;
	node->next = NULL;
}
