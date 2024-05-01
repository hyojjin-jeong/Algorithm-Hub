class Solution {
    public double solution(int[] numbers) {
        double answer = 0;
        double sum = 0;
        for (double num: numbers){
            sum += num;
        }
        double size = numbers.length;
        answer = sum / size;
        return answer;
    }
}