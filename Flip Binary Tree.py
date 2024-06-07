def flip_bt(head):
	if head is not None:
		head.left, head,right = head.right, head,left
		flip_bt(head.left)
		flip_bt(head.right)