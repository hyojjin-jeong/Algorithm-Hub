import java.lang.StringBuilder;
import java.util.Arrays;


class Solution {
    public long solution(long n) {
        long answer = 0;
        String[] str = String.valueOf(n).split("");
        Arrays.sort(str);
        
        StringBuilder sb = new StringBuilder();
        for (String s : str) {
            sb.append(s);
        }
        
        answer = Long.parseLong(sb.reverse().toString());
        return answer;
    }
}