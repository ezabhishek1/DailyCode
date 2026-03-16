class Solution {
    static class Pair {
        Node node;
        int hd; // horizontal distance
        Pair(Node n, int h) { node = n; hd = h; }
    }
    public ArrayList<ArrayList<Integer>> verticalOrder(Node root) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<>();
        if (root == null) return result;

        // Map from HD -> list of nodes in level order
        Map<Integer, ArrayList<Integer>> map = new TreeMap<>();
        Queue<Pair> q = new LinkedList<>();
        q.add(new Pair(root, 0));

        while (!q.isEmpty()) {
            Pair p = q.poll();
            Node curr = p.node;
            int hd = p.hd;

            map.putIfAbsent(hd, new ArrayList<>());
            map.get(hd).add(curr.data);

            if (curr.left != null) q.add(new Pair(curr.left, hd - 1));
            if (curr.right != null) q.add(new Pair(curr.right, hd + 1));
        }

        // Collect results from leftmost HD to rightmost HD
        for (ArrayList<Integer> col : map.values()) {
            result.add(col);
        }

        return result;
    }
}