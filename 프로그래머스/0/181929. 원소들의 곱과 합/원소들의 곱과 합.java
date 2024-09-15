class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        int reduce = 1;
        int sum = 0;
        for (int n : num_list) {
            reduce *= n;
            sum += n;
        }
        if (reduce < Math.pow(sum,2)) {
            answer = 1;
        }
        return answer;
    }
}