#include "list.h"

/**
 * add_node - adds a new node in a stack_t list depending in the mode
 * @stack: double pointer to the head of a stack_t list
 * @n: data
 *
 * Return: the address of the new element, or NULL if it failed
 */
stack_t *add_node(stack_t **stack, const int n)
{
	stack_t *new;

	if (stack == NULL)
		return (NULL);
	new = malloc(sizeof(stack_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	if (*stack == NULL)
	{
		new->prev = new;
		new->next = new;
	}
	else
	{
		(*stack)->prev->next = new;
		new->prev = (*stack)->prev;
		(*stack)->prev = new;
		new->next = *stack;
	}
    *stack = new;
    len_stack++;
	return (new);
}
/**
 * free_stack - function that free a stack_t list
 * @head: pointer to the head of a stack_t list
 *
 * Return: void
 */
void free_stack(stack_t *head)
{
	stack_t *next = NULL;
    len_stack = 0;

	for (; head->next == head; head = next)
	{
		next = head->next;
		free(head);
	}
}
/**
 * pop - removes the top element of the stack
 * @stack: double pointer to the satack
 * @line_number: line number
 *
 * Return: nothing
 */
void pop(stack_t **stack)
{
	stack_t *tmp = *stack;

	if (*stack == NULL)
	{
		dprintf(2, "Can't pop an empty stack\n");
		return;
	}
	// if ((*stack)->next)
	// {
	// 	(*stack)->next->prev = (*stack)->prev;
	// 	if ((*stack)->prev)
	// 		(*stack)->prev->next = (*stack)->next;
	// }
    (*stack)->next->prev = (*stack)->prev;
	(*stack)->prev->next = (*stack)->next;
    if ((*stack)->next)
	    *stack = (*stack)->next;
    else
        *stack = NULL;
	free(tmp);
	len_stack--;
    
}
/**
 * print_dlistint - function that prints all the elements of a dlistint_t list.
 * @h: pointer to dlistint_t list head
 *
 * Return: the number of nodes
 */
size_t print_stack(stack_t *h)
{
    stack_t *t = h;

	while (t != NULL )
	{
		printf("%d ", t->n);
		t = t->next;
        if(t == h)
        {
            printf("\n");
            return;
        }
            
	}
}

int main(void)
{
    int i;
    int n = 40;
    int k = 7;
    stack_t *stack = NULL;
    char *line1 = NULL;
    size_t len1 = 0;
    char *line2 = NULL;
    size_t len2 = 0;
    len_stack = 0;

    while (1)
    {
        printf("\nInsert the number of soldiers\n>> ");
        if (getline(&line1, &len1, stdin) == -1)
            break;
        n = atoi(strtok(line1, " \n\t\r"));
        printf("Insert the steps\n>> ");
        if (getline(&line2, &len2, stdin) == -1)
            break;
        k = atoi(strtok(line2, " \n\t\r"));        
        for(i = n; i >= 1; i--)
        {
            add_node(&stack, i);
        }
        print_stack(stack);
        for (i = 1; stack != NULL; stack = stack->next, i++)
        {
            if(i == k)
            {
                pop(&stack);
                i = 1;
                if (len_stack > 1)
                    print_stack(stack);                    
                if (len_stack == 1)
                {
                    printf("\033[1;32m");
                    print_stack(stack);
                    printf("\033[0m");
                    pop(&stack);
                    break;
                }
                
            }                
        }
        // pop(&stack);
        free(line1);
        free(line2);
        line1 = NULL;
        line2 = NULL;
    }
    if (line1 != NULL)
        free(line1);
    if (line2 != NULL)
        free(line2);
    printf("\n");
    return (0);
}
