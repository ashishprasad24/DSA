def isCircular(head):
    # Code here
    temp = head.next;
    while(temp!=None and temp!=head):
        temp=temp.next;
    return temp==head
