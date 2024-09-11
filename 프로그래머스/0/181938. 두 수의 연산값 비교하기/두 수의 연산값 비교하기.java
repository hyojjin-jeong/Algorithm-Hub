class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        int plus = Integer.valueOf("" + a + b);
        int two = 2 * a * b;
        answer = plus < two ? two : plus;
        return answer;
    }
}