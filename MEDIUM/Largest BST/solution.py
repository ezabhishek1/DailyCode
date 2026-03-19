class Solution:
    def largestBst(self, root):
        def post_order(node):
            if not node:
                return (True, 0, float('inf'), float('-inf'))
            
            left_is_bst, left_size, left_min, left_max = post_order(node.left)
            right_is_bst, right_size, right_min, right_max = post_order(node.right)
            
            if left_is_bst and right_is_bst and left_max < node.data < right_min:
                return (
                    True, 
                    left_size + right_size + 1, 
                    min(node.data, left_min), 
                    max(node.data, right_max)
                )
            else:
                return (False, max(left_size, right_size), float('-inf'), float('inf'))
        
        _, max_bst_size, _, _ = post_order(root)
        return max_bst_size