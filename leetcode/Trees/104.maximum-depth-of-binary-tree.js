/**
 * Definition for binary tree node.
 * function TreeNode (val) {
 *      this.val = val;
 *      this.left = this.right = null;
 * }
 */
/**
 * @param { TreeNode } root
 * @return { number }
 */
var maxDepth = function(root) {
    let maxNodes = (node, sum) {
        return Math.max(maxNodes(node.left, sum + 1), maxNodes(node.right, sum + 1));
    }
    return maxNodes(root, 0);
}