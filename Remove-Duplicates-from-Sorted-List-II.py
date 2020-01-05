/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* Solution::deleteDuplicates(ListNode* A) {
    
   if (NULL == A)
    {
        return A;
    }

    ListNode* start;
    ListNode* current;
    ListNode* next;
    ListNode* actualCurrent;

    current = A;
    next = A->next;
    start = NULL;
    actualCurrent = A;
    bool delCurrent = false;
    bool setStart = false;

    while (next)
    {        
        if (current->val == next->val)
        {
            delCurrent = true;
            current->next = next->next;
            delete next;
            next = current->next;             
        }
        else
        {
            ListNode* temp = current;
            current = current->next;
            next = current->next;
                            
            if (delCurrent)
            {
                delete temp;
                delCurrent = false;
                if (actualCurrent)
                    actualCurrent->next = NULL;
            }
            else
            {
                if (!setStart)
                {
                    start = temp;
                    actualCurrent = start;
                    setStart = true;
                }
                else
                {
                    actualCurrent->next = temp;
                    actualCurrent = actualCurrent->next;
                
                }
            }
        }
    }

    if (delCurrent)
    {
        delete current;
        delCurrent = false;
        current = NULL;
        if (actualCurrent)
                    actualCurrent->next = NULL;
    }

    if (setStart)
    {
        return start;
    }

    return current;
}