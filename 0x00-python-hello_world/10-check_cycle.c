#include "lists.h"
/**
  *check_cycle - checks if there is a loop in a linked list
  *@list: linked list
  *
  *Return: either 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;

	if (list == NULL)
	{
		return (0);
	}
	slow = list;
	fast = list->next;
	while (slow != fast)
	{
		if (fast == NULL || fast->next == NULL)
		{
			return (0);
		}
		slow = slow->next;
		fast = fast->next->next;
	}
	return (1);


}
