# PROG 1403 – Spring 2026
# HW4 – Contact List, Version 2
# Team: Shriya Sreejith, Aditi Shashidara and Lilly Ye
# Author: Shriya Sreejith, Aditi Shashidara and Lilly Ye

class Node:
    def __init__(self, contact):
        self.contact = contact
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, contact):
        def _insert(node, contact):
            if node is None:
                return Node(contact)
            if (contact.last, contact.first) < (node.contact.last, node.contact.first):
                node.left = _insert(node.left, contact)
            else:
                node.right = _insert(node.right, contact)
            return node
        self.root = _insert(self.root, contact)

    def inorder(self):
        result = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.contact)
                _inorder(node.right)
        _inorder(self.root)
        return result

    def find(self, first, last):
        first = first.lower()
        last = last.lower()
        def _find(node):
            if node is None:
                return None
            if (last, first) == (node.contact.last, node.contact.first):
                return node
            elif (last, first) < (node.contact.last, node.contact.first):
                return _find(node.left)
            else:
                return _find(node.right)
        return _find(self.root)

    def delete(self, first, last):
        first = first.lower()
        last = last.lower()

        def _min_value_node(node):
            current = node
            while current.left:
                current = current.left
            return current

        def _delete(node, first, last):
            if node is None:
                return node
            if (last, first) < (node.contact.last, node.contact.first):
                node.left = _delete(node.left, first, last)
            elif (last, first) > (node.contact.last, node.contact.first):
                node.right = _delete(node.right, first, last)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                temp = _min_value_node(node.right)
                node.contact = temp.contact
                node.right = _delete(node.right, temp.contact.first, temp.contact.last)
            return node

        self.root = _delete(self.root, first, last)