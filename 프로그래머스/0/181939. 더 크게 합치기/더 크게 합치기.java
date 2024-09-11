class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        String front = "" + a + b;
        String back = "" + b + a;
        int iF = Integer.valueOf(front);
        int iB = Integer.valueOf(back);
        if (iF < iB) {
            answer = iB;
        } else {
            answer = iF;
        }
        return answer;
    }
}