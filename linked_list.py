class node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next


class l_list(object):
    def __init__(self):
        self.num_nodes = 0
        self.head = None

    def insert(self, val):
        if self.head is None:
            self.head = node(val, None)
        else:
            old_head = self.head
            self.head = node(val, old_head)
        self.num_nodes += 1
        return self.head

    def size(self):
        return self.num_nodes

    def pop(self):
        if self.head is None:
            return None
        else:
            ret_val = self.head.val
            self.head = self.head.next
            self.num_nodes -= 1
            return ret_val

    def _print(self):
        if self.head is None:
            return ()
        retval = ''
        current_node = self.head
        while current_node is not None:
            retval += str(current_node.val)
            if current_node.next is not None:
                retval += ", "
            current_node = current_node.next
        return "(" + retval + ")"

    def search(self, val):
        current_node = self.head
        while current_node is not None:
            if current_node.val == val:
                return current_node
            current_node = current_node.next
        return None

    #a node is considered found if it has the same .val AND same .next
    def remove(self, node):
        if self.head is None:
            return
        elif self.head.val == node.val and self.head.next == node.next:
            self.head = self.head.next
            return
        previous_node = self.head
        current_node = self.head.next
        while current_node is not None:
            if current_node.val == node.val and current_node.next == node.next:
                previous_node.next = current_node.next
                return
            previous_node = current_node
            current_node = current_node.next
