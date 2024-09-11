class Solution {
    public String solution(String str1, String str2) {
        String answer = "";
        int size = str1.length();
        for (int i = 0; i < size; i++) {
            answer += str1.substring(i,i+1);
            answer += str2.substring(i,i+1);
        }
        return answer;
    }
}