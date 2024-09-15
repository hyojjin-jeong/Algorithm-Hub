class Solution {
    public String solution(String code) {
        String answer = "";
        int mode = 0;
        int idx = 0;
        for (String c : code.split("")) {
            if (mode == 0) {
                if (c.equals("1")) {
                    mode = 1;
                } else {
                    if (idx % 2 == 0) {
                        answer += c;
                    }
                }
            } else {
                if (c.equals("1")) {
                    mode = 0;
                } else {
                    if (idx % 2 == 1) {
                        answer += c;
                    }
                }
            }
            idx += 1;
        }
        return answer == "" ? "EMPTY" : answer;
    }
}