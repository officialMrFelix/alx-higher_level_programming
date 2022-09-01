#include "lists.h"
#include <math.h>
#include <stdio.h>
int _pow(int x, int y);

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: head pointer to singly linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	listint_t *tail = NULL;
    	int nodes = 0;
	int limit = 0;
	double value1 = 0.0;
	double value2 = 0.0;
	int i = 0;
	
	/*Empty list is palindrome*/
	if (*head = NULL)
		return (1);

	/*Count nodes*/
	while (current != NULL)
	{
		current = current->next;
		nodes++;
	}
printf("Number of nodes:%d\n",nodes);
	/*List with one node is palindrome*/
	if (nodes == 1)
		return (1);
printf("I reached here\n");
	/*Palindrome even case*/
	if (nodes % 2 == 0)
	{
		limit = nodes / 2;
		current = *head;

		for(i = 0; i < limit; i++)
		{
			value1 = (value1 * 10) + current->n;
			current = current->next;
		}
/*
		for(i = 0; current == NULL; i++)
		{
			value2 = (value2 / 10) + current->n;
			current = current->next;
		}
		value2 = value2 / (1 / _pow(10,i));*/
	}
printf("value1: %f, value2:%f", value1, value2);

	/*Palindrome odd case*/
	

}

int _pow(int x, int y)
{
	int i;
	int product = 1;
	
	if (y == 0)
		return (1);
	if (y == 1)
		return (x);
	for (i = 0; i < y; i++)
	{
		 product = product * x;
	}
	return (product);
}
