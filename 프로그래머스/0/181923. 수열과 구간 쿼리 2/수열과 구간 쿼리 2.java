import java.util.*;
class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = new int[queries.length];
        int index = 0;
        for (int[] q : queries) {
            ArrayList<Integer> newarr = new ArrayList<>();
            for (int i = 0; i < arr.length; i++) {
                if (q[0] <= i && i <= q[1] && arr[i] > q[2]) {
                    newarr.add(arr[i]);
                }
            }
            if (newarr.size() > 0) {
                answer[index] = Collections.min(newarr);
            } else {
                answer[index] = -1;
            }
            index++;
        }
        return answer;
    }
}