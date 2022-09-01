#include "lists.h"
int digit_count(int);

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: head pointer to singly linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 * Authour: Felix Obianozie
 */

int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int nodes = 0;
	int limit = 0;
	int tmp = 1;
	int i = 0;
	int j = 0;

	long double value1 = 0;
	long double value2 = 0;

	/*Empty list is palindrome*/
	if (*head == NULL)
		return (1);

	/*Count nodes*/
	while (current != NULL)
	{
		current = current->next;
		nodes++;
	}
	current = *head;

	/*List with one node is palindrome*/
	if (nodes == 1)
		return (1);

	/*Palindrome in an even case*/
	if (nodes % 2 == 0)
	{
		limit = nodes / 2;
		for (i = 0; i < limit; i++)
		{
			j = 0;
			tmp = digit_count(current->n);
			while (j < tmp)
			{
				value1 = value1 * 10;
				j++;
			}
			value1 = value1 + current->n;
			current = current->next;
		}

		tmp = 1;
		for (i = 0; current != NULL; i++)
		{
			while (value2 >= 1)
			{
				value2 = value2 / 10;
				if (i > 0)
					tmp = tmp * 10;
			}
			value2 = value2 + current->n;
			current = current->next;
		}
		value2 = value2 * tmp;
	}

	/*Palindrome in an odd case*/
	if (nodes % 2 != 0)
	{
		limit = (nodes / 2) + 1;
		for (i = 0; i < limit; i++)
		{
			j = 0;
			tmp = digit_count(current->n);
			while (j < tmp)
			{
				value1 = value1 * 10;
				j++;
			}
			value1 = value1 + current->n;
			tmp = current->n;
			current = current->next;
		}

		value2 = tmp;
		tmp = 1;
		for (i = 0; current != NULL; i++)
		{
			while (value2 >= 1)
			{
				value2 = value2 / 10;
				tmp = tmp * 10;
			}
			value2 = value2 + current->n;
			current = current->next;
		}
		value2 = value2 * tmp;
	}

	if (value1 == value2)
		return (1);
	return (0);
}

/**
 * digit_count - estimates the number of digits of a given integer value.
 * @value: the supposed integer value
 *
 * Return: number of digits of given integer.
 */

int digit_count(int value)
{
	int count = 0;

	while (value >= 1)
	{
		value = value / 10;
		count++;
	}

	return (count);
}
