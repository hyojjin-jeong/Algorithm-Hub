class Solution {
    public long solution(long n) {
        long answer = -1;
        long real = (long)Math.sqrt(n);
        if (real * real == n){
            answer = (real + 1) * (real + 1);
        }
        return answer;
    }
}