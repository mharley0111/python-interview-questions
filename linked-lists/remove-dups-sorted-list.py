class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

def deleteDuplicates(head: ListNode) -> ListNode:
	originalHead = head
	s = set()
	previous = ListNode()
	while head != None:
		if head.val in s:
			previous.next = head.next
		else:
			s.add(head.val)
			previous = head
		head = head.next
	return originalHead