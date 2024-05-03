class Solution {
    public double solution(int[] arr) {
        double answer = 0;
        int size = arr.length;
        for (int a : arr) {
            answer += a;
        }
        answer /= size;
        return answer;
    }
}