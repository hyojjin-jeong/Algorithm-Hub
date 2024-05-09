class Solution {
    public int solution(String s) {
        int size = s.length();
        int answer = 0;
        if (s.charAt(0) == '+') {
            answer = Integer.parseInt(s.substring(1,size));
        } else if (s.charAt(0) == '-') {
            answer = (-1) * Integer.parseInt(s.substring(1,size));
        } else {
            answer = Integer.parseInt(s);
        }
        return answer;
    }
}