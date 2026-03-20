class Solution:
    def findPreSuc(self, root, key):
        pre = None
        suc = None

        while root:
            if root.data == key:
       
                if root.left:
                    temp = root.left
                    while temp.right:
                        temp = temp.right
                    pre = temp

               
                if root.right:
                    temp = root.right
                    while temp.left:
                        temp = temp.left
                    suc = temp
                break

            elif key < root.data:
                suc = root
                root = root.left
            else:
                pre = root
                root = root.right

        return pre, suc