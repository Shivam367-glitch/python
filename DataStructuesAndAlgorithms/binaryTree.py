from queue import Queue

class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
    
class BT:
    def __init__(self):
        self.root=None
    
    def insert(self,data):
        if self.root is None:
            self.root=TreeNode(data)
        else:
             self._insert_recursive(self.root, data)
            
    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursive(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursive(node.right, data)
        else:
            # data already exists
            pass 
    def inorder_traversal(self,node):
        if node is None:
            return
        self.inorder_traversal(node.left)
        print(node.data, end=" ")
        self.inorder_traversal(node.right)
    
        
    def preorder_traversal(self,node):
        if node is None:
            return
        print(node.data, end=" ")
        self.inorder_traversal(node.left)
        self.inorder_traversal(node.right)
    
    def postorder_traversal(self,node):
        if node is None:
            return
        self.inorder_traversal(node.left)
        self.inorder_traversal(node.right)
        print(node.data, end=" ")
    
    def level_order_traversal(self,node):
        if node is None:
            return
        q=Queue()
        
        q.put(node)
        
        while not q.empty():
            n=q.qsize()
            
            for i in range(n):
                node=q.get()
                print (node.data,end=" ")
                if not node.left is None:
                    q.put(node.left)
                if not node.right is None:
                    q.put(node.right)
    def delete(self, data):
        self.root = self._delete_recursive(self.root, data)

    def _delete_recursive(self, root, data):
        if root is None:
            return root

        if data < root.data:
            root.left = self._delete_recursive(root.left, data)
        elif data > root.data:
            root.right = self._delete_recursive(root.right, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node has two children, find the inorder successor
            successor = self._find_min(root.right)
            root.data = successor.data
            root.right = self._delete_recursive(root.right, successor.data)

        return root
    def search(self,node,data):
        if node is None:
            return node
        if node.data is data:
            return node
        if node.data <data:
            return self.search(node.right,data)
        if node.data> data:
              return self.search(node.left,data)
          
            
        

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node
        
                
if __name__=="__main__":
    tree = BT()
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(2)
    tree.insert(4)
    tree.insert(6)
    tree.insert(8)
    tree.delete(8)
    print("Inorder Traversal:")
    tree.inorder_traversal(tree.root)
    print("\nPreorder Traversal:")
    tree.preorder_traversal(tree.root) 
    print("\nPostorder Traversal:")
    tree.postorder_traversal(tree.root) 
    
    print("\nLevelorder Traversal:")
    tree.level_order_traversal(tree.root)
    
    print("\nSearch Element 5 in Binary Tree:")
    aa=tree.search(tree.root,5)
    if aa  is None:
        print("Data is not present in Binary Tree")
    else : 
        print("TreeNode is Present in Binary Tree")
    
    
        
   