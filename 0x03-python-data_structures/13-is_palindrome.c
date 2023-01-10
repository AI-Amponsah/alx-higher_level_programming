#include "lists.h"
/**
  *find_mid - finds the middle node
  *@head: head node
  *Return: middle node
  */
listint_t *find_mid(listint_t *head)
{
listint_t *slow = head;
listint_t *fast = head;

while (fast != NULL && fast->next != NULL)
{
fast = fast->next->next;
slow = slow->next;
}
return (slow);
}
/**
  *reverse - reverses the second part of the list
  *@head: head node
  *Return: temp
  */
listint_t *reverse(listint_t *head)
{
listint_t *temp;

if (head == NULL || head->next == NULL)
return (head);
temp = reverse(head->next);
head->next->next = head;
head->next = NULL;
return (temp);
}
/**
  *is_palindrome - checks if a linked list is palindrome
  *@head: head pointer
  *Return: True or False
  */
int is_palindrome(listint_t **head)
{
listint_t *mid = find_mid(*head);
mid = reverse(mid);
while (mid != NULL)
{
if ((*head)->n != mid->n)
return (0);
(*head) = (*head)->next;
mid = mid->next;
}
return (1);
}
