#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 *
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

/**
 * is_member - Checks if a given pointer is a member
 *             of a list.
 * @list: The list.
 * @node: The node to check.
 *
 * Return: 1 true otherwise, 0.
 */
int is_member(listint_t *list, listint_t *node);


/**
 * add_nodeptr - Adds a new node pointer add the end the a list.
 * @list: A pinter to the head of the list.
 * @node: The node to add.
 */
void add_nodeptr(listint_t *list, listint_t *node);
#endif /* LISTS_H */
