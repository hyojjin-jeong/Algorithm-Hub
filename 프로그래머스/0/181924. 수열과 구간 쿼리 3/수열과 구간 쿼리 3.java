class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        for (int[] q : queries) {
            int first = arr[q[0]];
            int second = arr[q[1]];
            arr[q[0]] = second;
            arr[q[1]] = first;
        }
        return arr;
    }
}