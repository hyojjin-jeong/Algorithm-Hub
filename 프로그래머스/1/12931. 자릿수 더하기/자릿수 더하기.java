import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        String num = String.valueOf(n);
        char[] numArray = num.toCharArray();
        for (char c : numArray) {
            int intc = c - '0';
            answer += intc;
        }

        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        

        return answer;
    }
}